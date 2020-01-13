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

   "Set Switch Control", "✅", "✅"
   "Set LED Flash", "✅", "✅"
   "Set AssistiveTouch", "✅", "✅"
   "Set Audio Descriptions", "✅", "✅"
   "Set Classic Invert", "✅", "✅"
   "Set Smart Invert", "✅", "✅"
   "Set Closed Captions+SDH", "✅", "✅"
   "Set Increase Contrast", "✅", "✅"
   "Set Mono Audio", "✅", "✅"
   "Set Reduce Motion", "✅", "✅"
   "Set Reduce Transparency", "✅", "✅"
   "Set Voice Control", "✅", "✅"
   "Set VoiceOver", "✅", "✅"
   "Set White Point", "✅", "✅"
   "Set Zoom", "✅", "✅"
   "Set Text Size", "✅", "✅"
   "Open Magnifier", "✅", "✅"
   "Start Guided Access", "✅", "✅"

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

   "Encode Media", "✅", "❌", ""
   "Trim Media", "✅", "👁", "06f6587514024a4fa2650ea0011fb61f"
   "Detect Language with Microsoft", "✅", "❌"
   "Translate Text with Microsoft", "✅", "❌"
   "Airdrop", "✅", "👁", ""

**Tests**

   * todo

‎Math
=====

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Number", "✅", "✅", "8ec1111d76ea499daeb11a51f5905bed"
   "Random Number", "✅", "✅", "406710b35d834b5d94abc74250b9df9b"
   "Calculate", "❌", "❌", ""
   "Calculate Statistics", "✅", "✅", "e43107433b084e79aba13187b0a44de1"
   "Round Number", "✅", "✅", "30ccbbbf3dfa4fd28281a60260f52a37"
   "Format File Size", "✅", "❌", ""
   "Format Number", "✅", "❌", ""
   "Convert Measurement", "✅", "❌", "c27de7c1d81444069f6c6b67459ff661"
   "Measurement", "✅", "❌", ""

:TODO: Add exhaustive testing for Convert Measurement

‎Music
======

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Get Current Song", "❌", "❌", ""
   "Play Music", "✅", "✅", "faedd7efe2894db9b99425245906b894"
   "Play/Pause", "✅", "✅", "e7e2790c57434d7eb15ceadfba0172eb"
   "Skip Back", "✅", "✅", "4173f68c3797491c99e1a5d35ad0c273"
   "Skip Forward", "❌", "❌", ""
   "Select Music", "✅", "✅", "06c7737fab6e48ac8f2859366c9883d2"
   "Add to Playlist", "✅", "✅", "92954432e87444a4b009dfa217c18010"
   "Create Playlist", "❌", "❌", ""
   "Get Playlist", "❌", "❌", ""
   "Add to Up Next", "✅", "✅", "51619cdb300742d4ae119ef2888f8b05"
   "Clear Up Next", "✅", "✅", "6f12d879df9b4784be1d1f71d35e24bc"

:TODO: Test with more devices (esp. HomePods) for WFMediaRoute Actions

   * Play/Pause
   * Skip Forwards
   * Skip Back

Maps
======

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Get Distance", "❌", "❌", ""
   "Get Halfway Point", "❌", "❌", ""
   "Search Travel Time", "❌", "❌", ""
   "Street Address", "❌", "❌", ""
   "Get Maps URL", "❌", "❌", ""
   "Show Directions", "❌", "❌", ""
   "Show in Maps", "❌", "❌", ""
   "Search Local Businesses", "❌", "❌", ""
   
Date
======

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50

   "Date", "❌", "❌", ""
   "Format Date", "❌", "❌", ""
   "Adjust Date", "❌", "❌", ""
   "Get Dates from Input", "❌", "❌", ""
   "Get Time Between Dates", "❌", "❌", ""

Documents
=========

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50
   
   "Extract Archive", "❌", "❌", ""
   "Make Archive", "❌", "❌", ""
   "Speak Text", "❌", "❌", ""
   "Markup", "❌", "❌", ""
   "Open In...", "❌", "❌", ""
   "Quick Look", "❌", "❌", ""
   "Make PDF", "❌", "❌", ""
   "Print", "❌", "❌", ""
   "Generate QR Code", "❌", "❌", ""
   "Scan QR/Barcode", "❌", "❌", ""
   "Make Rich Text from Markdown", "❌", "❌", ""
   "Make Rich Text from HTML", "❌", "❌", ""
   "Make HTML from Rich Text", "❌", "❌", ""
   "Make Markdown from Rich Text", "❌", "❌", ""
   "Dictate Text", "❌", "❌", ""
   "Get Name of Emoji", "❌", "❌", ""
   "Show Definition", "❌", "❌", ""
   "Create Folder", "❌", "❌", ""
   "Append to File", "❌", "❌", ""
   "Delete Files", "❌", "❌", ""
   "Get Link to File", "❌", "❌", ""
   "Correct Spelling", "❌", "❌", ""
   "Get File", "❌", "❌", ""
   "Save File", "❌", "❌", ""
   
Safari
=========

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50
   
   "Search Web", "❌", "❌", ""
   "Show Web Page", "❌", "❌", ""
   "Add to Reading List", "❌", "❌", ""
   "Open URLs", "❌", "❌", ""
   "Run JavaScript on Web Page", "❌", "❌", ""
   "Get Contents of Web Page", "❌", "❌", ""
   "Get Article using Safari Reader", "❌", "❌", ""
   
Scripting
=========

.. csv-table::
   :header: "Action", "Class Written", "Test Written", "Test ID"
   :widths: 30, 10, 10, 50
   
   "Exit Shortcut", "❌", "❌", ""
   "Open App", "❌", "❌", ""
   "If", "❌", "❌", ""
   "Choose from Menu", "❌", "❌", ""
   "Repeat", "❌", "❌", ""
   "Repeat with Each", "❌", "❌", ""
   "Wait", "❌", "❌", ""
   "Wait to Return", "❌", "❌", ""
   "Get Battery Level", "❌", "❌", ""
   "Get Device Details", "❌", "❌", ""
   "Set Brightness", "❌", "❌", ""
   "Set Torch", "❌", "❌", ""
   "Dictionary", "❌", "❌", ""
   "Get Dictionary from Input", "❌", "❌", ""
   "Get Dictionary Value", "❌", "❌", ""
   "Set Dictionary Value", "❌", "❌", ""
   "Base64 Encode", "❌", "❌", ""
   "Generate Hash", "❌", "❌", ""
   "Choose from List", "❌", "❌", ""
   "Get Item from List", "❌", "❌", ""
   "List", "❌", "❌", ""
   "Get Current IP Address", "❌", "❌", ""
   "Get Network Details", "❌", "❌", ""
   "Set Do Not Disturb", "❌", "❌", ""
   "Set Airplane Mode", "❌", "❌", ""
   "Set Bluetooth", "❌", "❌", ""
   "Set Mobile Data", "❌", "❌", ""
   "Set Wi-Fi", "❌", "❌", ""
   "Set Low Power Mode", "❌", "❌", ""
   "Nothing", "❌", "❌", ""
   "Count", "❌", "❌", ""
   "Ask for Input", "❌", "❌", ""
   "Play Sound", "❌", "❌", ""
   "Show Alert", "❌", "❌", ""
   "Show Result", "❌", "❌", ""
   "Vibrate Device", "❌", "❌", ""
   "Run Script Over SSH", "❌", "❌", ""
   "Open X-Callback URL", "❌", "❌", ""
   "URL Encode", "❌", "❌", ""

Undocumented
============

Yet to be added as classes

   * Set Appearance
   * 
   * 
   * 
   * 