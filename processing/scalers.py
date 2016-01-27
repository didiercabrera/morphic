from __future__ import division
import numpy as np

def normalize(x,max):
	return float(x/max)

def denormalize(x,max):
	return float(x*max)

def rescale( X ,smax ,smin ):
	return [ (x-smin)/(smax - smin) for x in X]

def unit_rescale( X ):
	return [ x/len(X) for x in X ]
