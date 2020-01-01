dct = {
    
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