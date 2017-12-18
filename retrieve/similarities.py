import numpy as np
import json
from nltk.stem.snowball import SnowballStemmer

# cosine similarity given 2 arrays
def cosine_similarity(arr1, arr2):

	q1 = np.array(arr1)
	q2 = np.array(arr2)

	if(len(arr1) > len(arr2)):
		q2_tmp = np.zeros(q1.shape)
		q2_tmp[:q2.shape[0]] = q2
		q2 = q2_tmp
	elif(len(arr2) > len(arr1)):
		q1_tmp = np.zeros(q2.shape)
		q1_tmp[:q1.shape[0]] = q1
		q1 = q1_tmp

	dot = np.dot(q1,q2)
	mag = np.linalg.norm(q1)*np.linalg.norm(q2)

	return dot/mag

def prepare_document_vector():
	pass

def prepare_query_vector():
	pass

def get_weight(word):
	pass

def find_similar_title(query, collection):

	result = []
	stemmer = SnowballStemmer("english")

	query_title = query.lower()
	
	for item in collection:
		if query_title == item.title:
			result.append(item.title)
			return result

	query_vector = string_to_vector(query_title, stemmer)
	rank = []
	for item in collection:
		item_vector = item.title_wc

		v1 = [x[1] for x in query_vector]
		v2 = [item_vector[word] for (word,count) in query_vector]

		similarity = cosine_similarity(v1, v2)
		rank.append((item.title, similarity))

	result = sorted(rank, key = lambda x : x[1], reverse = True)[:3]

	return result

def find_similar_desc(query, collection):
	
	result = []
	stemmer = SnowballStemmer("english")

	query_desc = query.lower()
	
	query_vector = string_to_vector(query_desc, stemmer)
	rank = []
	for item in collection:
		item_vector = item.title_wc

		v1 = [x[1] for x in query_vector]
		v2 = [	(item_vector[word] * get_weight(x))
				for (word,count) in query_vector
			 ]

		similarity = cosine_similarity(v1, v2)
		rank.append((item.title, similarity))

	result = sorted(rank, key = lambda x : x[1], reverse = True)[:3]

	return result

def string_to_vector(query, stemmer):


	string_array = [stemmer.stem(x) for x in query.split()]
	return [	(x,string_array.count(x) * get_weight(x)) 
				for x in set(string_array)
			]



# Isi collection
# 
# books
# 	- title
# 	- description
# 	- genre (?)
# 	- title_wc (word count, dictionary)
# 	- desc_wc (word count, dictionary)
#
# weight_dictionary (per word, dictionaru=y)