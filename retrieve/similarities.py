import numpy as np
import json, math

from nltk.corpus import stopwords
from retrieve.models import Book, Word
from retrieve.utility import stemmer, count_idf
from django.core.exceptions import ObjectDoesNotExist

# done
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

# done
def prepare_document_vector():

	collection_size = Book.objects.all().count()
	collection_count_title = {}
	collection_count_desc = {}

	for item in Book.objects.all():
		item.prepare()
		
		for word in item.dict('desc').keys():
			collection_count_desc[word] = collection_count_desc.get(word,0) + 1

		for word in item.dict('title').keys():
			collection_count_title[word] = collection_count_title.get(word,0) + 1


	for (word, count) in collection_count_desc.items():

		idf = count_idf(collection_size, count)
		new_word = Word(value=word, desc_idf=idf)
		new_word.save()

	for (word, count) in collection_count_title.items():

		idf = count_idf(collection_size, count)
		update_word = None

		try:
			update_word = Word.objects.get(value=word)
			update_word.title_idf = idf
		except ObjectDoesNotExist:
			update_word = Word(value=word, title_idf=idf)
		finally:
			update_word.save()

#done
def get_weight(word, attr):
	
	ret = 0

	try:
		found = Word.objects.get(value=word)
		ret = found.dict(attr)[word]
	except ObjectDoesNotExist:
		pass
	
	return ret


def find_similar_title(query):

	query_title = query.lower()
	
	for item in Book.objects.all():
		if query_title == item.title:
			ret += "{books:[{ title:{}, desc:{} \}]".format(book.title, book.description)

	query_vector = string_to_vector(query_title, stemmer)
	rank = []
	for item in collection:
		item_vector = item.title_wc

		v1 = [x[1] for x in query_vector]
		v2 = [item_vector[word] for (word,count) in query_vector]

		similarity = cosine_similarity(v1, v2)
		rank.append((item.book_id, similarity))

	result = sorted(rank, key = lambda x : x[1], reverse = True)[:3]

	ret = "{books:["
	for item in result:
		book = Book.objects.get(book_id=item[0])
		ret += "\{ title:{}, desc:{} \},".format(book.title, book.description)

	ret += "]}"

	return ret

def find_similar_desc(query):
	
	query_desc = query.lower()
	
	query_vector = string_to_vector(query_desc)
	rank = []
	for item in Book.objects.all():
		item_vector = item.title_wc

		v1 = [x[1] for x in query_vector]
		v2 = [	(item_vector[word] * get_weight(word, 'desc'))
				for (word,count) in query_vector
			 ]

		similarity = cosine_similarity(v1, v2)
		rank.append((item.book_id, similarity))

	result = sorted(rank, key = lambda x : x[1], reverse = True)[:3]

	ret = "{books:["
	for item in result:
		book = Book.objects.get(book_id=item[0])
		ret += "\{ title:{}, desc:{} \},".format(book.title, book.description)

	ret += "]}"
	return ret

def string_to_vector(query):

	stopwords_list = set(stopwords.words("english"))

	string_array = [stemmer(x) for x in query.split() if x not in stopwords_list]
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