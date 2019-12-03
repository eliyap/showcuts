property_actions = {
    'trello':{
        'name':'Trello item',
    },
    'files':{
        'name':'File',
    },
    'itunesstore':{
        'name':'iTunes product',
    },
    'itunesartist':{
        'name':'iTunes artist',
    },
    'podcast':{
        'name':'Podcast episode',
    },
    'appstore':{
        'name':'App Store app',
    },
    'images':{
        'name':'Image',
    },
    'ulysses.sheet':{
        'name':'Ulysses sheet',
    },
    'music':{
        'default':'Artist',
        'name':'Music',
    },
    'podcastshow':{
        'name':'Podcast',
    },
    'weather.conditions':{
        'name':'Weather Conditions',
    },
    'locations':{
        'name':'Location',
    },
    'eventattendees':{
        'name':'Event Attendee',
    },
    'calendarevents':{
        'name':'Calendar Event',
    },
    'reminders':{
        'default':'List',
        'name':'Reminder',
    },
    'health.quantity':{
        'name':'Health Sample',
    },
    'contacts':{
        'name':'Contact',
    },
    'articles':{
        'name':'Article',
    },
    'safariwebpage':{
        'name':'Safari web page',
    },
}

filter_actions = {
    'locations':{
        'default':'Locations',
        'default_blank':True,
        'title':'Filter',
    },
    'eventattendees':{
        'default':'Event Attendees',
        'default_blank':True,
        'title':'Filter',
    },
    'calendarevents':{
        'default':'All Calendar Events',
        'default_blank':False,
        'title':'Find',
    },
    'reminders':{
        'default':'All Reminders',
        'default_blank':False,
        'title':'Find',
    },
    'images':{
        'default':'Images',
        'default_blank':True,
        'title':'Filter',
    },
    'music':{
        'default':'All Music',
        'default_blank':False,
        'title':'Find',
    },
    'photos':{
        'default':'All Photos',
        'default_blank':False,
        'title':'Find',
    },
    'files':{
        'default':'Files',
        'default_blank':True,
        'title':'Filter',
    },
    'notes':{
        'default':'All Notes',
        'default_blank':False,
        'title':'Find',
    },
    'articles':{
        'default':'Articles',
        'default_blank':True,
        'title':'Filter',
    },
    'contacts':{
        'default':'All Contacts',
        'default_blank':False,
        'title':'Find',
    },
    'health.quantity':{
        'default':'All Health Samples',
        'default_blank':False,
        'title':'Find',
    },
}

uni_params = {
    'getitemname':'Get name of', 
    'getitemtype':'Get type of',
    'viewresult':'Get Content Graph of',
    'detect.images':'Get images from',
    'detect.number':'Get numbers from',
    'detect.dictionary':'Get dictionary from',
    'detect.address':'Get addresses from',
    'detect.text':'Get text from',
    'detect.link':'Get URLs from',
    'detect.contacts':'Get contacts from',
    'detect.phonenumber':'Get phone numbers from',
    'print':'Print',
    'share':'Share',
}
toggle_params = {
    'airplanemode.set':'Turn Airplane Mode', 
    'bluetooth.set':'Turn Bluetooth',
    'cellulardata.set':'Turn Mobile Data', 
    'wifi.set':'Turn Wi-Fi',
    'lowpowermode.set':'Turn Low Power Mode',
}
no_params = { 
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartMagnifierIntent':'Open Magnifier',
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartGuidedAccessIntent':'Start Guided Access',
    'com.apple.AccessibilityUtilities.AXSettingsShortcuts.AXStartSpeakScreenIntent':'Start Speak Screen',
    'is.workflow.actions.selectphone':'Select Phone Number',
    'is.workflow.actions.getlatestphotoimport':'Get last import',
    'is.workflow.actions.clearupnext':'Clear Up Next',
    'is.workflow.actions.getcurrentsong':'Get current song',
    'is.workflow.actions.handoff':'Continue in Shortcuts app',
    'is.workflow.actions.waittoreturn':'Wait to return',
    'is.workflow.actions.getbatterylevel':'Get battery level',
    'is.workflow.actions.nothing':'Nothing',
    'is.workflow.actions.vibrate':'Vibrate device',# iphone only, or haptic watch boop
    'is.workflow.actions.getmyworkflows':'Get my shortcuts',
    'is.workflow.actions.getclipboard':'Get clipboard',
    'is.workflow.actions.getpodcastsfromlibrary':'Get Podcasts from Library',
    'com.apple.mobiletimer-framework.MobileTimerIntents.MTGetAlarmsIntent':'Get all alarms',
    'fm.overcast.overcast.add':'Add to Overcast',
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

categorize = {
    "is.workflow.actions.instapaper.add": {
        "glyph": "others/Instapaper.png",
        "category": "INSTAPAPER",
        "result":None,
    },
    "is.workflow.actions.properties.trello": {
        "glyph": "others/Trello.png",
        "category": "TRELLO",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.ulysses.sheet": {
        "glyph": "others/Ulysses.png",
        "category": "ULYSSES",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.instapaper.get": {
        "glyph": "others/Instapaper.png",
        "category": "INSTAPAPER",
        "result":'Instapaper Bookmarks',
    },
    "is.workflow.actions.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS",
        "result":'Contacts',
    },
    "is.workflow.actions.detect.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS",
        "result":'Contacts',
    },
    "is.workflow.actions.detect.phonenumber": {
        "glyph": "Phone.svg",
        "category": "CONTACTS",
        "result":'Phone Numbers',
    },
    "is.workflow.actions.phonenumber": {
        "glyph": "Phone.svg",
        "category": "PHONE NUMBER",
        "result":'Phone Number',
    },
    "is.workflow.actions.selectcontacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS",
        "result":'Contacts',
    },
    "is.workflow.actions.selectphone": {
        "glyph": "Phone.svg",
        "category": "CONTACTS",
        "result":'Phone Numbers',
    },
    "is.workflow.actions.timer.start": {
        "glyph": "system/Clock.png",
        "category": "CLOCK",
        'result':None,
    },
    "is.workflow.actions.addnewevent": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        'result':'New Event',
    },
    "is.workflow.actions.getupcomingevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        'result':'Upcoming Events',
    },
    "is.workflow.actions.removeevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        'result':None,
    },
    "is.workflow.actions.showincalendar": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        'result':None,
    },
    "com.apple.iBooks.openin": {
        "glyph": "system/Books.png",
        "category": "BOOKS",
        'result':None,
    },
    "is.workflow.actions.appendnote": {
        "glyph": "system/Notes.png",
        "category": "NOTES",
        'result':'Appended Note',
    },
    "is.workflow.actions.shownote": {
        "glyph": "system/Notes.png",
        "category": "NOTES",
        'result':None,
    },
    "com.apple.mobilephone.call": {
        "glyph": "system/Phone.png",
        "category": "PHONE",
        'result':None,
    },
    "is.workflow.actions.venmo.request": {
        "glyph": "system/applepay",
        "category": "WALLET",
        'result':None,
    },
    "is.workflow.actions.venmo.pay": {
        "glyph": "system/applepay",
        "category": "WALLET",
        'result':None,
    },
    "is.workflow.actions.filter.articles": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":"Articles",
    },
    "is.workflow.actions.filter.locations": {
        "glyph": "Location.svg",
        "category": "LOCATION",
        "result":"Locations",
    },
    "is.workflow.actions.filter.files": {
        "glyph": "File.svg",
        "category": "FILES",
        "result":"Files",
    },
    "is.workflow.actions.filter.photos": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        "result":"Photos",
    },
    "is.workflow.actions.filter.music": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        "result":"Music",
    },
    "is.workflow.actions.filter.images": {
        "glyph": "Image.svg",
        "category": "IMAGES",
        "result":"Images",
    },
    "is.workflow.actions.filter.eventattendees": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        "result":"Event Attendees",
    },
    "is.workflow.actions.filter.calendarevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        "result":"Calendar Events",
    },
    "is.workflow.actions.addnewreminder": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS",
        "result":"New Reminder",
    },
    "is.workflow.actions.getupcomingreminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS",
        "result":"Upcoming Reminders",
    },
    "is.workflow.actions.removereminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS",
        "result":None,
    },
    "is.workflow.actions.reminders.showlist": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS",
        "result":None,
    },
    "is.workflow.actions.filter.reminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS",
        "result":"Reminders",
    },
    "is.workflow.actions.filter.notes": {
        "glyph": "system/Notes.png",
        "category": "NOTES",
        "result":"Notes",
    },
    "is.workflow.actions.filter.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS",
        "result":"Contacts",
    },
    "is.workflow.actions.filter.health.quantity": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH",
        "result":"Health Samples",
    },
    "is.workflow.actions.health.workout.log": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH",
        'result':'Workout',
    },
    "is.workflow.actions.health.quantity.log": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH",
        'result':'Health Sample',
    },
    "is.workflow.actions.comment": {
        "glyph": "Note.svg",
        "category": "COMMENT",
        "result":None,
    },
    "is.workflow.actions.openapp": {
        "glyph": "App.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.choosefrommenu": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Menu Result",
    },
    "is.workflow.actions.handoff": {
        "glyph": "Handoff.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.exit": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.conditional": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"If Result",
    },
    "is.workflow.actions.repeat.count": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Repeat Results",
    },
    "is.workflow.actions.repeat.each": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Repeat Results",
    },
    "is.workflow.actions.delay": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.waittoreturn": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.getbatterylevel": {
        "glyph": "Battery.svg",
        "category": "SCRIPTING",
        "result":'Battery Level',
    },
    "is.workflow.actions.getdevicedetails": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Device Name",
    },
    "is.workflow.actions.appearance": {
        "glyph": "Brightness.svg",
        "category": "APPEARANCE",
        "result":None,
    },
    "is.workflow.actions.setbrightness": {
        "glyph": "Brightness.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.dnd.set": {
        "glyph": "DND.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.flashlight": {
        "glyph": "Flashlight.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.lowpowermode.set": {
        "glyph": "Battery.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.setplaybackdestination": {
        "glyph": "AirplayAudio.svg",
        "category": "AIRPLAY",
        "result":None,
    },
    "is.workflow.actions.setvolume": {
        "glyph": "Volume.svg",
        "category": "MEDIA",
        "result":None,
    },
    "is.workflow.actions.dictionary": {
        "glyph": "Settings.svg",
        "category": "DICTIONARY",
        "result":"Dictionary",
    },
    "is.workflow.actions.detect.dictionary": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Dictionary",
    },
    "is.workflow.actions.getvalueforkey": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Dictionary Value",
    },
    "is.workflow.actions.setvalueforkey": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Dictionary",
    },
    "is.workflow.actions.base64encode": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Base64 Encoded",
    },
    "is.workflow.actions.hash": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Hash",
    },
    "is.workflow.actions.count": {
        "glyph": "Math.svg",
        "category": "SCRIPTING",
        "result":"Count",
    },
    "is.workflow.actions.getitemname": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Name",
    },
    "is.workflow.actions.getitemtype": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Type",
    },
    "is.workflow.actions.setitemname": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Renamed Item",
    },
    "is.workflow.actions.viewresult": {
        "glyph": "",# CONTENT GRAPH SVG
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.choosefromlist": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Chosen Item",
    },
    "is.workflow.actions.getitemfromlist": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Item from List",
    },
    "is.workflow.actions.list": {
        "glyph": "Settings.svg",
        "category": "LIST",
        "result":"List",
    },
    "is.workflow.actions.math": {
        "glyph": "Math.svg",
        "category": "MATHS",
        "result":"Calculation Result",
    },
    "is.workflow.actions.statistics": {
        "glyph": "Math.svg",
        "category": "MATHS",
        "result":"Statistics", #TODO if you calculate Average, it show's Average
    },
    "is.workflow.actions.round": {
        "glyph": "Math.svg",
        "category": "MATHS",
        "result":"Rounded Number",
    },
    "is.workflow.actions.measurement.convert": {
        "glyph": "Math.svg",
        "category": "MEASUREMENT",
        "result":"Converted Measurement",
    },
    "is.workflow.actions.measurement.create": {
        "glyph": "Math.svg",
        "category": "MEASUREMENT",
        "result":"Measurement",
    },
    "is.workflow.actions.getipaddress": {
        "glyph": "Web.svg",
        "category": "SCRIPTING",
        "result":"Current IP Address",
    },
    "is.workflow.actions.getwifi": {
        "glyph": "Web.svg",
        "category": "SCRIPTING",
        "result":"Network Details",
    },
    "is.workflow.actions.airplanemode.set": {
        "glyph": "Airplane.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.bluetooth.set": {
        "glyph": "Bluetooth.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.cellulardata.set": {
        "glyph": "Mobile.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.wifi.set": {
        "glyph": "WiFi.svg",
        "category": "WI-FI",
        "result":None,
    },
    "is.workflow.actions.nothing": {
        "glyph": "Settings.svg",
        "category": "NOTHING",
        "result":None,
    },
    "is.workflow.actions.ask": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Provided Input",
    },
    "is.workflow.actions.playsound": {
        "glyph": "Volume.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.alert": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.notification": {
        "glyph": "Notification.svg",
        "category": "NOTIFICATIONS",
        "result":None,
    },
    "is.workflow.actions.showresult": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.vibrate": {
        "glyph": "Notification.svg",
        "category": "SCRIPTING",
        "result":None,
    },
    "is.workflow.actions.format.filesize": {
        "glyph": "Math.svg",
        "category": "MATHS",
        "result":"Formatted File Size",
    },
    "is.workflow.actions.format.number": {
        "glyph": "Math.svg",
        "category": "MATHS",
        "result":"Formatted Number",
    },
    "is.workflow.actions.date": {
        "glyph": "Date.svg",
        "category": "DATE",
        "result":"Date",
    },
    "is.workflow.actions.format.date": {
        "glyph": "Date.svg",
        "category": "CALENDAR",
        "result":"Formatted Date",
    },
    "is.workflow.actions.adjustdate": {
        "glyph": "Date.svg",
        "category": "CALENDAR",
        "result":"Adjusted Date",
    },
    "is.workflow.actions.detect.number": {
        "glyph": "Math.svg",
        "category": "SCRIPTING",
        "result":"Numbers",
    },
    "is.workflow.actions.number": {
        "glyph": "Math.svg",
        "category": "NUMBER",
        "result":"Number",
    },
    "is.workflow.actions.number.random": {
        "glyph": "Math.svg",
        "category": "MATHS",
        "result":"Random Number",
    },
    "is.workflow.actions.runsshscript": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":"Shell Script Result",
    },
    "is.workflow.actions.getmyworkflows": {
        "glyph": "system/Shortcuts.jpg",
        "category": "SHORTCUTS",
        "result":"My Shortcuts",
    },
    "is.workflow.actions.runworkflow": {
        "glyph": "system/Shortcuts.jpg",
        "category": "SHORTCUTS",
        "result":"Shortcut Result",
    },
    "is.workflow.actions.appendvariable": {
        "glyph": "Variable.svg",
        "category": "VARIABLES",
        "result":None,
    },
    "is.workflow.actions.setvariable": {
        "glyph": "Variable.svg",
        "category": "VARIABLES",
        "result":None,
    },
    "is.workflow.actions.getvariable": {
        "glyph": "Variable.svg",
        "category": "VARIABLES",
        'result':None, # could not reproduce this action on my phone
    },
    "is.workflow.actions.openxcallbackurl": {
        "glyph": "Link.svg",
        "category": "SCRIPTING",
        "result":"X-Callback Result",
    },
    "is.workflow.actions.urlencode": {
        "glyph": "Link.svg",
        "category": "SCRIPTING",
        "result":"URL Encoded Text",
    },
    "com.omz-software.Editorial.runworkflow": {
        "glyph": "",
        "category": "EDITORIAL",
    },
    "com.omz-software.Pythonista.editscript": {
        "glyph": "",
        "category": "PYTHONISTA",
    },
    "com.omz-software.Pythonista.runscript": {
        "glyph": "",
        "category": "PYTHONISTA",
    },
    "com.agiletortoise.Tally2.get": {
        "glyph": "",
        "category": "TALLY",
    },
    "com.agiletortoise.Tally2.updatetally": {
        "glyph": "",
        "category": "TALLY",
    },
    "is.workflow.actions.lightroom.import": {
        "glyph": "",
        "category": "MEDIA",
    },
    "is.workflow.actions.properties.appstore": {
        "glyph": "system/AppStore.jpg",
        "category": "APP STORE",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.searchappstore": {
        "glyph": "system/AppStore.jpg",
        "category": "APP STORE",
        "result":'App Store Apps',
    },
    "is.workflow.actions.recordaudio": {
        "glyph": "Record.svg",
        "category": "MEDIA",
        "result":'Recorded Audio',
    },
    "is.workflow.actions.takephoto": {
        "glyph": "system/Camera.jpg",
        "category": "CAMERA",
        "result":'Photo',
    },
    "is.workflow.actions.takevideo": {
        "glyph": "system/Camera.jpg",
        "category": "CAMERA",
        "result":'Video',
    },
    "is.workflow.actions.addframetogif": {
        "glyph": "GIF.svg",
        "category": "MEDIA",
        "result":'GIF',
    },
    "is.workflow.actions.getframesfromimage": {
        "glyph": "GIF.svg",
        "category": "MEDIA",
        "result":'Frames from Image',
    },
    "is.workflow.actions.makegif": {
        "glyph": "GIF.svg",
        "category": "MEDIA",
        "result":'GIF',
    },
    "is.workflow.actions.makevideofromgif": {
        "glyph": "GIF.svg",
        "category": "MEDIA",
        "result":'Video',
    },
    "is.workflow.actions.image.combine": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Combined Image",
    },
    "is.workflow.actions.image.crop": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Cropped Image",
    },
    "is.workflow.actions.image.flip": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Flipped Image",
    },
    "is.workflow.actions.avairyeditphoto": {
        "glyph": "Markup.svg",
        "category": "DOCUMENTS",
        "result":"Markup Result",
    },
    "is.workflow.actions.image.mask": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Masked Image",
    },
    "is.workflow.actions.overlayimageonimage": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Overlaid Image",
    },
    "is.workflow.actions.image.resize": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Resized Image",
    },
    "is.workflow.actions.image.rotate": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Rotated Image",
    },
    "is.workflow.actions.image.convert": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Converted Image",
    },
    "is.workflow.actions.properties.images": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.files": {
        "glyph": "File.svg",
        "category": "DOCUMENTS",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.health.quantity": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.reminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.calendarevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.eventattendees": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.detect.images": {
        "glyph": "Image.svg",
        "category": "MEDIA",
        "result":"Images",
    },
    "is.workflow.actions.properties.itunesartist": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.itunesstore": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.searchitunes": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE",
        "result":"iTunes Products",
    },
    "is.workflow.actions.showinstore": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE",
        "result":None,
    },
    "is.workflow.actions.getcurrentsong": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        'result':'Current Song',
    },
    "is.workflow.actions.properties.music": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.playmusic": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        'result':None,
    },
    "is.workflow.actions.exportsong": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        'result':'Music',
    },
    "is.workflow.actions.deletephotos": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        "result":None,
    },
    "is.workflow.actions.getlatestphotoimport": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        "result":'Imported Photos',
    },
    "is.workflow.actions.getlatestlivephotos": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Latest Live Photos'
    },
    "is.workflow.actions.getlastphoto": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Latest Photos'
    },
    "is.workflow.actions.getlastscreenshot": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Latest Screenshots'
    },
    "is.workflow.actions.getlastvideo": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Latest Videos'
    },
    "is.workflow.actions.selectphoto": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Photos'
    },
    "is.workflow.actions.pausemusic": {
        "glyph": "Play-Pause.svg",
        "category": "NOW PLAYING",
        "result":None,
    },
    "is.workflow.actions.skipback": {
        "glyph": "Skip-Back.svg",
        "category": "NOW PLAYING",
        "result":None,
    },
    "is.workflow.actions.skipforward": {
        "glyph": "Skip-Forward.svg",
        "category": "NOW PLAYING",
        "result":None,
    },
    "is.workflow.actions.addtoplaylist": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        'result':'Updated Playlist',
    },
    "is.workflow.actions.createplaylist": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        'result':'New Playlist',
    },
    "is.workflow.actions.get.playlist": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        'result':'Playlist',
    },
    "is.workflow.actions.properties.podcast": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.properties.podcastshow": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.getpodcastsfromlibrary": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":'Podcasts',
    },
    "is.workflow.actions.getepisodesforpodcast": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":'Episodes',
    },
    "is.workflow.actions.playpodcast": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":None,
    },
    "is.workflow.actions.searchpodcasts": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":'Podcasts',
    },
    "is.workflow.actions.podcasts.subscribe": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS",
        "result":None,
    },
    "is.workflow.actions.addmusictoupnext": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        "result":None,
    },
    "is.workflow.actions.clearupnext": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        "result":None,
    },
    "is.workflow.actions.encodemedia": {
        "glyph": "QuickTime.png",
        "category": "MEDIA",
        "result":'Encoded Media',
    },
    "is.workflow.actions.trimvideo": {
        "glyph": "QuickTime.png",
        "category": "MEDIA",
        "result":'Trimmed Media',
    },
    "is.workflow.actions.makezip": {
        "glyph": "File.svg",
        "category": "DOCUMENTS",
        'result':'Archive',
    },
    "is.workflow.actions.openin": {
        "glyph": "App.svg",
        "category": "DOCUMENTS",
        'result':None,
    },
    "is.workflow.actions.previewdocument": {
        "glyph": "Quicklook.svg",
        "category": "DOCUMENTS",
        'result':None,
    },
    "is.workflow.actions.makepdf": {
        "glyph": "Make-PDF.svg",
        "category": "DOCUMENTS",
        'result':'PDF',
    },
    "is.workflow.actions.print": {
        "glyph": "Print.svg",
        "category": "DOCUMENTS",
        'result':None,
    },
    "is.workflow.actions.generatebarcode": {
        "glyph": "QR.png",
        "category": "DOCUMENTS",
        'result':'QR Code',
    },
    "is.workflow.actions.url.getheaders": {
        "glyph": "GET.svg",
        "category": "NETWORK",
        "result":'Headers of URL',
    },
    "is.workflow.actions.gettypeaction": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING",
        "result":'File of Type',
    },
    "is.workflow.actions.getrichtextfrommarkdown": {
        "glyph": "RichText.png",
        "category": "DOCUMENTS",
        'result':'Rich Text from Markdown',
    },
    "is.workflow.actions.handoffplayback": {
        "glyph": "Handoff.svg",
        "category": "NOW PLAYING",
        "result":None,
    },
    "is.workflow.actions.getrichtextfromhtml": {
        "glyph": "RichText.png",
        "category": "DOCUMENTS",
        'result':'Rich Text from HTML',
    },
    "is.workflow.actions.gethtmlfromrichtext": {
        "glyph": "RichText.png",
        "category": "DOCUMENTS",
        'result':'HTML from Rich Text',
    },
    "is.workflow.actions.getmarkdownfromrichtext": {
        "glyph": "RichText.png",
        "category": "DOCUMENTS",
        'result':'Markdown from Rich Text',
    },
    "is.workflow.actions.dictatetext": {
        "glyph": "Dictate.svg",
        "category": "DOCUMENTS",
        'result':'Dictated Text',
    },
    "is.workflow.actions.getnameofemoji": {
        "glyph": "Emoji.svg",
        "category": "DOCUMENTS",
        'result':'Name of Emoji',
    },
    "is.workflow.actions.showdefinition": {
        "glyph": "Definition.svg",
        "category": "DOCUMENTS",
        'result':None,
    },
    "is.workflow.actions.detectlanguage": {
        "glyph": "Language.svg",
        "category": "MICROSOFT COGNITIVE SERVICES",
        'result':'Language',
    },
    "is.workflow.actions.airdropdocument": {
        "glyph": "Airdrop.svg",
        "category": "AIRDROP",
        "result":None,
    },
    "is.workflow.actions.share": {
        "glyph": "Share.svg",
        "category": "SHARING",
        "result":None,
    },
    "is.workflow.actions.savetocameraroll": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Saved Photo Media'
    },
    "is.workflow.actions.getlatestbursts": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS",
        'result':'Latest Bursts'
    },
    "is.workflow.actions.detect.text": {
        "glyph": "Note.svg",
        "category": "DOCUMENTS",
        'result':'Text',
    },
    "is.workflow.actions.unzip":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
        'result':'Files',
    },
    "is.workflow.actions.file.createfolder":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
        'result':None,
    },
    "is.workflow.actions.file.delete":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
        'result':None,
    },
    "is.workflow.actions.documentpicker.open":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
        'result':'File',
    },
    "is.workflow.actions.documentpicker.save":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
        'result':'Saved File',
    },
    "is.workflow.actions.file.getlink":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
        'result':'Link to File',
    },
    "is.workflow.actions.text.match.getgroup":{
        "glyph": "Note.svg",
        "category": "TEXT",
        'result':'Text',
    },
    "is.workflow.actions.text.match":{
        "glyph": "Note.svg",
        "category": "TEXT",
        'result':'Matches',
    },
    "is.workflow.actions.text.changecase":{
        "glyph": "Note.svg",
        "category": "TEXT",
        'result':'Updated Text',
    },
    "is.workflow.actions.correctspelling":{
        "glyph": "Note.svg",
        "category": "DOCUMENTS",
        'result':'Corrected Spelling',
    },
    "is.workflow.actions.text.split": {
        "glyph": "Note.svg",
        "category": "TEXT",
        'result':'Split Text',
    },
    "is.workflow.actions.text.combine": {
        "glyph": "Note.svg",
        "category": "TEXT",
        'result':'Combined Text',
    },
    "is.workflow.actions.text.replace": {
        "glyph": "Note.svg",
        "category": "DOCUMENTS",
        'result':'Updated Text',
    },
    "is.workflow.actions.downloadurl": {
        "glyph": "GET.svg",
        "category": "NETWORK",
        "result":'Contents of URL',
    },
    "is.workflow.actions.gettext": {
        "glyph": "Note.svg",
        "category": "TEXT",
        'result':'Text',
    },
    "is.workflow.actions.setclipboard": {
        "glyph": "Clipboard.svg",
        "category": "SHARING",
        "result":None,
    },
    "is.workflow.actions.getclipboard": {
        "glyph": "Clipboard.svg",
        "category": "SHARING",
        "result":'Clipboard',
    },
    "is.workflow.actions.getcurrentlocation": {
        "glyph": "Location.svg",
        "category": "LOCATION",
        "result":'Current Location',
    },
    "is.workflow.actions.properties.locations": {
        "glyph": "Location.svg",
        "category": "LOCATION",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.location": {
        "glyph": "Location.svg",
        "category": "LOCATION",
        "result":'Location',
    },
    "is.workflow.actions.detect.address": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Addresses',
    },
    "is.workflow.actions.address": {
        "glyph": "system/Maps.png",
        "category": "STREET ADDRESS",
        'result':'Street Address',
    },
    "is.workflow.actions.getmapslink": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Maps URL',
    },
    "is.workflow.actions.getdirections": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':None,
    },
    "is.workflow.actions.searchmaps": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':None,
    },
    "is.workflow.actions.getdistance": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Distance',
    },
    "is.workflow.actions.gethalfwaypoint": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Halfway Point',
    },
    "is.workflow.actions.gettraveltime": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Travel Time',
    },
    "is.workflow.actions.searchlocalbusinesses": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Local Businesses',
    },
    "is.workflow.actions.weather.currentconditions": {
        "glyph": "system/Weather.png",
        "category": "LOCATION",
        "result":'Weather Conditions',
    },
    "is.workflow.actions.properties.weather.conditions": {
        "glyph": "system/Weather.png",
        "category": "LOCATION",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.weather.forecast": {
        "glyph": "system/Weather.png",
        "category": "LOCATION",
        "result":'Weather Conditions',
    },
    "is.workflow.actions.sendemail": {
        "glyph": "system/Mail.png",
        "category": "MAIL",
    },
    "is.workflow.actions.sendmessage": {
        "glyph": "system/Messages.jpg",
        "category": "MESSAGES",
    },
    "com.apple.mobilenotes.SharingExtension": {
        "glyph": "system/Notes.png",
        "category": "NOTES",
    },
    "com.apple.mobileslideshow.StreamShareService": {
        "glyph": "system/Photos.png",
        "category": "Photos",
    },
    "is.workflow.actions.runextension": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "is.workflow.actions.cloudapp.upload": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "is.workflow.actions.postonfacebook": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "com.burbn.instagram.openin": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "is.workflow.actions.tumblr.post": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "com.tapbots.Tweetbot.opentweetbot": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "com.tapbots.Tweetbot.searchtext": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "com.tapbots.Tweetbot.viewprofile": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "com.tapbots.Tweetbot.tweet": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "is.workflow.actions.tweet": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "net.whatsapp.WhatsApp.send": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "net.whatsapp.WhatsApp.openin": {
        "glyph": "NULL",
        "category": "NULL",
    },
    "is.workflow.actions.wordpress.post": {
        "glyph": "NULL",
        "category": "NULL",
    },
    'is.workflow.actions.useractivity.open':{
        "glyph": "PLACEHOLDER",
        "category": "PLACEHOLDER",
        "result":None, # not sure if these can return anything
    },
    "is.workflow.actions.getarticle": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":'Article',
    },
    "is.workflow.actions.properties.articles": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.rss": {
        "glyph": "RSS.svg",
        "category": "WEB",
        "result":'Items from RSS Feed',
    },
    "is.workflow.actions.rss.extract": {
        "glyph": "RSS.svg",
        "category": "WEB",
        "result":'RSS Feeds from Page',
    },
    "is.workflow.actions.readinglist": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None,
    },
    "is.workflow.actions.properties.safariwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.openurl": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None,
    },
    "is.workflow.actions.runjavascriptonwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":'JavaScript Result',
    },
    "is.workflow.actions.searchweb": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None,
    },
    "is.workflow.actions.showwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None,
    },
    "is.workflow.actions.url.expand": {
        "glyph": "Link.svg",
        "category": "WEB",
        "result":'Expanded URL',
    },
    "is.workflow.actions.geturlcomponent": {
        "glyph": "Link.svg",
        "category": "URL",
        "result":'Component of URL',
    },
    "is.workflow.actions.detect.link": {
        "glyph": "Link.svg",
        "category": "WEB",
        "result":'URLs',
    },
    "is.workflow.actions.url": {
        "glyph": "Link.svg",
        "category": "URL",
        "result":'URL',
    },
    "is.workflow.actions.getwebpagecontents": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":'Contents of Web Page',
    },
    "com.google.chrome.ios.openurl": {
        "glyph": "others/Chrome",
        "category": "GOOGLE CHROME",
        "result":None,
    },
    "NULL": {
        "glyph": "NULL",
        "category": "NULL",
    },
}

def not_implemented_action(category:str = '', indent_level:int = 0, sub_name:str = 'Action', glyph:str = ''):
    return {
        'title': [{'value':f'{sub_name} Under Construction','class':'not-implemented'}],
        'line': [],
        'glyph': f'assets/cat/{glyph}',
        'category': category,
        'indent': indent_level if indent_level else '',
        'result':None,
    }

def not_implemented_options():
    return {
        'label':'',
        'class':'not-implemented',
        'value':'Options Under Construction',
    }

def error_action():
    return {
        'title': [{'value':'Error Loading Action','class':'error'}],
        'line': [],
        'glyph': '',#deliberately blank
        'category': '',
        'indent': '',
    }

color_dict = {
    4282601983:"(227,104,109)",
	4251333119:"(226,192,91)",
	4271458815:"(216,122,68)",
	4274264319:"(210,150,57)",
	4292093695:"(108,162,81)",
	431817727:"(86,159,136)",
	1440408063:"(95,153,171)",
	463140863:"(106,141,189)",
	946986751:"(111,122,191)",
	2071128575:"(139,115,186)",
	3679049983:"(185,119,187)",
	3980825855:"(217,111,140)",
	255:"(130,140,150)",
	3031607807:"(136,141,137)",
	2846468607:"(153,140,135)",
}

accessibility_toggles = {
    'AXToggleSwitchControlIntent':'Switch Control',
    'AXToggleLEDFlashIntent':'LED Flash',
    'AXToggleAssistiveTouchIntent':'AssistiveTouch',
    'AXToggleAudioDescriptionsIntent':'Audio Descriptions',
    'AXToggleClassicInvertIntent':'Classic Invert',
    'AXToggleSmartInvertIntent':'Smart Invert',
    'AXToggleCaptionsIntent':'Closed Captions+SDH',
    'AXToggleContrastIntent':'Increase Contrast',
    'AXToggleMonoAudioIntent':'Mono Audio',
    'AXToggleReduceMotionIntent':'Reduce Motion',
    'AXToggleTransparencyIntent':'Reduce Transparency',
    'AXToggleVoiceControlIntent':'Voice Control',
    'AXToggleVoiceOverIntent':'VoiceOver',
    'AXToggleWhitePointIntent':'White Point',
    'AXToggleZoomIntent':'Zoom',
}

extension_lookup = {
    'WFAppStoreAppContentItem':'App Store Apps',
    'WFArticleContentItem':'Articles',
    'WFContactContentItem':'Contacts',
    'WFDateContentItem':'Dates',
    'WFEmailAddressContentItem':'Email Addresses',
    'WFGenericFileContentItem':'Files',
    'WFImageContentItem':'Images',
    'WFiTunesProductContentItem':'iTunes Products',
    'WFLocationContentItem':'Locations',
    'WFDCMapsLinkContentItem':'Map Links',
    'WFAVAssetContentItem':'Media',
    'WFPDFContentItem':'PDFs',
    'WFPhoneNumberContentItem':'Phone Numbers',
    'WFRichTextContentItem':'Rich Text',
    'WFSafariWebPageContentItem':'Safari Web Pages',
    'WFStringContentItem':'Text',
    'WFURLContentItem':'URLs',
}

time_codes = {
    'sec':'second',
    'min':'minute',
    'hr':'hour',
}