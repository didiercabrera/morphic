'''
Segmentation of data by multiple algorithms,features or properties


'''




def by_beats( data, n_beats=16 ):
	'''
	Split a track in chunks of length = n_beats
	'''
	chunks = []
	cbeat = 0
	for e in data:
		I,P,V,D,S,E  = e
		cb, s  = divmod(S,n_beats)
		if cb!=cbeat:
			chunks.append([])
			cbeat = cb
		chunks[int(cbeat-1)].append( [I,P,V,D,S%n_beats,E%n_beats] )
	return chunks


def by_instrument():
	pass