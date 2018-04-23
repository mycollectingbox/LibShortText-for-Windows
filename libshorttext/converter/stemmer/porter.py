#!/usr/bin/env python

from ctypes import *
from ctypes.util import find_library
import sys
import os

if sizeof(c_voidp) == 4:
	stemmer = CDLL(os.path.join(os.path.dirname(__file__),'./porter.dll'))  # './porter.so.1'
elif sizeof(c_voidp) == 8:
	stemmer = CDLL(os.path.join(os.path.dirname(__file__),'./x64/porter.dll'))  # './porter.so.1'

def fillprototype(f, restype, argtypes): 
	f.restype = restype
	f.argtypes = argtypes

fillprototype(stemmer.trim, c_int, [c_char_p])

def stem(word):
	return word[:stemmer.trim(word.encode('utf-8'))]
