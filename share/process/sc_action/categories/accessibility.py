import re

from ..action import action
from share.process.components._directory import *
from share.process.lookups._directory import accessibility_toggles

def setting_title(setting_code:str, default:int):
    return [
        choose(
            'operation',
            ask_each_time='Operation',
            default='Turn',
            options=['Turn','Toggle'],
        ),
        text(accessibility_toggles[setting_code]),
        choose(
            'state',
            ask_each_time='State',
            default=default,
            options=['on','off'],
        )
    ]

class _base(action):
    category = 'SETTINGS'
    glyph = 'system/Settings.png'
    
    def modify(self):
        # "1 / 0" -> "On / Off"
        on_off_elem = self.get_title('state')
        on_off_elem['value'] = {1:'on',0:'off'}.get(
            on_off_elem['value'],
            on_off_elem['value'],
        )

        # title case the term
        self.get_title('operation')['value'] = self.get_title('operation')['value'].title()

        # hide on_off_elem if switch is not "Turn"
        if self.get_title('operation')['value'] != 'Turn':
            self.hide_title('state')

class AXToggleSwitchControlIntent(_base):
    name = 'Set Switch Control'
    title = setting_title('AXToggleSwitchControlIntent',1)

class AXToggleLEDFlashIntent(_base):
    name = 'Set LED Flash'
    title = setting_title('AXToggleLEDFlashIntent',1)

class AXToggleAssistiveTouchIntent(_base):
    name = 'Set AssistiveTouch'
    title = setting_title('AXToggleAssistiveTouchIntent',1)

class AXToggleAudioDescriptionsIntent(_base):
    name = 'Set Audio Descriptions'
    title = setting_title('AXToggleAudioDescriptionsIntent',1)

class AXToggleClassicInvertIntent(_base):
    name = 'Set Classic Invert'
    title = setting_title('AXToggleClassicInvertIntent',0)

class AXToggleSmartInvertIntent(_base):
    name = 'Set Smart Invert'
    title = setting_title('AXToggleSmartInvertIntent',1)

class AXToggleCaptionsIntent(_base):
    name = 'Set Closed Captions+SDH'
    title = setting_title('AXToggleCaptionsIntent',1)

class AXToggleContrastIntent(_base):
    name = 'Set Increase Contrast'
    title = setting_title('AXToggleContrastIntent',1)

class AXToggleMonoAudioIntent(_base):
    name = 'Set Mono Audio'
    title = setting_title('AXToggleMonoAudioIntent',1)

class AXToggleReduceMotionIntent(_base):
    name = 'Set Reduce Motion'
    title = setting_title('AXToggleReduceMotionIntent',0)

class AXToggleTransparencyIntent(_base):
    name = 'Set Reduce Transparency'
    title = setting_title('AXToggleTransparencyIntent',1)

class AXToggleVoiceControlIntent(_base):
    name = 'Set Voice Control'
    title = setting_title('AXToggleVoiceControlIntent',1)

class AXToggleVoiceOverIntent(_base):
    name = 'Set VoiceOver'
    title = setting_title('AXToggleVoiceOverIntent',1)

class AXToggleWhitePointIntent(_base):
    name = 'Set White Point'
    title = setting_title('AXToggleWhitePointIntent',1)

class AXToggleZoomIntent(_base):
    name = 'Set Zoom'
    title = setting_title('AXToggleZoomIntent',1)

class AXSetLargeTextIntent(action):
    name = 'Set Text Size'
    category = 'SETTINGS'
    glyph = 'system/Settings.png'

    title = [
        text('Set text size to'),
        choose(
            'textSize',
            ask_each_time='Text Size',
            default='extra small',
            options=[
                'extra small',
                'small',
                'medium',
                'default',
                'extra large',
                'extra extra large',
                'extra extra extra large',
                'accessibility medium',
                'accessibility large',
                'accessibility extra large',
                'accessibility extra extra large',
                'accessibility extra extra extra large',
            ]
        ),
    ]
    
    def modify(self):
        try: # make 'AX Extra Large' and such human readable
            size = self.title[1]
            size['value'] = re.sub('Extra','Extra ', size['value'])
            size['value'] = re.sub('AX','accessibility ', size['value'])
            if size['value'] != 'Text Size':
                size['value'] = size['value'].lower()
        except:
            pass
class _base2(action):
    category = 'SETTINGS'
    glyph = 'system/Settings.png'
    
class AXStartMagnifierIntent(_base2):
    name = 'Open Magnifier'
    title = [text('Open Magnifier')]
    
class AXStartGuidedAccessIntent(_base2):
    name = 'Start Guided Access'
    title = [text('Start Guided Access')]
    
class AXStartSpeakScreenIntent(_base2):
    name = 'Start Speak Screen'
    title = [text('Start Speak Screen')]
