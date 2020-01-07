## Dependency: sys
import re, logging

## Dependency: local
from share.process.sc_action.categories import (
    scripting, 
    filters, 
    maths, 
    date, 
    music, 
    maps, 
    documents, 
    text, 
    location, 
    accessibility, 
    safari, 
    misc,
)
from .action import action
from ..lookups.placeholder import *

lookup = {
'is.workflow.actions.':{
    'filter.':{
        'articles':NOT_IMPLEMENTED_ACTION,
    },
    'properties.':{
        'trello':NOT_IMPLEMENTED_ACTION,
    },
    
    # detect
    'detect.':{
        'dictionary':scripting.detect_dictionary,
        'number':scripting.detect_number,
        'date':date.detect_date,
    },
    
    # format
    'format.':{
        'filesize':maths.format_filesize,
        'number':maths.format_number,
        'date':date.format_date,
    },

    # SCRIPTING
    'openapp':scripting.openapp,
    'exit':scripting.exit_,
    'conditional':scripting.conditional,
    'choosefrommenu':scripting.choosefrommenu,
    'repeat.count':scripting.repeat_count,
    'repeat.each':scripting.repeat_each,
    'delay':scripting.delay,
    'waittoreturn':scripting.waittoreturn,
    'getbatterylevel':scripting.getbatterylevel,
    'getdevicedetails':scripting.getdevicedetails,
    'setbrightness':scripting.setbrightness,
    'flashlight':scripting.flashlight,
    'getvalueforkey':scripting.getvalueforkey,
    'dictionary':scripting.dictionary,
    'setvalueforkey':scripting.setvalueforkey,
    'gettypeaction':scripting.gettypeaction,
    'getitemtype':scripting.getitemtype,
    'getitemname':scripting.getitemname,
    'setitemname':scripting.setitemname,
    'base64encode':scripting.base64encode,
    'hash':scripting.hash_,
    'count':scripting.count,
    'choosefromlist':scripting.choosefromlist,
    'getitemfromlist':scripting.getitemfromlist,
    'list':scripting.list_,
    'getipaddress':scripting.getipaddress,
    'getwifi':scripting.getwifi,
    'dnd.set':scripting.dnd_set,
    'airplanemode.set':scripting.airplanemode_set,
    'bluetooth.set':scripting.bluetooth_set,
    'cellulardata.set':scripting.cellulardata_set,
    'lowpowermode.set':scripting.lowpowermode_set,
    'wifi.set':scripting.wifi_set,
    'nothing':scripting.nothing,
    'ask':scripting.ask,
    'playsound':scripting.playsound,
    'alert':scripting.alert,
    'showresult':scripting.showresult,
    'vibrate':scripting.vibrate,
    'runsshscript':scripting.runsshscript,
    'openxcallbackurl':scripting.openxcallbackurl,
    'urlencode':scripting.urlencode,
    'handoff':scripting.handoff,
    'viewresult':scripting.viewresult,

    # MATHS
    'math':maths.math,
    'statistics':maths.statistics,
    'round':maths.round_,
    'measurement.':{
        'convert':maths.measurement_convert,
        'create':maths.measurement_create,
    },
    'number':{
        '.random':maths.random,
        '':maths.number_,
    },

    # DATE
    'date':date.date,
    'adjustdate':date.adjustdate,
    'gettimebetweendates':date.gettimebetweendates,
    
    # MUSIC
    'getcurrentsong':music.getcurrentsong,
    'playmusic':music.playmusic,
    'pausemusic':music.pausemusic,
    'skipback':music.skipback,
    'skipforward':music.skipforward,
    'exportsong':music.exportsong,
    'addtoplaylist':music.addtoplaylist,
    'createplaylist':music.createplaylist,
    'get.playlist':music.get_playlist,
    'addmusictoupnext':music.addmusictoupnext,
    'clearupnext':music.clearupnext,

    # MAPS
    'getdistance':maps.getdistance,
    'gethalfwaypoint':maps.gethalfwaypoint,
    'gettraveltime':maps.gettraveltime,
    'address':maps.address,
    'getmapslink':maps.getmapslink,
    'getdirections':maps.getdirections,
    'searchmaps':maps.searchmaps,
    'searchlocalbusinesses':maps.searchlocalbusinesses,

    # DOCUMENTS
    'unzip':documents.unzip,
    'makezip':documents.makezip,
    'speaktext':documents.speaktext,
    'avairyeditphoto':documents.avairyeditphoto,
    'openin':documents.openin,
    'previewdocument':documents.previewdocument,
    'makepdf':documents.makepdf,
    'print':documents.print_,
    'generatebarcode':documents.generatebarcode,
    'scanbarcode':documents.scanbarcode,
    'getrichtextfrommarkdown':documents.getrichtextfrommarkdown,
    'getrichtextfromhtml':documents.getrichtextfromhtml,
    'gethtmlfromrichtext':documents.gethtmlfromrichtext,
    'getmarkdownfromrichtext':documents.getmarkdownfromrichtext,
    'dictatetext':documents.dictatetext,
    'getnameofemoji':documents.getnameofemoji,
    'showdefinition':documents.showdefinition,
    'correctspelling':documents.correctspelling,
    'file.':{
        'createfolder':documents.file_createfolder,
        'append':documents.file_append,
        'delete':documents.file_delete,
        'getlink':documents.file_getlink,
    },
    'documentpicker.':{
        'open':documents.documentpicker_open,
        'save':documents.documentpicker_save,
    },

    # TEXT
    'gettext':text.gettext,
    'text.':{
        'replace':text.text_replace,
        'combine':text.text_combine,
        'split':text.text_split,
        'changecase':text.text_changecase,
        'match':{
            '':text.text_match,
            '.getgroup':text.text_match_getgroup,
        },
        'translate':misc.text_translate,
    },

    # LOCATION
    'getcurrentlocation':location.getcurrentlocation,
    'location':location.location,
    'weather.':{
        'currentconditions':location.weather_currentconditions,
        'forecast':location.weather_forecast,
    },

    # SAFARI
    'searchweb':safari.searchweb,
    'showwebpage':safari.showwebpage,
    'readinglist':safari.readinglist,
    'openurl':safari.openurl,
    'runjavascriptonwebpage':safari.runjavascriptonwebpage,
    'getwebpagecontents':safari.getwebpagecontents,
    'getarticle':safari.getarticle,

    # MISC
    'encodemedia':misc.encodemedia,
    'trimvideo':misc.trimvideo,
    'detectlanguage':misc.detectlanguage,
    'airdropdocument':misc.airdropdocument,
    '___':misc.___,
    '___':misc.___,
    '___':misc.___,
    '___':misc.___,
    '___':misc.___,
    '___':misc.___,
    '___':misc.___,
},
'com.apple.AccessibilityUtilities.AXSettingsShortcuts.':{
    'AXToggleSwitchControlIntent':accessibility.AXToggleSwitchControlIntent,
    'AXToggleLEDFlashIntent':accessibility.AXToggleLEDFlashIntent,
    'AXToggleAssistiveTouchIntent':accessibility.AXToggleAssistiveTouchIntent,
    'AXToggleAudioDescriptionsIntent':accessibility.AXToggleAudioDescriptionsIntent,
    'AXToggleClassicInvertIntent':accessibility.AXToggleClassicInvertIntent,
    'AXToggleSmartInvertIntent':accessibility.AXToggleSmartInvertIntent,
    'AXToggleCaptionsIntent':accessibility.AXToggleCaptionsIntent,
    'AXToggleContrastIntent':accessibility.AXToggleContrastIntent,
    'AXToggleMonoAudioIntent':accessibility.AXToggleMonoAudioIntent,
    'AXToggleReduceMotionIntent':accessibility.AXToggleReduceMotionIntent,
    'AXToggleTransparencyIntent':accessibility.AXToggleTransparencyIntent,
    'AXToggleVoiceControlIntent':accessibility.AXToggleVoiceControlIntent,
    'AXToggleVoiceOverIntent':accessibility.AXToggleVoiceOverIntent,
    'AXToggleWhitePointIntent':accessibility.AXToggleWhitePointIntent,
    'AXToggleZoomIntent':accessibility.AXToggleZoomIntent,
    'AXSetLargeTextIntent':accessibility.AXSetLargeTextIntent,
    'AXStartMagnifierIntent':accessibility.AXStartMagnifierIntent,
    'AXStartGuidedAccessIntent':accessibility.AXStartGuidedAccessIntent,
    'AXStartSpeakScreenIntent':accessibility.AXStartSpeakScreenIntent,
}
}

def categorize_action(name:str):
    sc_action = find_branch(name, lookup)
    if sc_action:
        return sc_action
    return NOT_IMPLEMENTED_ACTION

def find_branch(name:str, tree:dict):
    for k,v in tree.items():
        k = re.escape(k)
        if re.findall(f'^{k}', name):
            if isinstance(v, dict):
                return find_branch(re.sub(k,'',name), v)
            else:
                return v