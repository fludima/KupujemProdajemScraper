import pickle

# pickle highest performance object conversion into a bytestream 
# used to pickle n unpickle (i.e. save/load)
def save(file, filename='file'):
    with open(f'{filename}.pickle', 'wb') as f:
        pickle.dump(file, f, protocol=pickle.HIGHEST_PROTOCOL)


def load(filename):
	with open(f'{filename}.pickle', 'rb') as f:
		return pickle.load(f) 
    
