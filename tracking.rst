=========
Shortcuts
=========

A complete action must have:

   * set ``name``, ``category``, ``glyph``
   * ``title`` or ``lines`` where applicable
   * tests

Key

   * ✅ Complete
   * ❌ Not Yet Complete
   * 👁 Visual Check Only (for simple actions)

Accessibility
=============

.. csv-table::
   :header: "Action", "Class Written", "Tests Written"
   :widths: 40, 20, 20

   "Set Switch Control",      "✅", "✅"
   "Set LED Flash",           "✅", "✅"
   "Set AssistiveTouch",      "✅", "✅"
   "Set Audio Descriptions",  "✅", "✅"
   "Set Classic Invert",      "✅", "✅"
   "Set Smart Invert",        "✅", "✅"
   "Set Closed Captions+SDH", "✅", "✅"
   "Set Increase Contrast",   "✅", "✅"
   "Set Mono Audio",          "✅", "✅"
   "Set Reduce Motion",       "✅", "✅"
   "Set Reduce Transparency", "✅", "✅"
   "Set Voice Control",       "✅", "✅"
   "Set VoiceOver",           "✅", "✅"
   "Set White Point",         "✅", "✅"
   "Set Zoom",                "✅", "✅"
   "Set Text Size",           "✅", "✅"
   "Open Magnifier",          "✅", "✅"
   "Start Guided Access",     "✅", "✅"

**Tests**

   * 3bc77e514fb241939e0111349aa3718a
   * 1d3f4f25d7a8451c8a453a9b66fc85e4
   * f3970902f90f48ba991fb4e76743920e
   * 458086c486fd485cbf1917a06e2c09cd
   * d50d574d94c74434ac8307dffdfbcfe1

‎Miscellaneous
==============

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Encode Media",                   "✅", "❌", ""
   "Trim Media",                     "✅", "👁", "06f6587514024a4fa2650ea0011fb61f"
   "Detect Language with Microsoft", "✅", "❌"
   "Translate Text with Microsoft",  "✅", "❌"
   "Airdrop",                        "✅", "👁", ""

**Tests**

   * todo

‎Math
=====

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Number",               "✅", "✅", "8ec1111d76ea499daeb11a51f5905bed"
   "Random Number",        "✅", "✅", "406710b35d834b5d94abc74250b9df9b"
   "Calculate",            "❌", "❌", ""
   "Calculate Statistics", "✅", "✅", "e43107433b084e79aba13187b0a44de1"
   "Round Number",         "✅", "✅", "30ccbbbf3dfa4fd28281a60260f52a37"
   "Format File Size",     "✅", "❌", ""
   "Format Number",        "✅", "❌", ""
   "Convert Measurement",  "✅", "❌", "c27de7c1d81444069f6c6b67459ff661"
   "Measurement",          "✅", "❌", ""

:TODO: Add exhaustive testing for Convert Measurement

‎Music
======

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Get Current Song", "✅", "👁", "06bc19b5a33d40d983f16939ccf9cf4d"
   "Play Music",       "✅", "✅", "faedd7efe2894db9b99425245906b894"
   "Play/Pause",       "✅", "✅", "e7e2790c57434d7eb15ceadfba0172eb"
   "Skip Back",        "✅", "✅", "4173f68c3797491c99e1a5d35ad0c273"
   "Skip Forward",     "✅", "👁", "1bacfe061a7c48599e7297ee6b35a6bc"
   "Select Music",     "✅", "✅", "06c7737fab6e48ac8f2859366c9883d2"
   "Add to Playlist",  "✅", "✅", "92954432e87444a4b009dfa217c18010"
   "Create Playlist",  "✅", "👁", "22795e014347497fb01f7bab5d1a0444"
   "Get Playlist",     "✅", "✅", "aea1999225dc49a38038521ccf350089"
   "Add to Up Next",   "✅", "✅", "51619cdb300742d4ae119ef2888f8b05"
   "Clear Up Next",    "✅", "✅", "6f12d879df9b4784be1d1f71d35e24bc"

:TODO: Test with more devices (esp. HomePods) for WFMediaRoute Actions

   * Play/Pause
   * Skip Forwards
   * Skip Back

Maps
======

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Get Distance",            "✅", "❌", "8f151110492b4a778a2d77cd62f281a2"
   "Get Halfway Point",       "✅", "❌", "be758e00b6ec471d976dcd48a2557cc0"
   "Search Travel Time",      "✅", "❌", "3616d9b19d564a4381fd4a7f3215cbcf"
   "Street Address",          "✅", "❌", "129b944bf99e4fcea68311061d723daf"
   "Get Maps URL",            "✅", "❌", "a27426b0a14b443f84989a2ab4cb6870"
   "Show Directions",         "✅", "❌", "de0bb2a9674a4034ad40e95408589777"
   "Show in Maps",            "✅", "❌", "4f23ca28d0c143b38738c2dc04e9948c"
   "Search Local Businesses", "❌", "❌", ""
   
Street Address
   * leftify formatting appears to be failing (appears properly propogated to CSS)
   * the `Country` line should default to the device country, I'm ignoring this

`Search Local Businesses` implements a Health-like line-measurement system. Come back to it later.

Date
======

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Date",                   "✅", "👁", "69dacb21242f4b8dabfa5de9636090e9"
   "Format Date",            "❌", "❌", ""
   "Adjust Date",            "❌", "❌", ""
   "Get Dates from Input",   "❌", "❌", ""
   "Get Time Between Dates", "✅", "❌", "3253ab06ee3d4fd6b68ee1365266c0a5"

`Format Date` has a default value in it's inline field. Not currently accounted for.

Documents
=========

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50
   
   "Extract Archive",              "✅", "❌", "e4d3e034b2eb490590bee504b8182e77"
   "Make Archive",                 "✅", "❌", "009a06cf07a842278ada7daa756ea1c1"
   "Speak Text",                   "❌", "❌", ""
   "Markup",                       "✅", "❌", "b94b90fcf41f40a697ef51afd381b226"
   "Open In...",                   "✅", "❌", "115e458dac0c4dea886228ff9b09400c"
   "Quick Look",                   "✅", "❌", "ce4d2a5bffcc44909554d57dc0c276e7"
   "Make PDF",                     "✅", "❌", "641dfddc93ea47babe6bd505c1350093"
   "Print",                        "✅", "❌", "f48382f13c4c448c8f567936f704c53f"
   "Generate QR Code",             "✅", "❌", "dc8a38bb8dc44ddc8d8a40c4f605e31b"
   "Scan QR/Barcode",              "✅", "👁", "d920c5ae8aec4011b87aa7cc99e6e0ab"
   "Make Rich Text from Markdown", "❌", "❌", ""
   "Make Rich Text from HTML",     "❌", "❌", ""
   "Make HTML from Rich Text",     "❌", "❌", ""
   "Make Markdown from Rich Text", "❌", "❌", ""
   "Dictate Text",                 "❌", "❌", ""
   "Get Name of Emoji",            "❌", "❌", ""
   "Show Definition",              "❌", "❌", ""
   "Create Folder",                "❌", "❌", ""
   "Append to File",               "❌", "❌", ""
   "Delete Files",                 "❌", "❌", ""
   "Get Link to File",             "❌", "❌", ""
   "Correct Spelling",             "❌", "❌", ""
   "Get File",                     "❌", "❌", ""
   "Save File",                    "❌", "❌", ""
   
`Make Archive` stores `Format` without the leading `.`. Need to account for this when encoding the Shortcut.

`Open In...` needs to have an App selector, as well as support for decoding app URLs. Needs further testing.

Safari
=========

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50
   
   "Search Web",                      "❌", "❌", ""
   "Show Web Page",                   "❌", "❌", ""
   "Add to Reading List",             "❌", "❌", ""
   "Open URLs",                       "❌", "❌", ""
   "Run JavaScript on Web Page",      "❌", "❌", ""
   "Get Contents of Web Page",        "❌", "❌", ""
   "Get Article using Safari Reader", "❌", "❌", ""
   
Scripting
=========

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50
   
   "Exit Shortcut",             "❌", "❌", ""
   "Open App",                  "❌", "❌", ""
   "If",                        "❌", "❌", ""
   "Choose from Menu",          "❌", "❌", ""
   "Repeat",                    "❌", "❌", ""
   "Repeat with Each",          "❌", "❌", ""
   "Wait",                      "❌", "❌", ""
   "Wait to Return",            "❌", "❌", ""
   "Get Battery Level",         "❌", "❌", ""
   "Get Device Details",        "❌", "❌", ""
   "Set Brightness",            "❌", "❌", ""
   "Set Torch",                 "❌", "❌", ""
   "Dictionary",                "❌", "❌", ""
   "Get Dictionary from Input", "❌", "❌", ""
   "Get Dictionary Value",      "❌", "❌", ""
   "Set Dictionary Value",      "❌", "❌", ""
   "Base64 Encode",             "❌", "❌", ""
   "Generate Hash",             "❌", "❌", ""
   "Choose from List",          "❌", "❌", ""
   "Get Item from List",        "❌", "❌", ""
   "List",                      "❌", "❌", ""
   "Get Current IP Address",    "❌", "❌", ""
   "Get Network Details",       "❌", "❌", ""
   "Set Do Not Disturb",        "❌", "❌", ""
   "Set Airplane Mode",         "❌", "❌", ""
   "Set Bluetooth",             "❌", "❌", ""
   "Set Mobile Data",           "❌", "❌", ""
   "Set Wi-Fi",                 "❌", "❌", ""
   "Set Low Power Mode",        "❌", "❌", ""
   "Nothing",                   "❌", "❌", ""
   "Count",                     "❌", "❌", ""
   "Ask for Input",             "❌", "❌", ""
   "Play Sound",                "❌", "❌", ""
   "Show Alert",                "❌", "❌", ""
   "Show Result",               "❌", "❌", ""
   "Vibrate Device",            "❌", "❌", ""
   "Run Script Over SSH",       "❌", "❌", ""
   "Open X-Callback URL",       "❌", "❌", ""
   "URL Encode",                "❌", "❌", ""

Undocumented
============

Yet to be added as classes

   * Set Appearance
   * 
   * 
   * 
   * 