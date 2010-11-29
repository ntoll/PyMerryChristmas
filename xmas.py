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
import random

# Apparently pygame.locals are commonly used constants to include in the global
# namespace
from pygame.locals import *


# Just so people know...
if not pygame.font:
    print 'Warning, fonts disabled'


# Width of the card's window
size_x = 800
# Height of the card's window
size_y = 600


class Flake(object):
    """
    Represents a circular snowflake (yeah, I know)

    Based upon code found here: http://www.tolchz.net/?p=29
    """

    def __init__(self):
        """
        Set up a whole load of attributes about the snowflake
        """
        # start x position
        self.x = random.randrange(size_x)
        # start y position
        self.y = - random.randrange(100)
        # drift x (amount of change each loop along the x axis)
        self.dx = random.randrange(3) - random.randrange(6)
        # drift y (amount of change each loop along the y axis)
        self.dy = random.randrange(1, 20) + random.randrange(4)
        # the size of the circular snowflake
        self.size = random.randrange(1, 4)
        # the colour of the snowflake (from sludgy grey to snowy white)
        c = random.randrange(200, 256)
        self.color = [c, c, c]

    def draw(self, screen):
        """
        Create a circular representation of the snowflake on the screen
        """
        # Snow is circular in this case... ;-)
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)),
            self.size)
        # now update things for the next loop
        # update the x position
        self.x += self.dx
        # update the y position
        self.y += self.dy
        # bounds checking
        if self.x < 0 or self.x > size_x:
            # floated off the edge of the screen so do a reset
            self.x = random.randrange(size_x)
            self.y = 0
            self.dy = random.randrange(1, 30) + random.random()
        if (self.y > size_y):
            # floated off the bottom of the screen so drift again from the top
            self.x = random.randrange(size_x)
            self.y = 0
            self.dy = random.randrange(1, 30) + random.random()


class Card(object):
    """
    Represents an interactive Christmas card, handles the main Pygame loop and
    provides various utility methods
    """

    def __init__(self, caption='Merry Christmas', background='snow.jpg',
        intensity=100):
        """
        Caption - game caption
        background - background image
        intensity - the number of snowflakes to display
        """
        # initialise various instance variables
        self.caption = caption
        self.background = os.path.join('data', background)
        self.intensity = intensity
        # pygame setup
        pygame.init()
        self.size = (size_x, size_y)
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(caption)
        self.screen = pygame.display.get_surface()
        # let it snow, let it snow, let it snow... :-)
        self.let_it_snow(self.intensity)

    def display_card(self):
        """
        Displays the Christmas card and runs the main loop
        """
        # draw the background
        bg_image = pygame.image.load(self.background)
        pygame.display.flip()
        # draw the greeting
        self.draw_greeting()
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
        # update the greeting
        self.draw_greeting()
        # draw some snow
        for s in self.snow:
            s.draw(self.screen)

    def let_it_snow(self, intensity=100):
        """
        Initialises a snowstorm
        """
        self.snow = []
        for i in range(intensity):
            self.snow.append(Flake())

    def draw_greeting(self):
        """
        Draw the greeting onto the screen
        """
        if pygame.font:
            # grab the correct font
            font = pygame.font.Font(None, 120) # fontname, size
            # render the font into the "text" surface
            # text, antialias, color
            text = font.render(self.caption, 1, (200, 50, 100))
            # center the text
            textpos = text.get_rect()
            textpos.centerx = self.screen.get_rect().centerx
            # render to screen
            self.screen.blit(text, textpos)

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
