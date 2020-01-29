======
Editor
======

**Goal**: Make a web based Shortcuts editor that
matches or exceeds the native iOS one.

Inline Variables
================

Magic String
   * Representation of inline field
   * Magic Variables replaced with ``$()`` syntax,
      * Ask Each Time (or whatever the ask text is) becomes $(Ask Each Time)
      * Clipboard, Shortcut Input, Current Date are similarly represented

Edit Engine
   * when user clicks, dump text and inline variables as a magic string
      * Magic Variables must have their information stored somewhere
      * information: UUID, glyph
   * parse a magic string, represent it in as HTML

Reverse Visualization Engine (not yet planned out)
   * turns HTML back into JSON or plist

Other Details
   * Magic Vars should turn RED if the originating action
     is missing or later in the flow
