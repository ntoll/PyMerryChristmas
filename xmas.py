#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A very simple application that draws an interactive Christmas card using the
awesomeness that is Pygame. Much of the code here is based upon the excellent
tutorial written by René Dudfield here:

http://rene.f0o.com/mywiki/PythonGameProgramming

Copyright (c) 2010 Nicholas H.Tollervey.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import pygame
import sys
import os

# Apparently pygame.locals are commonly used constants to include in the global
# namespace
from pygame.locals import *


# Width of the card's window
size_x = 800
# Height of the card's window
size_y = 600


class Card(object):
    """
    Represents an interactive Christmas card, handles the main Pygame loop and
    provides various utility methods
    """

    def __init__(self, caption='Merry Christmas', background='snow.jpg'):
        """
        Caption - game caption
        background - background image
        """
        # initialise various instance variables
        self.caption = caption
        self.background = os.path.join('data', background)
        # pygame setup
        pygame.init()
        self.size = (size_x, size_y)
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(caption)
        self.screen = pygame.display.get_surface()

    def display_card(self):
        """
        Displays the Christmas card and runs the main loop
        """
        # draw the background
        bg_image = pygame.image.load(self.background)
        pygame.display.flip()
        # main game loop
        while True:
            # update the state of the various game "assets" in this loop
            self.update_state(bg_image)
            # handle any input from the user
            self.handle_input(pygame.event.get())
            # display the result
            pygame.display.flip()

    def update_state(self, bg_image):
        """
        Updates the states of the various game "assets" for a loop
        """
        # update the background
        self.screen.blit(bg_image, (0, 0))

    def handle_input(self, events):
        """
        Process input from the user
        """
        for event in events:
            if event.type == QUIT:
                sys.exit(0)


if __name__ == "__main__":
    card = Card()
    card.display_card()
