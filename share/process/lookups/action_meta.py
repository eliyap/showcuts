# # #
# lookup for action's aesthetic decorations
# 1. Glyph / App Icon in the top left hand corner
# 2. App Category beside the glyph / icon (ALL CAPS)
# 3. The action's result (output), if any, available as a magic var to other actions
# # #

dct = {
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
    "is.workflow.actions.imgur.upload":{
        "glyph": "others/Imgur.png",
        "category": "IMGUR",
        'result':'Imgur URLs',
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
    
    "is.workflow.actions.appearance": {
        "glyph": "Brightness.svg",
        "category": "APPEARANCE",
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
    "is.workflow.actions.listeningmode.set":{
        "glyph": "Headphones.svg",
        "category": "HEADPHONES",
        'result':None,
    },
    "is.workflow.actions.notification": {
        "glyph": "Notification.svg",
        "category": "NOTIFICATIONS",
        "result":None,
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
    "is.workflow.actions.properties.music": {
        "glyph": "system/Music.png",
        "category": "MUSIC",
        "result":None, # handled elsewhere
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
    # "is.workflow.actions.encodemedia": {
    #     "glyph": "QuickTime.png",
    #     "category": "MEDIA",
    #     "result":'Encoded Media',
    # },
    # "is.workflow.actions.trimvideo": {
    #     "glyph": "QuickTime.png",
    #     "category": "MEDIA",
    #     "result":'Trimmed Media',
    # },
    "is.workflow.actions.url.getheaders": {
        "glyph": "GET.svg",
        "category": "NETWORK",
        "result":'Headers of URL',
    },
    "is.workflow.actions.handoffplayback": {
        "glyph": "Handoff.svg",
        "category": "NOW PLAYING",
        "result":None,
    },
    # "is.workflow.actions.detectlanguage": {
    #     "glyph": "Language.svg",
    #     "category": "MICROSOFT COGNITIVE SERVICES",
    #     'result':'Language',
    # },
    # "is.workflow.actions.text.translate":{
    #     "glyph": "Language.svg",
    #     "category": "MICROSOFT COGNITIVE SERVICES",
    #     'result':'Translated Text',
    # },
    # "is.workflow.actions.airdropdocument": {
    #     "glyph": "Airdrop.svg",
    #     "category": "AIRDROP",
    #     "result":None,
    # },
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
    "is.workflow.actions.downloadurl": {
        "glyph": "GET.svg",
        "category": "NETWORK",
        "result":'Contents of URL',
    },
    # "is.workflow.actions.setclipboard": {
    #     "glyph": "Clipboard.svg",
    #     "category": "SHARING",
    #     "result":None,
    # },
    # "is.workflow.actions.getclipboard": {
    #     "glyph": "Clipboard.svg",
    #     "category": "SHARING",
    #     "result":'Clipboard',
    # },
    "is.workflow.actions.properties.locations": {
        "glyph": "Location.svg",
        "category": "LOCATION",
        "result":None, # handled elsewhere
    },
    "is.workflow.actions.detect.address": {
        "glyph": "system/Maps.png",
        "category": "MAPS",
        'result':'Addresses',
    },
    "is.workflow.actions.properties.weather.conditions": {
        "glyph": "system/Weather.png",
        "category": "LOCATION",
        "result":None, # handled elsewhere
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
    # "is.workflow.actions.rss": {
    #     "glyph": "RSS.svg",
    #     "category": "WEB",
    #     "result":'Items from RSS Feed',
    # },
    # "is.workflow.actions.rss.extract": {
    #     "glyph": "RSS.svg",
    #     "category": "WEB",
    #     "result":'RSS Feeds from Page',
    # },
    "is.workflow.actions.properties.safariwebpage": {
        "glyph": "system/Safari.jpg",
        "category": "SAFARI",
        "result":None, # handled elsewhere
    },
    # "is.workflow.actions.url.expand": {
    #     "glyph": "Link.svg",
    #     "category": "WEB",
    #     "result":'Expanded URL',
    # },
    # "is.workflow.actions.geturlcomponent": {
    #     "glyph": "Link.svg",
    #     "category": "URL",
    #     "result":'Component of URL',
    # },
    # "is.workflow.actions.detect.link": {
    #     "glyph": "Link.svg",
    #     "category": "WEB",
    #     "result":'URLs',
    # },
    # "is.workflow.actions.url": {
    #     "glyph": "Link.svg",
    #     "category": "URL",
    #     "result":'URL',
    # },
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