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
        "category": "INSTAPAPER"
    },
    "is.workflow.actions.properties.trello": {
        "glyph": "others/Trello.png",
        "category": "TRELLO"
    },
    "is.workflow.actions.properties.ulysses.sheet": {
        "glyph": "others/Ulysses.png",
        "category": "ULYSSES"
    },
    "is.workflow.actions.instapaper.get": {
        "glyph": "others/Instapaper.png",
        "category": "INSTAPAPER"
    },
    "is.workflow.actions.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS"
    },
    "is.workflow.actions.detect.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS"
    },
    "is.workflow.actions.detect.phonenumber": {
        "glyph": "Phone.svg",
        "category": "CONTACTS"
    },
    "is.workflow.actions.phonenumber": {
        "glyph": "Phone.svg",
        "category": "PHONE NUMBER"
    },
    "is.workflow.actions.selectcontacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS"
    },
    "is.workflow.actions.selectphone": {
        "glyph": "Phone.svg",
        "category": "CONTACTS"
    },
    "is.workflow.actions.timer.start": {
        "glyph": "system/Clock.png",
        "category": "CLOCK"
    },
    "is.workflow.actions.addnewevent": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.getupcomingevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.removeevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.showincalendar": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "com.apple.iBooks.openin": {
        "glyph": "system/Books.png",
        "category": "BOOKS"
    },
    "is.workflow.actions.appendnote": {
        "glyph": "system/Notes.jpg",
        "category": "NOTES"
    },
    "is.workflow.actions.shownote": {
        "glyph": "system/Notes.jpg",
        "category": "NOTES"
    },
    "com.apple.mobilephone.call": {
        "glyph": "system/Phone.png",
        "category": "PHONE"
    },
    "is.workflow.actions.venmo.request": {
        "glyph": "system/applepay",
        "category": "WALLET"
    },
    "is.workflow.actions.venmo.pay": {
        "glyph": "system/applepay",
        "category": "WALLET"
    },
    "is.workflow.actions.filter.articles": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.filter.locations": {
        "glyph": "Location.svg",
        "category": "LOCATION"
    },
    "is.workflow.actions.filter.files": {
        "glyph": "File.svg",
        "category": "FILES"
    },
    "is.workflow.actions.filter.photos": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.filter.music": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.filter.images": {
        "glyph": "Image.svg",
        "category": "IMAGES"
    },
    "is.workflow.actions.filter.eventattendees": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.filter.calendarevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.addnewreminder": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS"
    },
    "is.workflow.actions.getupcomingreminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS"
    },
    "is.workflow.actions.removereminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS"
    },
    "is.workflow.actions.reminders.showlist": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS"
    },
    "is.workflow.actions.filter.reminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS"
    },
    "is.workflow.actions.filter.notes": {
        "glyph": "system/Notes.jpg",
        "category": "NOTES"
    },
    "is.workflow.actions.filter.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS"
    },
    "is.workflow.actions.filter.health.quantity": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH"
    },
    "is.workflow.actions.health.workout.log": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH"
    },
    "is.workflow.actions.health.quantity.log": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH"
    },
    "is.workflow.actions.comment": {
        "glyph": "Note.svg",
        "category": "COMMENT"
    },
    "is.workflow.actions.openapp": {
        "glyph": "App.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.choosefrommenu": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.handoff": {
        "glyph": "Handoff.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.exit": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.conditional": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.repeat.count": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.repeat.each": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.delay": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.waittoreturn": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getbatterylevel": {
        "glyph": "Battery.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getdevicedetails": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.appearance": {
        "glyph": "Brightness.svg",
        "category": "APPEARANCE"
    },
    "is.workflow.actions.setbrightness": {
        "glyph": "Brightness.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.dnd.set": {
        "glyph": "DND.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.flashlight": {
        "glyph": "Flashlight.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.lowpowermode.set": {
        "glyph": "Battery.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.setplaybackdestination": {
        "glyph": "AirplayAudio.svg",
        "category": "AIRPLAY"
    },
    "is.workflow.actions.setvolume": {
        "glyph": "Volume.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.dictionary": {
        "glyph": "Settings.svg",
        "category": "DICTIONARY"
    },
    "is.workflow.actions.detect.dictionary": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getvalueforkey": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.setvalueforkey": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.base64encode": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.hash": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.count": {
        "glyph": "Math.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getitemname": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getitemtype": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.setitemname": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.viewresult": {
        "glyph": "",# CONTENT GRAPH SVG
        "category": "SCRIPTING"
    },
    "is.workflow.actions.choosefromlist": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getitemfromlist": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.list": {
        "glyph": "Settings.svg",
        "category": "LIST"
    },
    "is.workflow.actions.math": {
        "glyph": "Math.svg",
        "category": "MATHS"
    },
    "is.workflow.actions.statistics": {
        "glyph": "Math.svg",
        "category": "MATHS"
    },
    "is.workflow.actions.round": {
        "glyph": "Math.svg",
        "category": "MATHS"
    },
    "is.workflow.actions.measurement.convert": {
        "glyph": "Math.svg",
        "category": "MEASUREMENT"
    },
    "is.workflow.actions.measurement.create": {
        "glyph": "Math.svg",
        "category": "MEASUREMENT"
    },
    "is.workflow.actions.getipaddress": {
        "glyph": "Web.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getwifi": {
        "glyph": "Web.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.airplanemode.set": {
        "glyph": "Airplane.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.bluetooth.set": {
        "glyph": "Bluetooth.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.cellulardata.set": {
        "glyph": "Mobile.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.wifi.set": {
        "glyph": "WiFi.svg",
        "category": "WI-FI"
    },
    "is.workflow.actions.nothing": {
        "glyph": "Settings.svg",
        "category": "NOTHING"
    },
    "is.workflow.actions.ask": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.playsound": {
        "glyph": "Volume.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.alert": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.notification": {
        "glyph": "Notification.svg",
        "category": "NOTIFICATIONS"
    },
    "is.workflow.actions.showresult": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.vibrate": {
        "glyph": "Notification.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.format.filesize": {
        "glyph": "Math.svg",
        "category": "MATHS"
    },
    "is.workflow.actions.format.number": {
        "glyph": "Math.svg",
        "category": "MATHS"
    },
    "is.workflow.actions.format.date": {
        "glyph": "Date.svg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.adjustdate": {
        "glyph": "Date.svg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.detect.number": {
        "glyph": "Math.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.number": {
        "glyph": "Math.svg",
        "category": "NUMBER"
    },
    "is.workflow.actions.number.random": {
        "glyph": "Math.svg",
        "category": "MATHS"
    },
    "is.workflow.actions.runsshscript": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getmyworkflows": {
        "glyph": "system/Shortcuts.jpg",
        "category": "SHORTCUTS"
    },
    "is.workflow.actions.runworkflow": {
        "glyph": "system/Shortcuts.jpg",
        "category": "SHORTCUTS"
    },
    "is.workflow.actions.appendvariable": {
        "glyph": "Variable.svg",
        "category": "VARIABLES"
    },
    "is.workflow.actions.setvariable": {
        "glyph": "Variable.svg",
        "category": "VARIABLES"
    },
    "is.workflow.actions.getvariable": {
        "glyph": "Variable.svg",
        "category": "VARIABLES"
    },
    "is.workflow.actions.openxcallbackurl": {
        "glyph": "Link.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.urlencode": {
        "glyph": "Link.svg",
        "category": "SCRIPTING"
    },
    "com.omz-software.Editorial.runworkflow": {
        "glyph": "",
        "category": "EDITORIAL"
    },
    "com.omz-software.Pythonista.editscript": {
        "glyph": "",
        "category": "PYTHONISTA"
    },
    "com.omz-software.Pythonista.runscript": {
        "glyph": "",
        "category": "PYTHONISTA"
    },
    "com.agiletortoise.Tally2.get": {
        "glyph": "",
        "category": "TALLY"
    },
    "com.agiletortoise.Tally2.updatetally": {
        "glyph": "",
        "category": "TALLY"
    },
    "is.workflow.actions.lightroom.import": {
        "glyph": "",
        "category": "MEDIA"
    },
    "is.workflow.actions.properties.appstore": {
        "glyph": "system/AppStore.jpg",
        "category": "APP STORE"
    },
    "is.workflow.actions.searchappstore": {
        "glyph": "system/AppStore.jpg",
        "category": "APP STORE"
    },
    "is.workflow.actions.recordaudio": {
        "glyph": "Record.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.takephoto": {
        "glyph": "system/Camera.jpg",
        "category": "CAMERA"
    },
    "is.workflow.actions.takevideo": {
        "glyph": "system/Camera.jpg",
        "category": "CAMERA"
    },
    "is.workflow.actions.addframetogif": {
        "glyph": "GIF.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.getframesfromimage": {
        "glyph": "GIF.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.makegif": {
        "glyph": "GIF.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.makevideofromgif": {
        "glyph": "GIF.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.image.combine": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.image.crop": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.image.flip": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.avairyeditphoto": {
        "glyph": "Markup.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.image.mask": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.overlayimageonimage": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.image.resize": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.image.rotate": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.image.convert": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.properties.images": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.properties.files": {
        "glyph": "File.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.properties.contacts": {
        "glyph": "system/Contacts.png",
        "category": "CONTACTS"
    },
    "is.workflow.actions.properties.health.quantity": {
        "glyph": "system/Health.jpg",
        "category": "HEALTH"
    },
    "is.workflow.actions.properties.reminders": {
        "glyph": "system/Reminders.png",
        "category": "REMINDERS"
    },
    "is.workflow.actions.properties.calendarevents": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.properties.eventattendees": {
        "glyph": "system/Calendar.jpg",
        "category": "CALENDAR"
    },
    "is.workflow.actions.detect.images": {
        "glyph": "Image.svg",
        "category": "MEDIA"
    },
    "is.workflow.actions.properties.itunesartist": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE"
    },
    "is.workflow.actions.properties.itunesstore": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE"
    },
    "is.workflow.actions.searchitunes": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE"
    },
    "is.workflow.actions.showinstore": {
        "glyph": "iTunes.svg",
        "category": "ITUNES STORE"
    },
    "is.workflow.actions.getcurrentsong": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.properties.music": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.playmusic": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.exportsong": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.deletephotos": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.getlatestphotoimport": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.getlatestlivephotos": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.getlastphoto": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.getlastscreenshot": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.getlastvideo": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.selectphoto": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.pausemusic": {
        "glyph": "Play-Pause.svg",
        "category": "NOW PLAYING"
    },
    "is.workflow.actions.skipback": {
        "glyph": "Skip-Back.svg",
        "category": "NOW PLAYING"
    },
    "is.workflow.actions.skipforward": {
        "glyph": "Skip-Forward.svg",
        "category": "NOW PLAYING"
    },
    "is.workflow.actions.addtoplaylist": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.createplaylist": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.get.playlist": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.properties.podcast": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.properties.podcastshow": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.getpodcastsfromlibrary": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.getepisodesforpodcast": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.playpodcast": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.searchpodcasts": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.podcasts.subscribe": {
        "glyph": "system/Podcasts.png",
        "category": "PODCASTS"
    },
    "is.workflow.actions.addmusictoupnext": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.clearupnext": {
        "glyph": "system/Music.png",
        "category": "MUSIC"
    },
    "is.workflow.actions.encodemedia": {
        "glyph": "Quicktime",
        "category": "MEDIA"
    },
    "is.workflow.actions.trimvideo": {
        "glyph": "Quicktime",
        "category": "MEDIA"
    },
    "is.workflow.actions.makezip": {
        "glyph": "File.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.openin": {
        "glyph": "App.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.previewdocument": {
        "glyph": "Quicklook.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.makepdf": {
        "glyph": "Make-PDF.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.print": {
        "glyph": "Print.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.generatebarcode": {
        "glyph": "QR.png",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.url.getheaders": {
        "glyph": "GET.svg",
        "category": "NETWORK"
    },
    "is.workflow.actions.gettypeaction": {
        "glyph": "Settings.svg",
        "category": "SCRIPTING"
    },
    "is.workflow.actions.getrichtextfrommarkdown": {
        "glyph": "Richtext",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.handoffplayback": {
        "glyph": "Handoff.svg",
        "category": "NOW PLAYING"
    },
    "is.workflow.actions.getrichtextfromhtml": {
        "glyph": "Richtext",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.gethtmlfromrichtext": {
        "glyph": "Richtext",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.getmarkdownfromrichtext": {
        "glyph": "Richtext",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.dictatetext": {
        "glyph": "Dictate.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.getnameofemoji": {
        "glyph": "Emoji.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.showdefinition": {
        "glyph": "Definition.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.detectlanguage": {
        "glyph": "Language.svg",
        "category": "MICROSOFT COGNITIVE SERVICES"
    },
    "is.workflow.actions.airdropdocument": {
        "glyph": "Airdrop.svg",
        "category": "AIRDROP"
    },
    "is.workflow.actions.share": {
        "glyph": "Share.svg",
        "category": "SHARING"
    },
    "is.workflow.actions.savetocameraroll": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.getlatestbursts": {
        "glyph": "system/Photos.png",
        "category": "PHOTOS"
    },
    "is.workflow.actions.detect.text": {
        "glyph": "Note.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.unzip":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
    },
    "is.workflow.actions.file.createfolder":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
    },
    "is.workflow.actions.file.delete":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
    },
    "is.workflow.actions.documentpicker.open":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
    },
    "is.workflow.actions.documentpicker.save":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
    },
    "is.workflow.actions.file.getlink":{
        "glyph": "File.svg",
        "category":"DOCUMENTS",
    },
    "is.workflow.actions.text.match.getgroup":{
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    "is.workflow.actions.text.match":{
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    "is.workflow.actions.text.changecase":{
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    "is.workflow.actions.correctspelling":{
        "glyph": "Note.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.text.split": {
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    "is.workflow.actions.text.combine": {
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    "is.workflow.actions.text.replace": {
        "glyph": "Note.svg",
        "category": "DOCUMENTS"
    },
    "is.workflow.actions.downloadurl": {
        "glyph": "GET.svg",
        "category": "NETWORK"
    },
    "is.workflow.actions.gettext": {
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    "is.workflow.actions.setclipboard": {
        "glyph": "Clipboard.svg",
        "category": "SHARING"
    },
    "is.workflow.actions.getclipboard": {
        "glyph": "Clipboard.svg",
        "category": "SHARING"
    },
    "is.workflow.actions.getcurrentlocation": {
        "glyph": "Location.svg",
        "category": "LOCATION"
    },
    "is.workflow.actions.properties.locations": {
        "glyph": "Location.svg",
        "category": "LOCATION"
    },
    "is.workflow.actions.location": {
        "glyph": "Location.svg",
        "category": "LOCATION"
    },
    "is.workflow.actions.detect.address": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.address": {
        "glyph": "system/Maps.png",
        "category": "STREET ADDRESS"
    },
    "is.workflow.actions.getmapslink": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.getdirections": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.searchmaps": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.getdistance": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.gethalfwaypoint": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.gettraveltime": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.searchlocalbusinesses": {
        "glyph": "system/Maps.png",
        "category": "MAPS"
    },
    "is.workflow.actions.weather.currentconditions": {
        "glyph": "system/Weather.png",
        "category": "LOCATION"
    },
    "is.workflow.actions.properties.weather.conditions": {
        "glyph": "system/Weather.png",
        "category": "LOCATION"
    },
    "is.workflow.actions.weather.forecast": {
        "glyph": "system/Weather.png",
        "category": "LOCATION"
    },
    "is.workflow.actions.sendemail": {
        "glyph": "system/Mail.png",
        "category": "MAIL"
    },
    "is.workflow.actions.sendmessage": {
        "glyph": "system/Messages.jpg",
        "category": "MESSAGES"
    },
    "com.apple.mobilenotes.SharingExtension": {
        "glyph": "system/Notes.jpg",
        "category": "NOTES"
    },
    "com.apple.mobileslideshow.StreamShareService": {
        "glyph": "system/Photos.png",
        "category": "Photos"
    },
    "is.workflow.actions.runextension": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "is.workflow.actions.cloudapp.upload": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "is.workflow.actions.postonfacebook": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "com.burbn.instagram.openin": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "is.workflow.actions.tumblr.post": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "com.tapbots.Tweetbot.opentweetbot": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "com.tapbots.Tweetbot.searchtext": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "com.tapbots.Tweetbot.viewprofile": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "com.tapbots.Tweetbot.tweet": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "is.workflow.actions.tweet": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "net.whatsapp.WhatsApp.send": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "net.whatsapp.WhatsApp.openin": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "is.workflow.actions.wordpress.post": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "is.workflow.actions.text.combine": {
        "glyph": "Note.svg",
        "category": "TEXT"
    },
    'is.workflow.actions.useractivity.open':{
        "glyph": "PLACEHOLDER",
        "category": "PLACEHOLDER"
    },
    "is.workflow.actions.getarticle": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.properties.articles": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.rss": {
        "glyph": "RSS.svg",
        "category": "WEB"
    },
    "is.workflow.actions.rss.extract": {
        "glyph": "RSS.svg",
        "category": "WEB"
    },
    "is.workflow.actions.readinglist": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.properties.safariwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.openurl": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.runjavascriptonwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.searchweb": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.showwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "is.workflow.actions.url.expand": {
        "glyph": "Link.svg",
        "category": "WEB"
    },
    "is.workflow.actions.geturlcomponent": {
        "glyph": "Link.svg",
        "category": "URL"
    },
    "is.workflow.actions.detect.link": {
        "glyph": "Link.svg",
        "category": "WEB"
    },
    "is.workflow.actions.url": {
        "glyph": "Link.svg",
        "category": "URL"
    },
    "is.workflow.actions.getwebpagecontents": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI"
    },
    "com.google.chrome.ios.openurl": {
        "glyph": "others/Chrome",
        "category": "GOOGLE CHROME"
    },
    "NULL": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "NULL": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "NULL": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "NULL": {
        "glyph": "NULL",
        "category": "NULL"
    },
    "NULL": {
        "glyph": "NULL",
        "category": "NULL"
    },
}

def not_implemented_action(category:str = '', indent_level:int = 0, sub_name:str = 'Action', glyph:str = ''):
    return {
        'title': [{'value':f'{sub_name} Under Construction','class':'not-implemented'}],
        'line': [],
        'glyph': f'assets/cat/{glyph}',
        'category': category,
        'indent': indent_level if indent_level else '',
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