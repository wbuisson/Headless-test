#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep, ctime
from collections import namedtuple
from threading import Thread
from os.path import isfile
import csv

SOUNDCLOUD_LIKES='https://soundcloud.com'

class Soundcloud_w():
    def __init__(self):
        # Create a headless browser
        opts = Options()
        #opts.set_headless()     
        self.browser = Chrome(options=opts)
        self.browser.get(SOUNDCLOUD_LIKES)

        # Track list related state
        self._current_track_number = 1

    def play(self,track=None):
        '''
        Play a track. If no track number is supplied, the presently selected track
        will play.
        '''
        self.browser.execute_script("arguments[0].click();", self.browser.find_element_by_class_name('playControl'))
            
    def pause(self):
        '''
        Pauses the playback
        '''
        self.play()
    
    def close_w(self):
        '''
        Closes the the Chrome Soundcloud window
        '''
        self.browser.quit()
