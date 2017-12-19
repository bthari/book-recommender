import string, math
from nltk.stem.snowball import SnowballStemmer

def stemmer(word):

	tmp_word = word

	translation = str.maketrans("","", string.punctuation);

	tmp_word.translate(translation)

	stemmer = SnowballStemmer("english")

	return stemmer.stem(tmp_word)

def count_idf(collection_size, count):
	upper_hand = math.log( collection_size / count )
	lower_hand = math.log(10)

	idf = upper_hand / lower_hand

	return idf