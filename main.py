# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 01:39:57 2021

@author: sammy
"""

from subprocess import Popen
import time
Popen('python voice.py')
time.sleep(1)
Popen('python connect4.py')