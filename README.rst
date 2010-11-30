Pygame Christmas
================

This little project displays an interactive Christmas card written in Python using the Pygame (http://pygame.org) library.

Usage
-----

To start the Christmas card type the following at the console::

    python xmas.py

Keys::

    S - toggle the snow
    M - toggle the music

The project was hacked together in a couple of hours on a Friday evening in preparation for the London Python Code Dojo. The source code is well commented and intended as an example for beginner Pygame developers.

There are three main classes:

* *Flake* - represents an individual snowflake.
* *Snowman* - represents the skating snowman and inherits Pygame's Sprite class.
* *Card* - represents the interactive Christmas card itself, contains the main loop and utility methods for handling various events.

The cards assets can be found in the "data" directory and are all licensed under a copyleft like license - see the sources.txt file therein for more information.

Code Walkthrough
----------------

Commands for moving between the different revisions and viewing the differences::

    git checkout [step1, step2... step7]
    git difftool -t meld step1 step2 -- xmas.py

You'll need the visual diff tool "meld" installed (via a simple apt-get install meld)

Please feel free to expand, extend and modify this software for your own purposes. The code is licensed under the MIT license (found in the source).

Finally, bug reports, comments and enhancements most welcome!

Merry Christmas!

Nicholas.

http://ntoll.org/contact
