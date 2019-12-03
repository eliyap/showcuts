## Dependency: sys
import copy, re
import warnings, logging

## Dependency: local
from share.process.action import action
from share.process.pieces import *
from share.process.components import *
from share.process.intent import *

# app URLs
filter_re = re.compile(r'is\.workflow\.actions\.filter\.(.+)')
property_re = re.compile(r'is\.workflow\.actions\.properties\.(.+)')
workflow_re = re.compile(r'is\.workflow\.actions\.(.+)')
editorial_re = re.compile(r'com\.omz\-software\.Editorial\.(.+)')
tally_re = re.compile(r'com\.agiletortoise\.Tally2\.(.+)')
accessibility_re = re.compile(r'com\.apple\.AccessibilityUtilities\.AXSettingsShortcuts\.(.+)')
bear_re = re.compile(r'net\.shinyfrog\.bear-IOS\.(.+)')
remote_re = re.compile(r'com\.apple\.TVRemoteUIService\.(.+)')
clock_re = re.compile(r'com\.apple\.mobiletimer-framework\.MobileTimerIntents\.(.+)')

def format_action(component: action, indent_level: int) -> (dict, int):
    indent_level = min(indent_level, 8) # cap indent level at 8
    title_elem = []
    line_elems = []
    list_items = [] # for dicts, lists, menus
    dict_items = []
    indent = 0
    special = ''  # indicates special elements
    impl = True # indicates unsupported elements
    options_impl = True # indicates unsupported line elements
    
    cat_info = {} #assign glyph
    for (app_url, info) in app_categorize.items():
        if app_url in component.name: cat_info = info
    if not cat_info:
        cat_info = categorize.get(component.name, {'glyph': 'missing', 'category': 'MISSING'})
    category, glyph = cat_info['category'], cat_info['glyph']
    result = cat_info.get('result', None)

    if component.name in no_params:
        title_elem = [no_params.get(component.name)]
    elif property_re.fullmatch(component.name):
        sub_name = property_re.fullmatch(component.name)[1]
        info = property_actions[sub_name]
        title_elem = [
            'Get',
            make_magic(component.parameters, 'WFContentItemPropertyName', info.get('default','Detail'), default_blank=('default' not in info), ask_text='Detail'),
            'from',
            make_magic(component.parameters, 'WFInput', info['name']),
        ]
        result = title_elem[1]['value']
        if result == 'Detail':
            result = f"Details of {info['name']}"
    elif filter_re.fullmatch(component.name):
        sub_name = filter_re.fullmatch(component.name)[1]
        info = filter_actions[sub_name]
        title_elem = [
            info['title'],
            make_magic(component.parameters, 'WFContentItemInputParameter', info['default'], default_blank=info['default_blank']),
        ]
        if 'files' == sub_name:
            options_impl = False
        elif "music" == sub_name:
            options_impl = False
        elif "articles" == sub_name:
            options_impl = False
            line_elems
        elif "images" == sub_name:
            options_impl = False
        elif "locations" == sub_name:
            options_impl = False
        elif "eventattendees" == sub_name:
            options_impl = False
        elif "calendarevents" == sub_name:
            options_impl = False
        elif "reminders" == sub_name:
            options_impl = False
        elif "notes" == sub_name:
            options_impl = False
        elif "contacts" == sub_name:
            options_impl = False
        elif "health.quantity" == sub_name:
            options_impl = False
        elif "photos" == sub_name:
            options_impl = False
        else:
            impl=False
        #TODO: add generalized handling
        # if any filters, title_elem += ['where']
        limit_elem = make_toggle(component.parameters,'WFContentItemLimitEnabled',False)
        line_elems += [{**{'label':'Limit'},**limit_elem}]
        if 'on' in limit_elem['class']:#content limited
            line_elems += [make_counter(component.parameters,'WFContentItemLimitNumber','Get # File',5,'Files'),]
    elif workflow_re.fullmatch(component.name):
        sub_name = workflow_re.fullmatch(component.name)[1]
        if sub_name in uni_params:
            get_text = uni_params.get(sub_name)
            title_elem = [
                get_text,
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
        elif sub_name in toggle_params:
            turn_text = toggle_params.get(sub_name)
            title_elem = [
                turn_text,
                on_off(component.parameters),
            ]

        # APP DONATED SHORTCUTS
        elif "sirikit.donation.handle" == sub_name:
            intent_info = get_intent(component.parameters)
            category, glyph = intent_info['category'], intent_info['glyph']
            title_elem = [text_elem(intent_info.get('remainder','Donated Action'))]
            special += "donated"
        elif "useractivity.open" == sub_name:
            info = app_categorize.get(component.parameters['AppBundleIdentifier'], {'glyph': 'missing', 'category': 'MISSING'})
            category, glyph = info['category'], info['glyph']
            title_elem = [text_elem(get_useractivity(component.parameters))]
            special += "donated"
            get_useractivity(component.parameters)
        # CASE BY CASE
        elif "reminders.showlist" == sub_name:
            title_elem = [
                'Show',
                make_magic(component.parameters, 'WFWorkflowActionParameters', 'List',default_blank=False),
            ]
        elif "removereminders" == sub_name:
            title_elem = [
                'Remove',
                make_magic(component.parameters, 'WFInputReminders', 'Reminders'),
            ]
        elif "addnewreminder" == sub_name:
            reminder_elem = make_magic(component.parameters, 'WFCalendarItemTitle', 'Reminder')
            rmd_list_elem = make_magic(component.parameters, 'WFCalendarItemCalendar', 'List',default_blank=False)
            alert_elem = make_magic(component.parameters, 'WFAlertEnabled', 'No Alert',default_blank=False)
            title_elem = [
                'Add',
                reminder_elem,
                'to',
                rmd_list_elem,
                'with',
                alert_elem,
            ]
            if alert_elem['value'] == 'Alert':
                alert_condition_elem = make_magic(component.parameters, 'WFAlertCondition', 'At Time',default_blank=False)
                if 'At Time' == alert_condition_elem['value']:
                    title_elem += [
                        alert_condition_elem,
                        make_magic(component.parameters, 'WFAlertCustomTime', '2:00 pm'),
                    ]
                elif 'Ask Each Time' == alert_condition_elem['value']:
                    title_elem = ['Add New Reminder']
                    line_elems = [
                        {**{'label':'Reminder'},**make_specify(component.parameters,'WFCalendarItemTitle','Text')},
                        {**{'label':'List'},**rmd_list_elem},
                        {**{'label':'Alert'},**make_pill(component.parameters,'WFAlertEnabled',['No Alert','Alert'],'No Alert')},
                        {**{'label':'Trigger'},**make_magic(component.parameters, 'WFAlertCondition', '<ask>'),},
                    ]
                elif alert_condition_elem['value'] in ['When I Arrive', 'When I Leave']:
                    title_elem += [
                        alert_condition_elem,
                        'at' if alert_condition_elem['value'] == 'When I Arrive' else 'from',
                        make_location(component.parameters, 'WFAlertCustomTime', 'Current Location', default_blank=False),
                    ]
                else: raise ValueError ('unexpected alert condition')
            options_impl = False # missing 'WFCalendarItemNotes'    
        elif "contacts" == sub_name:
            title_elem = []
            options_impl = False
        elif "phonenumber" == sub_name:
            title_elem = []
            options_impl = False
        elif "selectcontacts" == sub_name:
            title_elem = ['Select Contact']
            line_elems = [{**{'label':'Select Multiple'},**make_toggle(component.parameters,'WFSelectMultiple',False)}]
        elif "addnewevent" == sub_name:
            title_elem = [
                'Add',
                make_magic(component.parameters, 'WFCalendarItemTitle', 'Event Title'),
                'from',
                make_magic(component.parameters, 'WFCalendarItemStartDate', 'Tomorrow at midday'),
                'to',
                make_magic(component.parameters, 'WFCalendarItemEndDate', 'Tomorrow at 1 pm'),
            ]
            line_elems = [
                {**{'label':'Location'},**make_specify(component.parameters,'WFCalendarItemLocation','optional')},
                {**{'label':'Calendar'},**make_choose(component.parameters, 'WFCalendarItemCalendar', 'Calendar')},
                {**{'label':'All Day'},**make_toggle(component.parameters, 'WFCalendarItemAllDay', False)},
                {**{'label':'Alert'},**make_choose(component.parameters, 'WFAlertTime', 'Choose')},
                #notes 'WFCalendarItemNotes'
            ]
        elif sub_name in ['getupcomingevents','getupcomingreminders']:
            quantifier = {
                'getupcomingevents':'event',
                'getupcomingreminders':'reminder',
            }.get(sub_name)
            all_default = {
                'getupcomingevents':'Add Calendars',
                'getupcomingreminders':'Add Lists',
            }.get(sub_name)
            count_elem = make_magic(component.parameters, 'WFGetUpcomingItemCount', 'Input')
            try:
                count = int(float(count_elem['value']))
                count_elem['value'] = f'{count} {quantifier}' + ('' if count == 1 else 's')
            except ValueError:
                pass
            title_elem = [
                'Get',
                count_elem,
                'from',
                make_magic(component.parameters, 'WFGetUpcomingItemCalendar', all_default,default_blank=False),
            ]
            if 'getupcomingevents' == sub_name:
                line_elems = [{**{'label':'Day'},**make_choose(component.parameters, 'WFDateSpecifier', 'Any Day')}]
                if component.parameters.get('WFDateSpecifier','') == 'Specified Day':
                    line_elems += [{**{'label':'Specified Day'},**make_specify(component.parameters, 'WFSpecifiedDate', '29 June 2007')}]
                # if specified day, add specific day
        elif "removeevents" == sub_name:
            title_elem = [
                'Remove',
                make_magic(component.parameters, 'WFInputEvents', 'Events'),
            ]
            line_elems = [{**{'label':'Include Future Events'},**make_toggle(component.parameters, 'WFCalendarIncludeFutureEvents', False)}]
        elif "showincalendar" == sub_name:
            title_elem = [
                'Show',
                make_magic(component.parameters, 'WFEvent', 'Event'),
                'in Calendar',
            ]
        elif 'health.workout.log' == sub_name:
            title_elem = [
                'Log',
                make_magic(component.parameters, 'WFWorkoutReadableActivityType', 'Type',ask_text='Type'),
                'workout'
            ]
            line_elems = [
                {**{'label':'Date'},**make_specify(component.parameters,'WFWorkoutDate','optional')},
                #{**{'label':'Duration'},**},
                #{**{'label':'Calories'},**},
                #{**{'label':'Distance'},**},
            ]
            options_impl = False
        elif 'health.quantity.log' == sub_name:
            title_elem = ['Log Health Sample']
            line_elems = [
                {**{'label':'Type'},**make_choose(component.parameters, 'WFQuantitySampleType', 'Type')},
            ]
            options_impl = False
        elif 'openapp' == sub_name:
            app_url = component.parameters.get('WFAppIdentifier', None)
            # TODO: map URL -> name
            app_name = app_lookup.get(app_url, app_url)
            app_magic = magic(app_name) if app_url else magic(var_name='App', blank=True)
            title_elem = [
                'Open',
                app_magic,
            ]
            # add app name, if not blank
            # TODO: add app icon inside magic var
        elif 'comment' == sub_name:
            title_elem = [make_magic(component.parameters, 'WFCommentActionText', 'Enter comment...', force_magic=False)]
            special += ' comment'
        elif 'choosefrommenu' == sub_name:
            (UUID, group, mode) = control_flow(component.parameters)
            if 0 == mode:
                indent = +1
                title_elem = ['Choose from Menu']
            elif 1 == mode:
                indent_level -= 1
                title_elem = [component.parameters['WFMenuItemTitle']]
                special += ' flow'
            elif 2 == mode:
                indent_level -= 1
                indent = -1
                title_elem = ['End Menu']
                special += ' flow'
        elif 'exit' == sub_name:
            title_elem = [
                'Exit shortcut with',
                make_magic(component.parameters, 'WFResult', 'Result'),
            ]
        elif 'conditional' == sub_name:  # aka 'If'
            (UUID, group, mode) = control_flow(component.parameters)
            if 0 == mode:
                title_elem = conditional(component)# special handler for 'If' head block
                indent = +1
                result = None
            elif 1 == mode:
                indent_level -= 1
                title_elem = ['Otherwise']
                special += ' flow'
                result = None
            elif 2 == mode:
                indent_level -= 1
                indent = -1
                title_elem = ['End If']
                special += ' flow'
        elif 'repeat.count' == sub_name:
            # how does repeat index and repeat item look?
            (UUID, group, mode) = control_flow(component.parameters)
            count_elem = make_magic(component.parameters, 'WFRepeatCount', 'Count')
            try:
                count = int(float(count_elem['value']))
                count_elem['value'] = f'{count} time' + ('' if count==1 else 's')
            except ValueError:
                pass
            if 0 == mode:
                title_elem = [
                    'Repeat',
                    count_elem,
                ]
                indent = +1
            elif 2 == mode:
                indent_level -= 1
                indent = -1
                title_elem = ['End Repeat']
                special += ' flow'
        elif 'repeat.each' == sub_name:
            (UUID, group, mode) = control_flow(component.parameters)
            if 0 == mode:
                title_elem = [
                    'Repeat with each item in',
                    make_magic(component.parameters, 'WFInput', 'Input')
                ]
                indent = +1
            elif 2 == mode:
                indent_level -= 1
                indent = -1
                title_elem = ['End Repeat']
                special += ' flow'
        elif 'delay' == sub_name:
            delay_elem = make_magic(component.parameters, 'WFDelayTime', '1', default_blank=False)
            try:
                delay = int(float(delay_elem['value']))
                delay_elem['value'] = f'{delay} second' + ('' if delay == 1 else 's')
            except ValueError:
                pass
            title_elem = [
                'Wait',
                delay_elem,
            ]
        elif 'getdevicedetails' == sub_name:
            title_elem = [
                'Get the',
                make_magic(component.parameters, 'WFDeviceDetail', 'Device Name', default_blank=False),
            ]
        elif 'appearance' == sub_name:
            title_elem = [
                'Set appearance to',
                make_magic(component.parameters, 'style', 'Dark', default_blank=False),
            ]
        elif 'setbrightness' == sub_name:
            brightness = component.parameters.get('WFBrightness', .5)
            brightness_perc = f'{int(100*brightness)}%'
            title_elem = [
                'Set brightness to',
                magic(brightness_perc)
            ]
        elif 'dnd.set' == sub_name:
            DND_status = 'On' if component.parameters.get('Enabled',1) else 'Off'
            title_elem = [
                'Turn Do Not Disturb',
                magic(DND_status),
            ]
            if DND_status == 'On':
                end_elem = make_magic(component.parameters, 'AssertionType', 'Turned Off', default_blank=False)
                title_elem += [
                    'until',
                    end_elem,
                ]
                if 'Time' == end_elem['value']:
                    title_elem += [make_magic(component.parameters, 'Time', '7 pm'),]
                elif 'Event Ends' == end_elem['value']:
                    title_elem += [make_magic(component.parameters, 'Event', 'Event'),]
        elif 'flashlight' == sub_name:
            title_elem = [
                'Turn torch',
                make_magic(component.parameters, 'WFFlashlightSetting', 'On', default_blank=False),
            ]
        elif 'setplaybackdestination' == sub_name:
            try:
                route_elem = magic(component.parameters['WFMediaRoute']['routeName'])
            except KeyError:
                route_elem = magic('Device',True)
            title_elem = [
                'Set playback destination to',
                route_elem,
            ]
        elif 'setvolume' == sub_name:
            volume = component.parameters.get('WFVolume', .5)
            volume_perc = f'{int(100*volume)}%'
            title_elem = [
                'Set volume to',
                magic(volume_perc),
            ]
        elif 'dictionary' == sub_name:
            pass
            dict_items = get_dict(component.parameters)
        elif 'getvalueforkey' == sub_name:
            value_type = component.parameters.get('WFGetDictionaryValueType','Value')
            key_elems = [
                'for',
                make_magic(component.parameters, 'WFDictionaryKey', 'Key'),
            ] if value_type == 'Value' else []
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFGetDictionaryValueType', 'Value'),
                ]+ key_elems + ['in',
                make_magic(component.parameters, 'WFInput', 'Dictionary'),
            ]
        elif 'setvalueforkey' == sub_name:
            title_elem = [
                'Set',
                make_magic(component.parameters, 'WFDictionaryKey', 'Key'),
                'to',
                make_magic(component.parameters, 'WFDictionaryValue', 'Value'),
                'in',
                make_magic(component.parameters, 'WFInput', 'Dictionary'),
            ]
        elif 'base64encode' == sub_name:
            title_elem = [
                make_magic(component.parameters, 'WFEncodeMode', 'Mode'),
                make_magic(component.parameters, 'WFInput', 'Dictionary'),
                'with base64',
            ]
        elif 'hash' == sub_name:
            title_elem = [
                'Generate',
                make_magic(component.parameters, 'WFHashType', 'MD5', default_blank=False),
                'hash of',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
        elif 'count' == sub_name:
            title_elem = [
                'Count',
                make_magic(component.parameters, 'WFCountType', 'Items', default_blank=False),
                'in',
                make_magic(component.parameters, 'Input', 'Input'),
            ]
        elif 'setitemname' == sub_name:
            title_elem = [
                'Set name of',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'to',
                make_magic(component.parameters, 'WFName', 'Name'),
            ]
        elif 'choosefromlist' == sub_name:
            title_elem = [
                'Choose from',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
            multiple_elem = make_toggle(component.parameters,'WFChooseFromListActionSelectMultiple',False)
            line_elems = [
                {**{'label':'Prompt'},**make_specify(component.parameters,'WFChooseFromListActionPrompt','optional')},
                {**{'label':'Select Multiple'},**multiple_elem},
            ]
            if 'on' in multiple_elem['class']:
                line_elems += [{**{'label':'Select All Initially'},**make_toggle(component.parameters, 'WFChooseFromListActionSelectAll', False)}]
        elif "getepisodesforpodcast" == sub_name:
            title_elem = [
                'Get episodes of',
                get_podcast(component.parameters, 'WFInput', 'Podcast'),
            ]
        elif "playpodcast" == sub_name:
            title_elem = [
                'Play',
                get_podcast(component.parameters, 'WFPodcastShow', 'Podcast'),
            ]
        elif "searchpodcasts" == sub_name:
            title_elem = ['Search Podcasts']
            line_elems = [
                {**{'label':'Search'},**make_specify(component.parameters, 'WFSearchTerm', 'The Daily')},
                {**{'label':'Search By'},**make_choose(component.parameters, 'WFAttribute', 'All')},
                {**{'label':'Results'},**make_pill(component.parameters,'WFEntity',['Podcasts','Authors'],'Podcasts')},
                {**{'label':'Country'},**make_choose(component.parameters, 'WFCountry', 'United States')}, # not actually US default, but w/e
                make_counter(component.parameters,'WFItemLimit','# Item',25,'Number of Items'),
            ] 
        elif "podcasts.subscribe" == sub_name:
            title_elem = ['Subscribe to']
            podcasts = component.parameters.get('WFInput',[])
            if isinstance(podcasts, dict):
                title_elem += [make_magic(component.parameters, 'WFInput', 'Podcast URL'),]
            elif podcasts: # parse list of magic vars
                for elem in podcasts:
                    title_elem += [get_podcast({'elem':elem}, 'elem', 'Podcast URL'),]
            else: # unspecified
                title_elem += [magic('Podcast URL',True)]
        elif 'getitemfromlist' == sub_name:
            # cannot be a magic var, except 'Ask'
            specifier = component.parameters.get('WFItemSpecifier','First Item')
            if 'Item At Index' == specifier:
                title_mid = [
                    magic(specifier),
                    make_magic(component.parameters, 'WFItemIndex', '1'),
                ]
            elif 'Items in Range' == specifier:
                title_mid = [
                    magic(specifier),
                    make_magic(component.parameters, 'WFItemRangeStart', 'Start Index'),
                    'to',
                    make_magic(component.parameters, 'WFItemRangeEnd', 'End Index'),
                ]
            else:
                title_mid = [magic(specifier)]
            title_elem = ['Get'] + title_mid + ['from',make_magic(component.parameters, 'WFInput', 'List')]
        elif 'list' == sub_name:
            list_items = get_list(component.parameters)
            # kill inline due to formatting reasons
        elif 'math' == sub_name:
            'WFMathOperand'
            title_elem = [
                make_magic(component.parameters, 'WFInput', 'Number'),
                make_magic(component.parameters, 'WFMathOperation', '+', default_blank=False),
                make_magic(component.parameters, 'WFMathOperand', 'Number'),
            ]
            options_impl = False
            #TODO: scientific operation handling
        elif 'statistics' == sub_name:
            title_elem = [
                'Calculate the',
                make_magic(component.parameters, 'WFStatisticsOperation', 'Average', default_blank=False),
                'of',
                make_magic(component.parameters, 'Input', 'Input'),
            ]
        elif 'round' == sub_name:
            title_elem = [
                'Round',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'to',
                make_magic(component.parameters, 'WFRoundTo', 'Ones Place', default_blank=False),
            ]
            line_elems = [{**{'label':'Mode'},**make_choose(component.parameters, 'WFRoundMode', 'Normal')}]
        elif 'measurement.convert' == sub_name:
            try:
                unit = component.parameters['WFMeasurementUnit']['WFNSUnitSymbol']
            except KeyError:
                unit = None
            title_elem = [
                'Convert',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'into',
                make_magic(component.parameters, 'WFMeasurementUnitType', 'Length', default_blank=False),
                'in',
                magic(unit) if unit else magic('metres'),
            ]
        elif 'measurement.create' == sub_name:
            try:
                unit_dct = component.parameters['WFMeasurementUnit']['Value']
                magnitude = unit_dct['Magnitude'] 
                unit = unit_dct['Unit']
            except KeyError:
                magnitude, unit = None, None
            title_elem = [
                make_magic(component.parameters, 'WFMeasurementUnitType', 'Length', default_blank=False),
                magic(magnitude) if unit else magic('Value', True),
                magic(unit) if unit else magic('m'),
            ]
        elif 'getipaddress' == sub_name:
            title_elem = ['Get current IP address']
            # line elems
            options_impl = False
        elif 'getwifi' == sub_name:
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFNetworkDetailsNetwork', 'Wi-Fi', default_blank=False),
                'network\'s',
                make_magic(component.parameters, 'WFWiFiDetail', 'Network Name', default_blank=False),
            ]
        elif 'ask' == sub_name:
            title_elem = [
                'Ask',
                make_magic(component.parameters, 'WFAskActionPrompt', 'Question'),
            ]
            ask_elem = {**{'label':'Input Type'},**make_choose(component.parameters, 'WFInputType', 'Text')}
            line_elems = [ask_elem]
            if ask_elem['value'] in ['Text', 'URL']:
                default_elem = make_specify(component.parameters, 'WFAskActionDefaultAnswer', 'Text')
            elif 'Number' == ask_elem['value']:
                default_elem = make_specify(component.parameters, 'WFAskActionDefaultAnswerNumber', '0')
                default_elem['class'] = re.sub('empty','',default_elem['class'])
            elif 'Date' == ask_elem['value']:
                default_elem = make_specify(component.parameters, 'WFAskActionDefaultAnswerTime', 'Time')
            elif 'Time' == ask_elem['value']:
                default_elem = make_specify(component.parameters, 'WFAskActionDefaultAnswerNumber', '0')
            elif 'Date and Time' == ask_elem['value']:
                default_elem = make_specify(component.parameters, 'WFAskActionDefaultAnswerDateAndTime', 'Date and time')
            else:
                raise ValueError('Unexpected Question Type for Ask!')
            line_elems += [{**{'label':'Default Answer'},**default_elem}]
        elif 'playsound' == sub_name:
            title_elem = ['Play sound']
            line_elems = [{**{'label':'Sound File'},**make_choose(component.parameters, 'WFInput', 'Choose Variable')}]
        elif 'alert' == sub_name:
            title_elem = [
                'Show alert',
                make_magic(component.parameters, 'WFAlertActionTitle', 'Informational Message'),
            ]
            line_elems = [
                {**{'label':'Title'},**make_specify(component.parameters, 'WFAlertActionTitle', 'optional',align_left=True)},
                {**{'label':'Show Cancel Button'},**make_toggle(component.parameters, 'WFAlertActionCancelButtonShown', True)},
            ]
        elif 'notification' == sub_name:
            title_elem = [
                'Show notification',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
            options_impl = False
            # line elem
            'WFNotificationActionTitle'
        elif 'showresult' == sub_name:
            #might need custom formatting
            title_elem = [
                'Show',
                make_magic(component.parameters, 'Text', 'Result')
            ]
        elif 'format.filesize' == sub_name:
            title_elem = [
                'Format',
                make_magic(component.parameters, 'WFFileSize', 'File Size'),
                'into',
                make_magic(component.parameters, 'WFFileSizeFormat', 'Closest Unit', default_blank=False),
            ]
            options_impl = False
            # line elem, accepts magic vars
            'WFFileSizeIncludeUnits'
        elif 'format.number' == sub_name:
            places = make_magic(component.parameters,'WFNumberFormatDecimalPlaces', 'NO DEFAULT')
            places['value'] = f'{int(places["value"])} decimal places'
            title_elem = [
                'Format',
                make_magic(component.parameters, 'WFNumber', 'Number'),
                'to',
                places,
            ]
        elif 'date' == sub_name:
            title_elem = [make_magic(component.parameters, 'WFDateActionMode', 'Current Date', default_blank=False)]
            if 'Specified Date' == title_elem[0]['value']:
                title_elem += [make_magic(component.parameters, 'WFDateActionDate', '29 June 2007')]
            elif 'Ask Each Time' == title_elem[0]['value']:
                line_elems = [{**{'label':'Use'},**title_elem[0]}]
                title_elem = []
        elif 'adjustdate' == sub_name:
            title_elem = [
                make_magic(component.parameters, 'WFAdjustOperation', 'Add', default_blank=False),
                'from',
                make_magic(component.parameters, 'WFDate', 'Date'),
            ]
            if component.parameters.get('WFAdjustOperation','Add') in ['Add', 'Subtract']:
                title_elem = title_elem[:1] + get_duration(component.parameters, 0, 'second') + title_elem[1:]
        elif 'format.date' == sub_name:
            title_elem = [
                'Format',
                make_magic(component.parameters, 'WFDate', 'Date'),
            ]
            options_impl = False
            # line elems
            'WFDateFormatStyle' # and lots more!
        elif 'number' == sub_name:
            title_elem = [make_magic(component.parameters, 'WFNumberActionNumber', '42')]
        elif 'number.random' == sub_name:
            min_elem = make_magic(component.parameters, 'WFRandomNumberMinimum', 'Minimum')
            max_elem = make_magic(component.parameters, 'WFRandomNumberMaximum', 'Maximum')
            try: # coerce to int
                min_elem['value'] = int(float(min_elem['value']))
            except ValueError:
                pass
            try:
                max_elem['value'] = int(float(max_elem['value']))
            except ValueError:
                pass
            title_elem = [
                'Random number between',
                min_elem,
                'and',
                max_elem,
            ]
        elif 'runsshscript' == sub_name:
            title_elem = ['Run script over SSH']
            options_impl = False
            # shittons of option
        elif 'runworkflow' == sub_name:
            title_elem = [
                'Run',
                make_magic(component.parameters, 'WFWorkflowName', 'Shortcut'),
            ]
            if 'WFInput' in component.parameters:
                input_elem = make_magic(component.parameters, 'WFInput', 'ERROR')
            else:
                input_elem = {'class':'choose-var','value':'Choose Variable'}
            line_elems = [
                {**{'label':'Input'},**input_elem},
                {**{'label':'Show While Running'},**make_toggle(component.parameters, 'WFShowWorkflow', True)},
            ]
        elif 'appendvariable' == sub_name:
            title_elem = [
                'Add',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'to',
                make_magic(component.parameters, 'WFVariableName', 'Variable Name'),
            ]
        elif 'getvariable' == sub_name:
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFVariable', 'Variable'),
            ]
            logging.warn(DeprecationWarning('Get Variable has been deprecated as of iOS13.1'))
        elif 'setvariable' == sub_name:
            title_elem = [
                'Set variable',
                make_magic(component.parameters, 'WFVariableName', 'Variable Name'),
                'to',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
        elif 'openxcallbackurl' == sub_name:
            title_elem = [
                'Open',
                make_magic(component.parameters, 'WFXCallbackURL', 'X-Callback URL'),
                'with x-callback',
            ]
            options_impl = False
            # shittons of options
        elif 'urlencode' == sub_name:
            title_elem = [
                'URL',
                make_magic(component.parameters, 'WFEncodeMode', 'Encode', default_blank=False),
                make_magic(component.parameters, 'WFInput', 'Text'),
            ]
        elif "lightroom.import" == sub_name:
            impl = False
        elif "properties.appstore" == sub_name:
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFContentItemPropertyName', 'Detail'),
                'from',
                make_magic(component.parameters, 'WFInput', 'App Store app'),
            ]
        elif "searchappstore" == sub_name:
            title_elem = [
                'Search App Store for',
                make_magic(component.parameters, 'WFSearchTerm', 'Shortcuts'),
            ]
            line_elems = product_details(component.parameters)
        elif "recordaudio" == sub_name:
            title_elem = ['Record Audio']
            line_elems = []
            'WFRecordingCompression'
            'WFRecordingStart'
            'WFRecordingEnd'
            'WFRecordingTimeInterval' # in seconds, only true if 'After Time'
        elif "takephoto" == sub_name:
            preview_elem = make_magic(component.parameters, 'WFCameraCaptureShowPreview', True)
            if preview_elem['value'] == True:
                count_elem = make_magic(component.parameters, 'WFPhotoCount', 1)
                # detect float or int
                if isinstance(count_elem['value'], (float,int)):
                    count = int(float(count_elem['value']))
                    title_elem = [
                        'Take',
                        magic(f'{count} {"photo" if count==1 else "photos"}'),
                        'photo',
                    ] 
                preview_elem = toggle('on')
            elif preview_elem['value'] == False:
                title_elem = ['Take photo with']
                preview_elem = toggle('off')
            else: # magic var
                title_elem = ['Take photo with']
            title_elem += [
                make_magic(component.parameters, 'WFCameraCaptureDevice', 'Back', default_blank=False),
                'camera',
            ]
            line_elems = [{**{'label':'Show Camera Preview'},**preview_elem}]
        elif "takevideo" == sub_name:
            title_elem = [
                'Take video with',
                make_magic(component.parameters, 'WFCameraCaptureDevice', 'Back', default_blank=False),
                'camera',
            ]
            start_mode = make_magic(component.parameters, 'WFRecordingStart', 'Immediately', default_blank=False)
            start_mode['class'] = 'choose-var'
            line_elems = [
                {**{'label':'Quality'},**make_pill(component.parameters, 'WFCameraCaptureQuality', ['Low','Medium','High'],'Medium')},
                {**{'label':'Start Recording'},**start_mode},
            ]
        elif "addframetogif" == sub_name:
            title_elem = [
                'Add',
                make_magic(component.parameters, 'WFImage', 'Image'),
                'to',
                make_magic(component.parameters, 'WFInputGIF', 'GIF'),
            ]
            line_elems = [
                {**{'label':'Delay Time'},**make_specify(component.parameters, 'WFGIFDelayTime', '0.25')},
                {**{'label':'Auto Size'},**make_toggle(component.parameters, 'WFGIFAutoSize')},
            ]
            if component.parameters.get('WFGIFAutoSize') == False:
                line_elems += [
                    {**{'label':'Width'},**make_specify(component.parameters, 'WFGIFManualSizeWidth', '500')},
                    {**{'label':'Height'},**make_specify(component.parameters, 'WFGIFManualSizeHeight', '500')},
                ]
        elif "getframesfromimage" == sub_name:
            title_elem = [
                'Get frames from',
                make_magic(component.parameters, 'WFImage', 'Image'),
            ]
        elif "makegif" == sub_name:
            title_elem = [
                'Make GIF from',
                make_magic(component.parameters, 'WFInput', 'Content'),
            ]
            delay_elem = make_specify(component.parameters, 'WFMakeGIFActionDelayTime', '0.2')
            line_elems = [
                {**{'label':'Seconds per photo'},**delay_elem},
                {**{'label':'Loop Forever'},**make_toggle(component.parameters, 'WFMakeGIFActionLoopEnabled')},
            ]
            if component.parameters.get('WFMakeGIFActionLoopEnabled') == False:
                pass
                options_impl = False
                line_elems += [make_counter(component.parameters,
                    'WFMakeGIFActionLoopCount',
                    'Loop # Time',
                    1,
                    'Number of Loops',
                )]
            line_elems += [{**{'label':'Auto Size'},**make_toggle(component.parameters, 'WFMakeGIFActionAutoSize')}]
            if component.parameters.get('WFGIFAutoSize') == False:
                line_elems += [
                    {**{'label':'Width'},**make_specify(component.parameters, 'WFGIFManualSizeWidth', '500')},
                    {**{'label':'Height'},**make_specify(component.parameters, 'WFGIFManualSizeHeight', '500')},
                ]
        elif "makevideofromgif" == sub_name:
            title_elem = [
                'Make video from GIF',
                make_magic(component.parameters, 'WFInputGIF', 'Image'),
            ]
            line_elems = [make_counter(component.parameters,
                'WFMakeGIFActionLoopCount',
                'Loop # Time',
                1,
                'Number of Loops',
            )]
        elif "image.combine" == sub_name:
            mode_elem = make_magic(component.parameters, 'WFImageCombineMode', 'Horizontally', default_blank=False)
            if (mode_elem['class'], mode_elem['value']) == ('magic', 'Ask Each Time'):
                mode_elem['value'] = 'Mode' # special value, TODO TEST THIS!
            title_elem = [
                'Combine',
                make_magic(component.parameters, 'WFInput', 'Images'),
                mode_elem,
            ]
            line_elems = [{**{'label':'Spacing'},**make_specify(component.parameters, 'WFImageCombineSpacing', '0')}]
        elif "image.crop" == sub_name:
            title_elem = [
                'Crop',
                make_magic(component.parameters, 'WFInput', 'Image'),
            ]
            line_elems = image_crop(component.parameters)
        elif "image.flip" == sub_name:
            title_elem = [
                'Flip',
                make_magic(component.parameters, 'WFInput', 'Image'),
                make_magic(component.parameters, 'WFImageFlipDirection', 'Horizontally', default_blank=False),
            ]
        elif "avairyeditphoto" == sub_name:
            title_elem = [
                'Mark up',
                make_magic(component.parameters, 'WFDocument', 'Document'),
            ]
        elif "image.mask" == sub_name:
            mask_elem = make_magic(component.parameters, 'WFMaskType', 'Rounded Rectangle', default_blank=False)
            title_elem = [
                'Mask',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'with',
                mask_elem,
            ]
            if mask_elem['value'] in ['Ellipse','Icon']:
                title_elem += ['Shape']  
            elif mask_elem['value'] == 'Rounded Rectangle':
                title_elem += ['Shape']  
                line_elems = [{**{'label':'Corner Radius'},**make_specify(component.parameters, 'WFMaskCornerRadius', '0')}]
            elif mask_elem['value'] == 'Custom Image':
                title_elem += [make_magic(component.parameters, 'WFCustomMaskImage', 'Image')]  
        elif "overlayimageonimage" == sub_name:
            title_elem = [
                'Overlay',
                make_magic(component.parameters, 'WFImage', 'Image'),
                'on',
                make_magic(component.parameters, 'WFInput', 'Image'),
            ]
            editor_elem = make_toggle(component.parameters, 'WFShouldShowImageEditor', True)
            line_elems = [{**{'label':'Show Image Editor'},**editor_elem}]
            if 'off' in editor_elem['class']:
                line_elems += image_crop(component.parameters)
            opacity_elem = make_magic(component.parameters, 'WFOverlayImageOpacity', '100', default_blank=False)
            try:
                opacity_elem['value'] = int(float(opacity_elem['value']))
                opacity_elem['class'] = re.sub('magic','specify',opacity_elem['class'])
            except ValueError:
                pass
            line_elems += [{**{'label':'Opacity'},**opacity_elem}]
        elif "image.resize" == sub_name:
            title_elem = [
                'Resize',
                make_magic(component.parameters, 'WFImage', 'Image'),
                'to',
                make_magic(component.parameters, 'WFImageResizeWidth', 'Auto Width'),
                'x',
                make_magic(component.parameters, 'WFImageResizeHeight', 'Auto Height'),
            ]
        elif "image.rotate" == sub_name:
            title_elem = [
                'Rotate',
                make_magic(component.parameters, 'WFImage', 'Image'),
                'by',
                make_magic(component.parameters, 'WFImageRotateAmount', '90'),
                'degrees',
            ]
        elif "image.convert" == sub_name:
            title_elem = [
                'Convert',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'to',
                make_magic(component.parameters, 'WFImageFormat', 'JPEG', default_blank=False),
            ]
            line_elems = [
                #quality slider KMS 'WFImageCompressionQuality'
                # TODO lots of other options on a per format basis
            ]
            options_impl = False
        elif "searchitunes" == sub_name:
            title_elem = [
                'Search iTunes Store for',
                make_magic(component.parameters, 'WFSearchTerm', 'Search Term'),
            ]
            cat_elem = make_magic(component.parameters, 'WFMediaType', 'Music', default_blank=False)
            cat_elem['class'] = 'choose-var'
            line_elems = [{**{'label':'Category'},**cat_elem}] + product_details(component.parameters)
        elif "showinstore" == sub_name:
            title_elem = [
                'Show',
                make_magic(component.parameters, 'WFProduct', 'Product'),
                'in iTunes Store',
            ]
        elif "playmusic" == sub_name:
            try:
                music_elem = magic(component.parameters['WFMediaItems']['itemName'])
            except:
                music_elem = make_magic(component.parameters, 'WFMediaItems', 'Music')
            title_elem = [
                'Play',
                music_elem,
            ]
            line_elems = [
                {**{'label':'Shuffle'},**make_pill(component.parameters, 'WFPlayMusicActionShuffle', ['Off','Shuffle'], default='')},
                {**{'label':'Repeat'},**make_pill(component.parameters, 'WFPlayMusicActionRepeat', ['None','One','All'], default='')},
            ]
        elif "exportsong" == sub_name:
            title_elem = ['Select music']
            line_elems = [{**{'label':'Select Multiple Songs'},**make_toggle(component.parameters,'WFExportSongActionSelectMultiple',False)}]
        elif "deletephotos" == sub_name:
            title_elem = [
                'Delete',
                make_magic(component.parameters, 'WFInputPhotos', 'Photos'),
            ]
        elif sub_name in ['getlatestlivephotos','getlastphoto','getlastscreenshot','getlastvideo','getlatestbursts']:
            count_elem = make_magic(component.parameters, 'WFGetLatestPhotoCount', '1', default_blank=False)
            try:
                count = int(float(count_elem['value']))
                photo_type = {
                    'getlatestlivephotos':'live photo',
                    'getlastphoto':'photo',
                    'getlastscreenshot':'screenshot',
                    'getlastvideo':'video',
                    'getlatestbursts':'burst',
                }.get(sub_name)
                count_elem['value'] = f'{count} {photo_type}' + ('' if count == 1 else 's')
            except ValueError:
                pass
            title_elem = ['Get the latest', count_elem]
            if 'getlastphoto' == sub_name:
                line_elems = [{**{'label':'Include Screenshots'},**make_toggle(component.parameters,'WFGetLatestPhotosActionIncludeScreenshots',True)}]
        elif "savetocameraroll" == sub_name:
            title_elem = [
                'Save',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'to',
                make_magic(component.parameters, 'WFCameraRollSelectedGroup', 'Recents', default_blank= False),
            ]
        elif "selectphoto" == sub_name:
            title_elem = ['Select photos']
            line_elems = [{**{'label':'Select Multiple'},**make_toggle(component.parameters, 'WFSelectMultiplePhotos',False)}]
        elif "pausemusic" == sub_name:
            title_elem = [
                make_magic(component.parameters, 'WFPlayPauseBehavior', 'Play/Pause', default_blank=False),
                'on',
                replace_ask(make_magic(component.parameters, 'WFMediaRoute', 'iPhone', default_blank=False), 'Device'),# probably depends on the device being used
            ]
        elif "skipback" == sub_name:
            title_elem = [
                'Skip back to the',
                make_magic(component.parameters, 'WFSkipBackBehavior', 'Beginning',default_blank=False),
                'on',
                replace_ask(make_magic(component.parameters, 'WFMediaRoute', 'iPhone', default_blank=False), 'Device'),# probably depends on the device being used
            ]
        elif "skipforward" == sub_name:
            title_elem = [
                'Skip forwards on',
                replace_ask(make_magic(component.parameters, 'WFMediaRoute', 'iPhone', default_blank=False), 'Device'),# probably depends on the device being used
            ]
        elif "addtoplaylist" == sub_name:
            title_elem = [
                'Add',
                make_magic(component.parameters, 'WFInput', 'Music'),
                'to',
                make_magic(component.parameters, 'WFPlaylistName', 'My Music Library', default_blank = False),
            ]
        elif "createplaylist" == sub_name:
            title_elem = [
                'Create playlist',
                make_magic(component.parameters, 'WFPlaylistName', 'Playlist Name'),
                'with',
                make_magic(component.parameters, 'WFPlaylistItems', 'Music'),
            ]
            line_elems = [
                {**{'label':'Author'},**make_specify(component.parameters, 'WFPlaylistAuthor', 'Shortcuts')},
                {**{'label':'Description'},**make_specify(component.parameters, 'WFPlaylistDescription', 'All my favorites')},
            ]
        elif "get.playlist" == sub_name:
            title_elem = [
                'Get songs in',
                make_magic(component.parameters, 'WFPlaylistName', 'Playlist'),
            ]
        elif "addmusictoupnext" == sub_name:
            try:
                music_elem = magic(component.parameters['WFMusic']['itemName'])
            except KeyError:
                #TODO test handling for magic var music...
                music_elem = make_magic(component.parameters, 'WFMusic', 'Music')
            title_elem = [
                'Add',
                music_elem,
                'to',
                make_magic(component.parameters, 'WFWhenToPlay', 'Next',default_blank=False),
                'of Up Next',
            ]
        elif "encodemedia" == sub_name:
            title_elem = [
                'Encode',
                make_magic(component.parameters, 'WFMedia', 'Media'),
            ]
            options_impl = False
        elif "trimvideo" == sub_name:
            title_elem = [
                'Trim',
                make_magic(component.parameters, 'WFInputMedia', 'Media'),
            ]
        elif "makezip" == sub_name:
            title_elem = [
                'Make',
                make_magic(component.parameters, 'WFArchiveFormat', '.zip', default_blank=False),
                'archive from',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
            line_elems = [{**{'label':'Archive Name'},**make_specify(component.parameters, 'WFZIPName', 'optional')}]
        elif "openin" == sub_name:
            title_elem = [
                'Open',
                make_magic(component.parameters, 'WFInput', 'File'),
            ]
            menu_elem = make_toggle(component.parameters, 'WFOpenInAskWhenRun', True)
            line_elems = [{**{'label':'Show Open In Menu'},**menu_elem}]
            if 'on' in menu_elem['class']:
                title_elem += [
                    'in',
                    make_magic(component.parameters, 'WFOpenInAppIdentifier', 'Choose'),
                ]
        elif "previewdocument" == sub_name:
            title_elem = [
                'Show',
                make_magic(component.parameters, 'WFInput', 'Input'),
                'in Quick Look',
            ]
        elif "makepdf" == sub_name:
            title_elem = [
                'Make PDF from',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
            line_elems = [{**{'label':'Include Margin'},**make_toggle(component.parameters, 'WFPDFIncludeMargin', False)}]
            page_elem = make_magic(component.parameters, 'WFPDFIncludedPages', 'All Pages', default_blank=False)
            page_elem['class'] = 'choose-var'
            line_elems = [{**{'label':'Include'},**page_elem}]
            if 'All Pages' == page_elem['value']:
                pass
            elif 'Single Page' == page_elem['value']:
                line_elems += [{**{'label':'Page No.'},**make_specify(component.parameters, 'WFPDFSinglePage', '1')}]
            elif 'Page Range' == page_elem['value']:
                line_elems += [
                    {**{'label':'Start Page No.'},**make_specify(component.parameters, 'WFPDFPageRangeStart', '1')},
                    {**{'label':'End Page No.'},**make_specify(component.parameters, 'WFPDFPageRangeEnd', '3')},
                ]
        elif "generatebarcode" == sub_name:
            title_elem = [
                'Generate QR code from',
                make_magic(component.parameters, 'WFText', 'Text'),
            ]
            error_elem = make_magic(component.parameters, 'WFQRErrorCorrectionLevel', 'Medium', default_blank=False)
            error_elem['class'] = 'choose-var'
            line_elems = [{**{'label':'Error Correction'},**error_elem}]
        elif "url.getheaders" == sub_name:
            title_elem = [
                'Get headers from',
                make_magic(component.parameters, 'WFInput', 'URL'),
            ]
        elif "getrichtextfrommarkdown" == sub_name:
            title_elem = [
                'Make rich text from',
                make_magic(component.parameters, 'WFInput', 'Markdown Text'),
            ]
        elif "dictatetext" == sub_name:
            title_elem = ['Dictate Text']
            lang_elem = make_magic(component.parameters, 'WFSpeechLanguage', 'English') # device lang is set
            stop_elem = make_magic(component.parameters, 'WFDictateTextStopListening', 'After Pause')
            lang_elem['class'], stop_elem['class'] = ['choose-var'] * 2
            line_elems = [
                {**{'label':'Language'},**lang_elem},
                {**{'label':'Stop Listening'},**stop_elem},
            ]
        elif "getnameofemoji" == sub_name:
            title_elem = [
                'Get name of emoji in',
                make_magic(component.parameters, 'WFInput', 'Text'),
            ]
        elif "showdefinition" == sub_name:
            title_elem = [
                'Show definition of',
                make_magic(component.parameters, 'Word', 'word'),
            ]
        elif "detectlanguage" == sub_name:
            title_elem = [
                'Detect language of',
                make_magic(component.parameters, 'WFInput', 'Text'),
            ]
        elif "airdropdocument" == sub_name:
            title_elem = [
                'Airdrop',
                make_magic(component.parameters, 'WFInput', 'Content'),
            ]
        elif "getcurrentlocation" == sub_name:
            title_elem = ['Get current location'] 
        elif "location" == sub_name:
            title_elem = [make_location(component.parameters, 'WFLocation', 'Location')] 
        elif "address" == sub_name:
            title_elem = []
            line_elems = [
                {**{'label':'Line 1'},   **make_specify(component.parameters,'WFAddressLine1','44 Planter Road', align_left=True)},
                {**{'label':'Line 2'},   **make_specify(component.parameters,'WFAddressLine2','Text', align_left=True)},
                {**{'label':'Town/City'},**make_specify(component.parameters,'WFCity','Swindon', align_left=True)},
                {**{'label':'County'},   **make_specify(component.parameters,'WFState','Wiltshire', align_left=True)},
                {**{'label':'Postcode'}, **make_specify(component.parameters,'WFPostalCode','SN2 7BP', align_left=True)},
                {**{'label':'Region'},   **make_specify(component.parameters,'WFCountry','United Kingdom', align_left=True)},
            ] 
        elif "getmapslink" == sub_name:
            title_elem = [
                'Get maps URL from',
                make_location(component.parameters, 'WFInput', 'Location'),
            ] 
        elif "getdirections" == sub_name:
            title_elem = [
                'Show',
                make_magic(component.parameters, 'WFGetDirectionsActionMode', 'Driving', default_blank=False, ask_text='Mode'),
                'directions to',
                make_location(component.parameters, 'WFDestination', 'Destination', ask_text='Destination'),
            ] 
        elif "searchmaps" == sub_name:
            title_elem = [
                'Show',
                make_location(component.parameters, 'WFInput', 'Location'),
                'in Maps',
            ] 
        elif "getdistance" == sub_name:
            title_elem = [
                'Get distance from',
                make_location(component.parameters, 'WFGetDirectionsCustomLocation', 'Current Location', default_blank=False, ask_text='Start Location'),
                'to',
                make_location(component.parameters, 'WFGetDistanceDestination', 'End Location', ask_text='End Location'),
            ] 
            line_elems = [
                {**{'label':'Route Type'},**make_pill(component.parameters, 'WFGetDirectionsActionMode', ['Direct','Driving', 'Walking'], default='Direct')},
                {**{'label':'Unit'},**make_pill(component.parameters, 'WFDistanceUnit', ['Miles','Kilometers'], default='Kilometers')},
            ]
        elif "gethalfwaypoint" == sub_name:
            title_elem = [
                'Get halfway point between',
                make_location(component.parameters, 'WFGetHalfwayPointFirstLocation', 'First Location'),
                'and',
                make_location(component.parameters, 'WFGetHalfwayPointSecondLocation', 'Second Location'),
            ] 
        elif "gettraveltime" == sub_name:
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFGetDirectionsActionMode', 'Driving', default_blank=False, ask_text='Mode'),
                'time from',
                make_location(component.parameters, 'WFGetDirectionsCustomLocation', 'Current Location', default_blank=False, ask_text='Start Location'),
                'to',
                make_location(component.parameters, 'WFDestination', 'End Location',  ask_text='End Location'),
            ] 
        elif "searchlocalbusinesses" == sub_name:
            title_elem = [
                'Search for',
                make_magic(component.parameters, 'WFSearchQuery', 'Local Businesses'),
                'near',
                make_location(component.parameters, 'WFInput', 'Current Location', default_blank=False),
            ] 
        elif "weather.currentconditions" == sub_name:
            title_elem = [
                'Get current weather at',
                make_location(component.parameters, 'WFWeatherCustomLocation', 'Current Location', default_blank=False),
            ] 
        elif "weather.forecast" == sub_name:
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFWeatherForecastType', 'Daily'),
                'forecast at',
                make_location(component.parameters, 'WFWeatherCustomLocation', 'Current Location', default_blank=False),
            ] 
        elif "text.split" == sub_name:
            sep_elem = make_magic(component.parameters, 'WFTextSeparator', 'New Lines', default_blank=False)
            title_elem = [
                'Split',
                make_magic(component.parameters, 'text', 'Text'),
                'by',
                sep_elem,
            ]
            if sep_elem['value'] == 'Custom':
                title_elem += [make_magic(component.parameters, 'WFTextCustomSeparator', 'Custom Separator')]
        elif "text.combine" == sub_name:
            separator_elem = make_magic(component.parameters, 'WFTextSeparator', 'New Lines', default_blank=False,ask_text='Separator')
            title_elem = [
                'Combine',
                make_magic(component.parameters, 'text', 'Text List'),
                'with',
                separator_elem,
            ]
            if separator_elem['value'] == 'Custom':
                title_elem += [make_magic(component.parameters, 'WFTextCustomSeparator', 'Text'),]
        elif "text.replace" == sub_name:
            title_elem = [
                'Replace',
                make_magic(component.parameters, 'WFReplaceTextFind', 'Hello'),
                'with',
                make_magic(component.parameters, 'WFReplaceTextReplace', 'World'),
                'in',
                make_magic(component.parameters, 'WFInput', 'Text'),
            ]
            line_elems = [
                {**{'label':'Case Sensitive'},**make_toggle(component.parameters, 'WFReplaceTextCaseSensitive', True)},
                {**{'label':'Regular Expression'},**make_toggle(component.parameters, 'WFReplaceTextRegularExpression', False)},
            ]
        elif "downloadurl" == sub_name:
            title_elem = [
                'Get contents of',
                make_magic(component.parameters, 'WFURL', 'URL'),
            ]
            line_elems = [
            ]
            options_impl = False
        elif "gettext" == sub_name:
            """ # old system, might still be useful
            try:
                texts = component.parameters['WFTextActionText']
                if isinstance(texts,str):
                    title_elem = [text_elem(texts)]
                else:
                    title_elem = [get_inline(texts, magic_wrapper = False)]
                    logging.error(title_elem)
            except KeyError:
                title_elem = [{'class':'empty specify', 'value':'Text'}] #ld default
            """
            title_elem = [make_magic(component.parameters, 'WFTextActionText', 'Text', force_magic=False)]
            #title_elem = [{'class':'empty specify', 'value':'Text'}] old default
            special += ' text'
        elif "setclipboard" == sub_name:
            title_elem = [
                'Copy',
                make_magic(component.parameters, 'WFInput', 'Content'),
                'to clipboard',
            ]
            line_elems = [
                {**{'label':'Local Only'},**make_toggle(component.parameters,'WFLocalOnly',False)},
                {**{'label':'Expire At'},**make_specify(component.parameters,'WFExpirationDate','Today at 3 pm')},
            ]
        elif "sendemail"== sub_name: 
            title_elem=[
                'Send',
                make_magic(component.parameters, 'WFSendEmailActionInputAttachments', 'Message'),
                'to',
                # I can't implement these contact details right now. probably never used
                make_magic(component.parameters, 'WFInput', '<Recipients>'),
                'as',
                make_magic(component.parameters, 'WFSendEmailActionSubject', 'Subject'),
            ]
            options_impl = False
        elif "sendmessage"== sub_name: 
            title_elem=[
                'Send "',
                make_magic(component.parameters, 'WFSendMessageContent', 'Message'),
                '" to',
                # I can't implement these contact details right now. probably never used
                make_magic(component.parameters, 'WFInput', 'Recipients'),
            ]
        elif "getarticle" == sub_name:
            title_elem = [
                'Get article from',
                make_magic(component.parameters, 'WFWebPage', 'URL'),
            ]
        elif "rss" == sub_name:
            item_elem = make_magic(component.parameters, 'WFRSSItemQuantity', '10')
            try: # coerce to int
                item_count = int(float(item_elem['value']))
                item_elem['value'] = f'{item_count} item' + ('' if item_count == 1 else 's')
            except ValueError:
                pass
            
            title_elem = [
                'Get',
                item_elem,
                'from',
                make_magic(component.parameters, 'WFRSSFeedURL', 'https://www.apple.com/uk/newsroom/rss-feed.rss',default_blank=False),
            ]
        elif "rss.extract" == sub_name:
            title_elem = [
                'Get RSS feeds from',
                make_magic(component.parameters, 'WFURLs', 'Page'),
            ]
        elif "readinglist" == sub_name:
            title_elem = [
                'Add',
                make_magic(component.parameters, 'WFURL', 'URL'),
                'to Reading List',
            ]
        elif "openurl" == sub_name:
            title_elem = [
                'Open',
                make_magic(component.parameters, 'WFInput', 'Safari web page'),
            ]
        elif "runjavascriptonwebpage" == sub_name:
            title_elem = [
                'Run JavaScript on',
                make_magic(component.parameters, 'WFInput', 'Web page'),
            ]
            line_elems = [
                #make_line('',make_specify(component.parameters, 'WFJavaScript', 'JavaScript'),)
            ]
            options_impl = False # wow, they have a real JS thing... can't imagine the kinds of vulnerabilities this exposes my site to
        elif "searchweb" == sub_name:
            title_elem = [
                'Search',
                make_magic(component.parameters, 'WFSearchWebDestination', 'Google',default_blank=False),
                'for',
                make_magic(component.parameters, 'WFInputText', 'Text'),
            ]
        elif "showwebpage" == sub_name:
            title_elem = [
                'Show web page at',
                make_magic(component.parameters, 'WFURL', 'URL'),
            ]
            line_elems = [{**{'label':'Enter Safari Reader'},**make_toggle(component.parameters, 'WFEnterSafariReader',False)}]
        elif "url.expand" == sub_name:
            title_elem = [
                'Expand',
                make_magic(component.parameters, 'URL', 'URL'),
            ]
        elif "geturlcomponent" == sub_name:
            title_elem = [
                'Get',
                make_magic(component.parameters, 'WFURLComponents', 'Scheme',default_blank=False),
                'from',
                make_magic(component.parameters, 'WFURL', 'URL'),
            ]
        elif "url" == sub_name:
            title_elem = [make_magic(component.parameters, 'WFURLActionURL', 'apple.com'),]
        elif "getwebpagecontents" == sub_name:
            title_elem = [
                'Get contents of web page at',
                make_magic(component.parameters, 'WFInput', 'URL'),
            ]
        elif "venmo.request"== sub_name: 
            title_elem=[
                'Request $',
                make_magic(component.parameters, 'WFVenmoActionAmount', 'Amount', ask_text='Amount'),
                'from',
                #vcard handling 'WFVenmoActionRecipients'
                magic('<contacts>'),
            ]
            line_elems = [
                {**{'label':'App'},**make_choose(component.parameters,'','Apple Pay')},
                {**{'label':'Open in App'},**make_toggle(component.parameters,'WFVenmoActionAppSwitch',False)},
                # note
            ]
            if component.parameters.get('WFVenmoActionAppSwitch',None)==False:
                line_elems.insert(2,{**{'label':'Show When Run'},**make_toggle(component.parameters,'x',True)},)
        elif "venmo.pay"== sub_name: 
            title_elem=[
                'Send $',
                make_magic(component.parameters, 'WFVenmoActionAmount', '7.00', ask_text='Amount'),
                'to',
                #vcard handling 'WFVenmoActionRecipients'
                magic('<contacts>'),
            ]
            line_elems = [
                {**{'label':'App'},**make_choose(component.parameters,'x','Apple Pay')},
                {**{'label':'Open in App'},**make_toggle(component.parameters,'x',False)},
                #note
            ]
        elif "appendnote"== sub_name: 
            title_elem=[
                'Append',
                make_magic(component.parameters, 'WFInput', 'Text', ask_text='Text'),
                'to',
                make_magic(component.parameters, 'WFNote', 'Note',ask_text=None),
            ]
        elif "shownote"== sub_name: 
            title_elem=[
                'Show',
                make_magic(component.parameters, 'WFInput', 'Note'),
            ]
        elif "timer.start"== sub_name: 
            title_elem=['Start timer for'] + get_duration(component.parameters, 30, 'minute')
        elif "instapaper.add"== sub_name: 
            title_elem=[
                'Add',
                make_magic(component.parameters, 'WFInputURL', 'URL'),
            ]
            line_elems = [{**{'label':'Folder'},**make_choose(component.parameters, 'WFInstapaperFolder', 'Choose')}]
        elif "instapaper.get"== sub_name: 
            count_elem = make_magic(component.parameters, 'WFBookmarkCount', '5')
            try:
                count = int(float(count_elem['value']))
                count_elem['value'] = f'{count} bookmark' + ('' if count == 1 else 's')
            except ValueError:
                pass
            title_elem=[
                'Get',
                count_elem,
                'from',
                make_magic(component.parameters, 'WFInstapaperFolder', 'Folder'),
            ]
        elif "unzip"== sub_name: 
            title_elem=[
                'Extract',
                make_magic(component.parameters, 'WFArchive', 'Archive'),
            ]
        elif "file.createfolder"== sub_name: 
            title_elem=['Create Folder']
            service_elem = make_choose(component.parameters, 'WFFileStorageService', 'iCloud Drive')
            path_elem = make_specify(component.parameters, 'WFFilePath', 'Adventure/',align_left=True)
            if 'iCloud Drive' == service_elem['value']:
                path_elem['value'] = '/Shortcuts/' + path_elem['value']
            line_elems = [
                {**{'label':'Service'},**service_elem},
                {**{'label':'Path'},**path_elem},
            ]
        elif "file.delete"== sub_name: 
            title_elem=[
                'Delete',
                make_magic(component.parameters, 'WFInput', 'Files'),
            ]
            line_elems = [{**{'label':'Confirm Before Deleting'},**make_toggle(component.parameters,'WFDeleteFileConfirmDeletion',True)}]
        elif "documentpicker.open"== sub_name: 
            title_elem=['Get File']
            service_elem = make_choose(component.parameters, 'WFFileStorageService', 'iCloud Drive')
            picker_elem = make_toggle(component.parameters, 'WFShowFilePicker', True)
            line_elems = [
                {**{'label':'Service'},**service_elem},
                {**{'label':'Show Document Picker'},**picker_elem},
            ]

            if 'Ask Each Time' in picker_elem['value']:
                pass # no further questions
            elif 'off' in picker_elem['class']:
                path_elem = make_specify(component.parameters, 'WFFilePath', 'example.txt',align_left=True)
                if service_elem['value'] == 'iCloud Drive':
                    path_elem['value'] = '/Shortcuts/' + path_elem['value']
                line_elems += [
                    {**{'label':'File Path'},**path_elem},
                    {**{'label':'Error If Not Found'},**make_toggle(component.parameters, 'WFFileErrorIfNotFound', True)},
                ]
            elif 'on' in picker_elem['class']:
                line_elems += [{**{'label':'Select Multiple'},**make_toggle(component.parameters, 'SelectMultiple', False)}]
                if service_elem['value'] == 'Dropbox':
                    line_elems += [{**{'label':'Initial Path'},**make_specify(component.parameters, 'WFGetFileInitialDirectoryPath', 'optional',align_left=True)}]
        elif "documentpicker.save"== sub_name: 
            title_elem=[
                'Save',
                make_magic(component.parameters, 'WFInput', 'File'),
            ]
            service_elem = make_choose(component.parameters, 'WFFileStorageService', 'iCloud Drive')
            picker_elem = make_toggle(component.parameters, 'WFAskWhereToSave', True)
            line_elems = [
                {**{'label':'Service'},**service_elem},
                {**{'label':'Ask Where to Save'},**picker_elem},
            ]
            if 'off' in picker_elem['class']:
                if 'iCloud Drive' == service_elem['value']:
                    dest_elem = make_specify(component.parameters, 'WFFileDestinationPath', 'Text',align_left=True)
                    dest_elem['value'] = '/Shortcuts/' + dest_elem['value']
                elif 'Dropbox' == service_elem['value']:
                    dest_elem = make_specify(component.parameters, 'WFFileDestinationPath', 'optional',align_left=True)
                line_elems += [
                    {**{'label':'Destination Path'},**dest_elem},
                    {**{'label':'Overwrite If File Exists'},**make_toggle(component.parameters, 'WFSaveFileOverwrite', False)},
                ]
        elif "file.getlink"== sub_name: 
            title_elem=[
                'Get link to',
                make_magic(component.parameters, 'WFFile', 'File'),
            ]
        elif "text.match.getgroup"== sub_name: 
            idx_elem = make_magic(component.parameters, 'WFGetGroupType', 'Group At Index', default_blank=False)
            title_elem=[
                'Get',
                idx_elem,
                'in',
                make_magic(component.parameters, 'matches', 'Matches'),
            ]
            if 'Group At Index' == idx_elem['value']:
                # NOTE: left blank -> 'Group Index', not specified -> '1'. My code does not account for this, but it is more likely that a shared shortcut would be trying to get the first element, as blank -> error
                title_elem.insert(2, make_magic(component.parameters, 'WFGroupIndex', '1',default_blank=False,ask_text='Group Index'))
        elif "text.match"== sub_name: 
            title_elem=[
                'Match',
                make_magic(component.parameters, 'WFMatchTextPattern', 'Pattern'),
                'in',
                make_magic(component.parameters, 'text', 'Text'),
            ]
            line_elems = [{**{'label':'Case Sensitive'},**make_toggle(component.parameters,'WFMatchTextCaseSensitive',True)}]
        elif "text.changecase"== sub_name: 
            title_elem=[
                'Change',
                make_magic(component.parameters, 'text', 'Text'),
                'to',
                make_magic(component.parameters, 'WFCaseType', 'UPPERCASE',default_blank=False,ask_text = 'Case'),
            ]
        elif "correctspelling"== sub_name: 
            title_elem=[
                'Correct spelling of',
                make_magic(component.parameters, 'text', 'Text'),
            ]
        elif "gettypeaction"== sub_name: 
            title_elem = [
                'Get file of type',
                make_magic(component.parameters, 'WFFileType', 'UTI'),
                'from',
                make_magic(component.parameters, 'WFInput', 'Input'),
            ]
        elif "getrichtextfromhtml"== sub_name: 
            title_elem=[
                'Make rich text from',
                make_magic(component.parameters, 'WFHTML', 'HTML'),
            ]
        elif "gethtmlfromrichtext"== sub_name: 
            title_elem=[
                'Make HTML from',
                make_magic(component.parameters, 'WFInput', 'Rich Text'),
            ]
            line_elems = [{**{'label':'Make Full Document'},**make_toggle(component.parameters, 'WFMakeFullDocument', False)}]
        elif "handoffplayback"== sub_name: 
            title_elem = [
                'Hand off playback from',
                make_magic(component.parameters, 'WFSourceMediaRoute', 'Source', ask_text = 'Source'),
                'to',
                make_magic(component.parameters, 'WFDestinationMediaRoute', 'Destination', ask_text= 'Destination'),
            ]
        elif "getmarkdownfromrichtext"== sub_name: 
            title_elem = [
                'Make Markdown from',
                make_magic(component.parameters, 'WFInput', 'Rich Text'),
            ]
        elif "runextension"== sub_name: 
            title_elem=[]
        elif "postonfacebook"== sub_name: 
            title_elem=[]
        elif "tumblr.post"== sub_name: 
            title_elem=[]
        elif "tweet"== sub_name: 
            title_elem=[]
        elif "wordpress.post"== sub_name: 
            title_elem=[]
        elif "cloudapp.upload"== sub_name: 
            title_elem=[]
        else:
            impl = False
    elif editorial_re.fullmatch(component.name):
        sub_name = editorial_re.fullmatch(component.name)[1]
        if 'editscript' == sub_name:
            impl = False
        elif 'runscript' == sub_name:
            impl = False
        else:
            impl = False
    elif tally_re.fullmatch(component.name):
        sub_name = tally_re.fullmatch(component.name)[1]
        if 'get' == sub_name:
            impl = False
        elif 'updatetally' == sub_name:
            impl = False
        else:
            impl = False
    elif accessibility_re.fullmatch(component.name):
        sub_name = accessibility_re.fullmatch(component.name)[1]
        if sub_name in accessibility_toggles:
            turn_elem = make_magic(component.parameters, 'operation', 'Turn', default_blank=False, ask_text='Operation')
            turn_elem['value'] = turn_elem['value'].title()
            setting = accessibility_toggles[sub_name]
            title_elem = [
                turn_elem,
                setting,
            ]
            if turn_elem['value'] == 'Turn':
                if sub_name in [
                    'AXToggleAudioDescriptionsIntent',
                    'AXToggleAssistiveTouchIntent',
                    'AXToggleCaptionsIntent',
                    'AXToggleContrastIntent',
                    'AXToggleLEDFlashIntent',
                    'AXToggleMonoAudioIntent',
                    'AXToggleTransparencyIntent',
                    'AXToggleSmartInvertIntent',
                    'AXToggleVoiceControlIntent',
                    'AXToggleVoiceOverIntent',
                    'AXToggleWhitePointIntent',
                    'AXToggleZoomIntent',
                    'AXToggleSwitchControlIntent',
                ]: on_elem = make_magic(component.parameters, 'state', 1, ask_text='State', default_blank=False)
                elif sub_name in [
                    'AXToggleClassicInvertIntent',
                    'AXToggleReduceMotionIntent',
                ]: on_elem = make_magic(component.parameters, 'state', 0, ask_text='State', default_blank=False)
                else: on_elem = make_magic(component.parameters, 'state', 1, ask_text='State') # if you see a blank, it means something is unhandled
                
                on_elem['value'] = {1:'on',0:'off'}.get(on_elem['value'],on_elem['value'])
                title_elem += [on_elem]
        elif 'AXSetLargeTextIntent' == sub_name:
            title_elem = [
                'Set text size to',
                make_magic(component.parameters, 'textSize', 'extra small', default_blank=False, ask_text='Text Size'),
            ]
            try:
                title_elem[1]['value'] = re.sub('Extra','extra ',title_elem[1]['value'])
                title_elem[1]['value'] = re.sub('AX','accessibility ',title_elem[1]['value'])
                if title_elem[1]['value'] != 'Text Size':
                    title_elem[1]['value'] = title_elem[1]['value'].lower()
            except: pass
        else:
            impl = False
    elif clock_re.fullmatch(component.name):
        sub_name = clock_re.fullmatch(component.name)[1]
        if 'MTCreateAlarmIntent' == sub_name:
            title_elem = [
                'Create an alarm for',
                make_magic(component.parameters, 'dateComponents', 'Time'),
                'called',
                make_magic(component.parameters, 'label', 'Alarm'),
            ]
            repeats = component.parameters.get('repeatSchedule',[])
            if isinstance(repeats, dict):
                line_elems = [{**{'label':'Repeat'},**make_specify(component.parameters, 'repeatSchedule', 'Never')}]
            else: # parse list of magic vars
                repeat_line = ', '.join([i['displayString'] for i in repeats])
                line_elems = [{**{'label':'Repeat'},**{'class':'choose-var','value':repeat_line}}]
        elif 'MTToggleAlarmIntent' == sub_name:
            turn_elem = make_magic(component.parameters, 'operation', 'Turn')
            turn_elem['value'] = turn_elem['value'].title()
            state_elem = ''
            try:
                alarm_elem = magic(component.parameters['alarm']['displayString'])
            except KeyError:
                alarm_elem = magic('Alarm',True)
            if turn_elem['value'] == 'Turn':
                state_elem = make_magic(component.parameters, 'state', 'on', ask_text='State')
            title_elem = [turn_elem,'alarm \"',alarm_elem,'\"',state_elem,]
        else:
            impl = False
    elif remote_re.fullmatch(component.name):
        sub_name = remote_re.fullmatch(component.name)[1]
        tv_elem = make_magic(component.parameters, 'device', 'Apple TV')
        if 'LaunchApplicationIntent' == sub_name:
            if 'empty' not in tv_elem['class']:
                try:
                    app_elem = magic(component.parameters['application']['displayString'])
                except KeyError:
                    app_elem = magic('TV')
                title_elem = ['Open',app_elem,'on']
            else:
                title_elem = ['Open App on']
            title_elem += [tv_elem]
        elif 'PauseContentIntent' == sub_name:
            title_elem = [
                make_magic(component.parameters, 'mediaCommand', 'Play/Pause',default_blank=False,ask_text='Media Command'),
                tv_elem,
            ]
        elif 'LaunchRemoteIntent' == sub_name:
            title_elem = ['Show remote control for',tv_elem]
        elif 'SleepAppleTVIntent' == sub_name:
            title_elem = ['Sleep',tv_elem]
        elif 'WakeAppleTVIntent' == sub_name:
            title_elem = ['Wake',tv_elem]
        else:
            impl = False
        # custom 'Ask Each Time'
        for elem in [i for i in title_elem if isinstance(i,dict)]:
            if 'Ask Each Time' == elem.get('value',''): elem['value'] = 'Apple TV'
    elif bear_re.fullmatch(component.name):
        sub_name = bear_re.fullmatch(component.name)[1]
        if 'add' == sub_name:
            title_elem = ['Add to Bear Note']
            line_elems = [
                {**{'label':'Attach'},**make_pill(component.parameters,'BearAttachmentType',['Text','File'],'Text')},
                {**{'label':'Mode'},**make_pill(component.parameters,'BearMode',['Append','Prepend'],'Append')},
                {**{'label':'Title'},**make_specify(component.parameters,'BearTitle','optional')},
                {**{'label':'Note Identifier'},**make_specify(component.parameters,'BearIdentifier','7A544B90-3B94-4...')},
                {**{'label':'Return to Shortcuts'},**make_toggle(component.parameters,'BearReturn',True)},
            ]
            result = 'Bear Note'
        elif 'create' == sub_name:
            title_elem = [
                'Create',
                make_magic(component.parameters, 'BearTitle', 'Note Title'),
                'with',
                make_magic(component.parameters, 'BearNoteInput', 'Content'),
            ]
            line_elems = [
                {**{'label':'Tags'},**make_specify(component.parameters, 'BearTags', 'cats, dogs')},
                {**{'label':'Return to Shortcuts'},**make_toggle(component.parameters,'BearReturn',True)},
            ]
            result = 'Bear Note from URL'
        elif 'grab' == sub_name:
            title_elem = [
                'Create note from',
                make_magic(component.parameters, 'BearURL', 'URL'),
            ]
            line_elems = [
                {**{'label':'Tags'},**make_specify(component.parameters, 'BearTags', 'cats, dogs')},
                {**{'label':'Include Images'},**make_toggle(component.parameters,'BearImages',True)},
                {**{'label':'Return to Shortcuts'},**make_toggle(component.parameters,'BearReturn',True)},
            ]
        elif 'contents' == sub_name:
            title_elem = [
                'Get contents of',
                make_magic(component.parameters, 'BearIdentifier', 'Note Title'),
            ]
            line_elems = [{**{'label':'Note Identifier'},**make_specify(component.parameters,'BearIdentifier','7A544B90-3B94-4...')}]
            result = 'Contents of Bear Note'
        elif 'open' == sub_name:
            title_elem = [
                'Open',
                make_magic(component.parameters, 'BearTitle', 'Note Title'),
            ]
            line_elems = [{**{'label':'Note Identifier'},**make_specify(component.parameters,'BearIdentifier','7A544B90-3B94-4...')}]
        elif 'search' == sub_name:
            title_elem = [
                'Search for',
                make_magic(component.parameters, 'BearTerm', 'grape'),
            ]
            line_elems = [{**{'label':'Tag'},**make_specify(component.parameters, 'BearTag', 'optional')}]
        else:
            impl = False
    elif 'com.apple.mobileslideshow.StreamShareService' == component.name:
        title_elem = [
            'Post',
            make_magic(component.parameters, 'ImageInput', 'Images'),
            'to Shared Album',
        ]
    elif 'com.apple.mobilenotes.SharingExtension' == component.name:
        title_elem = [
            'Create note with',
            make_magic(component.parameters, 'WFCreateNoteInput', 'Body'),
        ]
        line_elems = [{**{'label':'Show Compose Sheet'},**make_toggle(component.parameters, 'ShowWhenRun',True)}]
        if component.parameters.get('ShowWhenRun',None) == False:
            title_elem += [
                'in',
                make_magic(component.parameters, 'WFNoteGroup', 'Folder',ask_text='Folder'),
            ]
    elif 'com.apple.mobilephone.call' == component.name:
        title_elem = [
            'Call',
            #vcard handling 'WFCallContact'
            magic('<contacts>'),
        ]
    elif 'com.apple.iBooks.openin' == component.name:
        title_elem = [
            'Add',
            make_magic(component.parameters, 'BooksInput', 'File'),
            'to Books',
        ]
    elif 'com.apple.Numbers.TNiOSAddValueIntent' == component.name:
        title_elem = ['Add to',make_magic(component.parameters, 'file', 'Spreadsheet'),]
        values = component.parameters.get('values',{})
        value_elem = {}
        if isinstance(values, dict):
            value_elem = make_magic(component.parameters, 'values', 'Values')
        else: # parse list of magic vars
            value_elem = [make_magic({'elem':i},'elem','Values') for i in repeats]
        line_elems = [
            {**{'label':'Values'},**value_elem},
            {**{'label':'Position'},**make_pill(component.parameters,'position',['Above','Below'],'Below')},
            {**{'label':'Sheet name'},**make_specify(component.parameters, 'sheetName', 'Text'),},
            {**{'label':'Table name'},**make_specify(component.parameters, 'tableName', 'Text'),},
        ]
    elif 'com.apple.Numbers.TNiOSOpenAnyDocumentIntent' == component.name:
        title_elem = ['Open',make_magic(component.parameters, 'file', 'Spreadsheet'),]
    elif 'com.burbn.instagram.openin' == component.name:
        title_elem = ['Post',make_magic(component.parameters, 'InstagramInput', 'Photo'),]
        line_elems = [{**{'label':'Caption'},**make_specify(component.parameters, 'InstagramCaption', 'optional',align_left=True)}]
    elif 'dk.simonbs.Jayson.GetFileIntent' == component.name:
        title_elem = [
            'Get',
            make_magic(component.parameters, 'filename', 'Filename'),
            'from',
            make_magic(component.parameters, 'folder', 'iCloud',default_blank=False),
        ]
    elif 'dk.simonbs.Jayson.ViewJSONIntent' == component.name:
        title_elem = [
            'View',
            make_magic(component.parameters, 'files', 'Text'),
            'in',
            make_magic(component.parameters, 'viewDestination', 'app',default_blank=False),
        ]
        line_elems = [
            {**{'label':'Filename'},**make_specify(component.parameters, 'filename', 'Text')},
            {**{'label':'Save'},**make_pill(component.parameters,'saveDestination',['Don\'t Save','Local','iCloud'],'Don\'t Save')},
        ]
    else:
        impl = False
        sub_name = ''

    # turn strings -> dict for the Django templater:
    title_elem = [({'class': '', 'value': i, } if isinstance(i, str) else i) for i in title_elem]
    # silence to restore inline elems, the styling for which is very hard
    title_elem = flatten(title_elem)
    title_elem = [i for i in title_elem if i['value']]
    # © Processing:
    if not options_impl:
        line_elems += [not_implemented_options()]
    
    if not impl:
        action_dct = not_implemented_action(category, indent_level, sub_name, glyph)
    else:
        action_dct = {
            'title': title_elem,
            'line': line_elems,
            'glyph': f'assets/cat/{glyph}',
            'category': category,
            'indent': f'indent{indent_level}' if indent_level else '',
            'special':special,
            'lines':line_elems,
            'list_items':list_items,
            'dct':dict_items,
            'UUID':component.UUID,
            'result':result,
        }
    return action_dct, indent

def control_flow(parameters: dict) -> (str, str, int):
    UUID = parameters.get('UUID', None)
    group = parameters.get('GroupingIdentifier')
    mode = parameters.get('WFControlFlowMode')
    return (UUID, group, mode)

def conditional(component: action) -> list:
    (UUID, group, mode) = control_flow(component.parameters)
    condition = component.parameters.get('WFCondition', None)
    input_elem = make_magic(component.parameters, 'WFInput', 'Input')
    title_elem = []

    # condensed check for 'Current Date' / 'Clipboard' Magic Var
    try:
        var_type = component.parameters['WFInput']['Type']
    except KeyError:
        var_type = None

    if None == condition:
        title_elem = [
            'If',
            input_elem,
            magic('Condition', True),
        ]
    elif condition in [0, 2]:
        if 'CurrentDate' == var_type:
            condition_elem = magic('is after' if condition == 0 else 'is before')
            test_elem = make_magic(component.parameters, 'WFDate', 'Date')
        elif 'WFNumberValue' in component.parameters:  # can't detect number?
            condition_elem = magic(
                'is less than' if condition == 0 else 'is greater than')
            test_elem = make_magic(component.parameters, 'WFNumberValue', 'Number')
        else:  # catch all
            condition_elem = magic('is less than' if condition == 0 else 'is greater than')
            test_val = component.parameters.get('WFDate', component.parameters.get('WFConditionalActionString', component.parameters.get('Number', None)))
            test_elem = magic(test_val) if test_val else magic('Value', True)
        title_elem = [
            'If',
            input_elem,
            condition_elem,
            test_elem,
        ]
    elif condition in [1, 3]:
        title_elem = [
            'If',
            input_elem,
            magic('is greater than or equal to' if condition == 3 else 'is less than or equal to'),
            make_magic(component.parameters, 'WFNumberValue', 'Number'),
        ]
    elif condition in [4, 5]:
        if 'CurrentDate' == var_type:
            condition_elem = magic(
                'is exactly' if condition == 4 else 'is not exactly')
            test_elem = make_magic(component.parameters, 'WFDate', 'Date')
        elif 'Clipboard' == var_type:
            condition_elem = magic('is' if condition == 4 else 'is not')
            test_elem = make_magic(component.parameters, 'WFConditionalActionString', 'Text')
        # can't detect number?
        elif 'WFNumberValue' in component.parameters:
            condition_elem = magic('is' if condition == 4 else 'is not')
            test_elem = make_magic(component.parameters, 'WFNumberValue', 'Number')
        else:  # catch all
            condition_elem = magic('is' if condition == 4 else 'is not')
            test_val = component.parameters.get('WFDate', component.parameters.get('WFConditionalActionString', component.parameters.get('Number', None)))
            test_elem = magic(test_val) if test_val else magic('Value', True)
        title_elem = [
            'If',
            input_elem,
            condition_elem,
            test_elem,
        ]
    elif condition in [8, 9]:
        title_elem = [
            'If',
            input_elem,
            magic('begins with' if condition == 8 else 'ends with'),
            make_magic(component.parameters, 'WFConditionalActionString', 'Text'),
        ]
    elif condition in [99, 999]:
        title_elem = [
            'If',
            input_elem,
            magic('contains' if condition == 99 else 'does not contain'),
            make_magic(component.parameters, 'WFConditionalActionString', 'Text'),
        ]
    elif condition in [100, 101]:
        title_elem = [
            'If',
            input_elem,
            magic('has any value' if condition ==
                  100 else 'does not have any value'),
        ]
    elif condition in [1000, 1001]:
        title_elem = [
            'If',
            input_elem,
            magic('is in the next' if condition == 1000 else 'is in the last'),
            make_magic(component.parameters, 'WFDuration', 'Number', False, 'Magnitude'),
            # no blank, 'minutes' is chosen by default
            make_magic(component.parameters, 'WFDuration','unit', False, 'Unit')
        ]
    elif 1002 == condition:
        title_elem = [
            'If',
            input_elem,
            magic('is today'),
        ]
    elif 1003 == condition:
        if 'WFDate' in component.parameters and 'WFAnotherDate' in component.parameters:
            test_elem_1 = make_magic(component.parameters, 'WFDate', 'Date')
            test_elem_2 = make_magic(
                component.parameters, 'WFAnotherDate', 'Date')
        elif 'WFNumberValue' in component.parameters and 'WFAnotherNumber' in component.parameters:
            test_elem_1 = make_magic(
                component.parameters, 'WFNumberValue', 'Date')
            test_elem_2 = make_magic(
                component.parameters, 'WFAnotherNumber', 'Date')
        else:  # catch all
            test_elem_1 = magic('Value', True)
            test_elem_2 = magic('Value', True)
        title_elem = [
            'If',
            input_elem,
            magic('is between'),
            test_elem_1,
            'and',
            test_elem_2,
        ]
    else:
        title_elem = [
            'If',
            input_elem,
            magic('Condition', True),
        ]
    return title_elem

# flattens nested lists
def flatten(title_elem:list)->list:
    title_flat = []
    [title_flat.extend(i['value'] if isinstance(i['value'],list) else [i]) for i in title_elem]
    return title_flat