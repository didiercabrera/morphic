from __future__ import division

def normalize(x,max):
	return float(x/max)

def denormalize(x,max):
	return float(x*max)

def rescale( data_set ,smax ,smin ):
	return [ (x-smin)/(smax - smin) for x in data_set]

def unit_rescale( data_set ):
	return [ (x/len(data_set)) for x in data_set ]
