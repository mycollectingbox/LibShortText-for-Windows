#!/usr/bin/env python

from ctypes import *
from ctypes.util import find_library
import sys
import os
import platform

platformName = platform.system()

if platformName == 'Windows':
	if sizeof(c_voidp) == 4:
		stemmer = CDLL(os.path.join(os.path.dirname(__file__),'./porter_x86.dll'))
	elif sizeof(c_voidp) == 8:
		try:
			stemmer = CDLL(os.path.join(os.path.dirname(__file__),'./porter_x64.dll'))
		except:
			stemmer = CDLL(os.path.join(os.path.dirname(__file__),'./porter_x64_MT.dll'))
elif platformName == 'Linux':
	stemmer = CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), './porter.so.1'))
elif platformName == 'Darwin':
	stemmer = CDLL(os.path.join(os.path.abspath(os.path.dirname(__file__)), './porter.so.1'))

def fillprototype(f, restype, argtypes): 
	f.restype = restype
	f.argtypes = argtypes

fillprototype(stemmer.trim, c_int, [c_char_p])

def stem(word):
	return word[:stemmer.trim(word.encode('utf-8'))]
