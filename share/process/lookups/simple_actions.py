# # #
# Uni Params: Accept 1 input, with key WFInput, and blank value "Input"
# mostly for delect.* actions
# # #
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
    'detect.date':'Get dates from',
    'print':'Print',
    'share':'Share',
}

# # #
# Toggles: these actions flip a simple switch on iOS
# logic is handled elsewhere
# # #
toggle_params = {
    'airplanemode.set':'Turn Airplane Mode', 
    'bluetooth.set':'Turn Bluetooth',
    'cellulardata.set':'Turn Mobile Data', 
    'wifi.set':'Turn Wi-Fi',
    'lowpowermode.set':'Turn Low Power Mode',
}

# # #
# No Parameters: These Actions have no magic fields / inputs.
# Their titles are simple copy
# # #
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
    'is.workflow.actions.scanbarcode':'Scan QR/Barcode',
    'com.apple.mobiletimer-framework.MobileTimerIntents.MTGetAlarmsIntent':'Get all alarms',
    'fm.overcast.overcast.add':'Add to Overcast',
}

# # #
# Accessiblity Actions from Settings
# # #
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