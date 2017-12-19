import json

from retrieve.utility import stemmer
from django.db import models
from nltk.corpus import stopwords


class Book(models.Model):
	book_id = models.IntegerField()
	title = models.CharField(max_length=128)
	description = models.TextField(default='-')
	title_wc = models.TextField(default='-')
	desc_wc = models.TextField(default='-')

	def prepare(self):

		stopwords_list = set([stemmer(x) for x in stopwords.words("english")])

		title_wc = {}
		tokens = self.title.lower().split()
		tokens = [stemmer(word) for word in tokens]
		tokens = [word for word in tokens if word not in stopwords_list]
		for word in tokens:
			title_wc[word] = title_wc.get(word, 0) + 1

		desc_wc = {}
		tokens = self.description.lower().split()
		tokens = [stemmer(word) for word in tokens]
		tokens = [word for word in tokens if word not in stopwords_list]
		for word in tokens:
			desc_wc[word] = desc_wc.get(word, 0) + 1

		self.title_wc = json.dumps(title_wc)
		self.desc_wc = json.dumps(desc_wc)

		self.save(update_fields=['title_wc','desc_wc'])

	def dict(self, attr):
		ret = ""

		if attr == 'title':
			ret = self.title_wc
		elif attr == 'desc':
			ret = self.desc_wc

		return json.loads(ret)

class Word(models.Model):
	value = models.CharField(max_length=128)
	title_idf = models.FloatField(default=0)
	desc_idf = models.FloatField(default=0)
	
	def dict(self, attr):
		ret = 0

		if attr == 'title':
			ret = self.title_idf
		elif attr == 'desc':
			ret = self.desc_idf

		return ret