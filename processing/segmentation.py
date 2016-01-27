import collections
from itertools import groupby

N = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

"""

Segmentation of data by multiple algorithms,features or properties

"""

def by_bars( C , n_beats=16, beat_axis=4 ):
	"""
	Divide a composition C in bars with N beats,

	Parameters
	----------
	C : 2D array

	n_beats: int , optional (16 by default) length of the bar in beats

	beat_axis : int , optional(4 by default) index of the beat value,
				we assume the data has a regular event structure [I,P,V,D,S,E]

	"""
	if not isinstance(C[0], collections.Sequence):
		raise ValueError( "Events must be a Sequence" )
	if len(C[0])>=beat_axis:
		raise ValueError( "beat_axis is out of range" )

	bars = []
	cbeat = 0
	for e in data:
		cb, s  = divmod( e[beat_axis] , n_beats )
		if cb!=cbeat:
			bars.append([])
			cbeat = cb
		bars[int(cbeat-1)].append( [I,P,V,D,S%n_beats,E%n_beats] )
	return bars

def by_axis( C, axis=0 ):
	"""
	Divide a composition C in subsets which contain one same property

	Parameters
	----------

	C : 2D array

	axis : int, optional( 0 by default) index of the property to be grouped by

	"""
	keyfunc = lambda x:x[axis]
	C = sorted(C, key=keyfunc)
	return [list(j) for i, j in groupby(C,keyfunc)]

