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
    
    # "Enumeration"
    # album can be string or enum, depending on music / photo
    'Orientation':'enum',
    'Media Type':'enum',
    'Media Kind':'enum',
    'Photo Type':'enum',
    'Folder':'enum',
    'Priority':'enum',
    'Type':'enum', # NOTE: similar to album, this might refer to many other things. Here, it specifically references health samples
    'Status':'enum',
    'Role':'enum',
    'Calendar':'enum', # calendar events
    'List':'enum', # reminders
    '':'enum',
    
    # number
    'Frame Rate':'number',
    'Width':'number',
    'Height':'number',
    'Altitude':'number',
    'Play Count':'number',
    'Album Track #':'number',
    'Disc #':'number',
    'Skip Count':'number',
    'Rating':'number',
    'Number of Words':'number',
    '':'number',
    
    # boolean
    'Is a Screenshot':'bool',
    'Is Hidden':'bool',
    'Is Favorite':'bool',
    'Is Explicit':'bool',
    'Is Cloud Item':'bool',
    'Has Album Artwork':'bool',
    'Has Photo':'bool',
    'Is Me':'bool',
    'Is All Day':'bool',
    'Is Completed':'bool',
    'Has Alarms':'bool',
    '':'bool',
    
    # contact
    'Phone Number':'phone', # technically not a string, offers only [0-9] and *+#
    'Email Address':'email',

    # string
    'Name':'string',
    'File Extension':'string',
    'Title':'string',
    'Author':'string',
    'Excerpt':'string',
    'URL':'string',
    'Body':'string',
    'City':'string',
    'Latitude':'string',
    'Longitude':'string',
    'State':'string',
    'ZIP Code':'string',
    'Country':'string',
    'Main Image URL':'string', # URLs stored as strings
    'Value':'string',
    'First Name':'string',
    'Middle Name':'string',
    'Last Name':'string',
    'Street Address':'string',
    'Prefix':'string',
    'Suffix':'string',
    'Nickname':'string',
    'Phonetic First Name':'string',
    'Phonetic Last Name':'string',
    'Phonetic Middle Name':'string',
    'Job Title':'string',
    'Company':'string',
    'Department':'string',
    'Notes':'string',
    'Album':'string',
    'Artist':'string',
    'Album Artist':'string',
    'Genre':'string',
    'Composer':'string',
    'Lyrics':'string',
    'Comments':'string',
    'Location':'string',
    '':'string',
    
    # size (number + unit)
    'File Size':'size',
    'Duration':'duration',
    
    # date
    'Creation Date':'date',
    'Last Modified Date':'date',
    'Release Date':'date',
    'Last Played Date':'date',
    'Published Date':'date',
    'Start Date':'date',
    'End Date':'date',
    'Birthday':'date',
    'Date Taken':'date', # NOTE: should omit time, this is inaccurate
    'Time Taken':'date', # NOTE: should omit date, this is inaccurate
    'Due Date':'date',
    'Completion Date':'date',
    '':'date',
    
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