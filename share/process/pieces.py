from .lookups import color, wf_icons, languages, simple_actions, placeholder, extensions, action_meta, template_actions

# lookup dictionaries
color_codes = color.codes
icon_codes = wf_icons.codes
lang_codes = languages.dct
extension_lookup = extensions.dct
categorize = action_meta.dct

# information to fill in the blanks for simple repeated actions
uni_params       = simple_actions.uni_params
toggle_params    = simple_actions.toggle_params
no_params        = simple_actions.no_params

property_actions = template_actions.property_actions
filter_actions   = template_actions.filter_actions

# placeholders
infoless                = placeholder.infoless
error_action            = placeholder.error_action
not_implemented_action  = placeholder.not_implemented_action
not_implemented_options = placeholder.not_implemented_options

field_type = {
    'Album':'',
    'Width':'number',
    'Height':'number',
    'Date Taken':'',
    'Time Taken':'',
    'Media Type':'',
    'Photo Type':'',
    'Duration':'duration',
    'Frame Rate':'number',
    'Orientation':'',
    'Is a Screenshot':'bool',
    'Is Hidden':'bool',
    'Is Favorite':'bool',
    'Name':'string',
    'File Size':'size',
    'File Extension':'string',
    'Creation Date':'date',
    'Last Modified Date':'date',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',
    '':'',

}

app_categorize = {
    'dk.simonbs.Jayson':{
        'glyph':'others/Jayson.png',
        'category':'JAYSON',
        'name':'Jayson',
    },
    'com.apple.Numbers':{
        'glyph':'system/Numbers.png',
        'category':'NUMBERS',
        'name':'clock?',
    },
    'com.apple.mobiletimer-framework.MobileTimerIntents':{
        'glyph':'system/Clock.png',
        'category':'CLOCK',
        'name':'clock?',
    },
    'com.apple.TVRemoteUIService':{
        'glyph':'system/Remote.png',
        'category':'APPLE TV REMOTE',
        'name':'Remote?',
    },
    'net.shinyfrog.bear-IOS':{
        "glyph": "others/Bear.png",
        "category": "BEAR",
        'name':'Bear',
    },
    'net.shinyfrog.bear-iOS':{
        "glyph": "others/Bear.png",
        "category": "BEAR",
        'name':'Bear',
    },
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts': {
        "glyph": "system/Settings.png",
        "category": "SETTINGS",
        'name':'Settings?',
    },
    'fm.overcast.overcast': {
        "glyph": "others/Overcast.png",
        "category": "OVERCAST",
        'name':'Overcast',
    },
    'com.burbn.instagram':{
        "glyph": "others/Instagram.png",
        "category": "Instagram",
        'name':'Instagram',
    },
}


# I gave up on these. in principle, current date *should* cause 4 & 5 to adopt a different keyword
# see if anyone complains about it
date_conditions = {
    4:'is exactly',
    5:'is not exactly',
}
text_conditions = {
    4:'is',
    5:'is not',
}

app_lookup = {
    'com.FormaGrid.Hyperbase':'Airtable',
}

time_codes = {
    'sec':'second',
    'min':'minute',
    'hr':'hour',
}