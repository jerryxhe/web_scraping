#!/usr/bin/env python
from abc import ABCMeta,abstractproperty,abstractmethod
import types

__author__="Jerry He"
import re

class OrPattern(BasePattern):
	def __init__(self, pat1, pat2):
		self.pat1=pat1
		self.pat2=pat2
	def __eq__(self, other):
		try:
			return (self.pat1==other or self.pat2==other)
		except:
			return False

class RegExpPattern(BasePattern):
	"""TODO: class-level caching"""
	def __init__(self, pat_str):
		self.re = re.compile(pat_str, re.UNICODE | re.IGNORECASE | re.MULTILINE)
		self.name="_pattern:"+pat_str
	def __eq__(self, sentence_context): 
		if self.re.match(sentence_context):
			return True
		return False

class BasePattern:
	__metaclass__= ABCMeta
	@staticmethod
	def instantiate_the_uninstantiated(self, o):
		if isinstance(o, types.ClassType): # instantiating with all default parameters
			return o()
		return o
	@staticmethod
	def default_text_accessor(self, _dict):
		return _dict['BodyText']
	@abstractmethod
	def __eq__(self, other):
		return False
	def __or__(self, pattern2):
		return OrPattern(self, pattern2)
	def nword(self):
		if hasattr(self, 'nwords'):
			return self.nwords
		return 1
	def _(self):
		return 1
 
