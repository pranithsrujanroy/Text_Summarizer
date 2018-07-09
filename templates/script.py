# print("1:")
import nltk
import string
from lxml import html
import requests
from readability import Document
from urllib import request
import re
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
response = requests.get("https://en.wikipedia.org/wiki/Louis_Tomlinson")
tree = html.fromstring(response.content)
doc = Document(response.text)
# print(doc.title())
tree_text = tree.xpath('//p/text() | //p/a/text() |//p/b/text() | //div/text() | //h2/text() | //h1/text() | //h2/a/text() | //h3/text() | //h3/a/text()')
# tree_text = tree.xpath('//div/text()')
# print(tree_text)
# response=request.urlopen("https://en.wikipedia.org/wiki/Louis_Tomlinson")
# print("URL:",response.geturl())

# print("2:")
text=""
file=open('text_with_b.txt','w+')
for x in tree_text:
    if("'b'" in x):
        x.strip("'b'")
    file.write(str(x.encode("utf-8")))
file.close()

# print("3:")
s0='"b"'
s1="'b'"
s2="'b"
s3="b'"
# print(set(string.printable))
# pattern = "\"(?=[<\"]+,)[>\"]+\""
with open('text_with_b.txt', 'r') as infile, \
     open('text_document.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace(s0,"")
    data = data.replace(s1, "")
    data = data.replace(s2, "")
    data = data.replace(s3, "")
    outfile.write(data)
infile.close()
outfile.close()

# starting summarizer 
# print("4:")
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import copy

class FrequencySummarizer:
  def __init__(self, min_cut=0.1, max_cut=0.9):
    """
     Initilize the text summarizer.
     Words that have a frequency term lower than min_cut 
     or higer than max_cut will be ignored.
    """
    self._min_cut = min_cut
    self._max_cut = max_cut 
    self._stopwords = set(stopwords.words('english') + list(punctuation))

  def _compute_frequencies(self, word_sent):
    """ 
      Compute the frequency of each of word.
      Input: 
       word_sent, a list of sentences already tokenized.
      Output: 
       freq, a dictionary where freq[w] is the frequency of w.
    """
    freq = defaultdict(int)
    for s in word_sent:
      for word in s:
        if word not in self._stopwords:
          freq[word] += 1
    # frequencies normalization and fitering
#     print(freq)
    m = float(max(freq.values()))
    freq_words = copy.deepcopy(freq)
    for w in freq.keys():
      freq[w] = freq[w]/m
      freq_words[w] = freq_words[w]/m
      if freq[w] >= self._max_cut or freq[w] <= self._min_cut:
        del freq_words[w]
    return freq_words

  def summarize(self, text, n):
    """
      Return a list of n sentences 
      which represent the summary of text.
    """
    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = [word_tokenize(s.lower()) for s in sents]
    self._freq = self._compute_frequencies(word_sent)
    ranking = defaultdict(int)
    for i,sent in enumerate(word_sent):
      for w in sent:
        if w in self._freq:
          ranking[i] += self._freq[w]
    sents_idx = self._rank(ranking, n)    
    return [sents[j] for j in sents_idx]

  def _rank(self, ranking, n):
    """ return the first n sentences with highest ranking """
    return nlargest(n, ranking, key=ranking.get)

# print("5:")
print(doc.title())
print()
fs = FrequencySummarizer()
f=open('result.txt','w+')
with open("text_document.txt","r") as file:
    text=file.read()
    for s in fs.summarize(text,4):
        f.write(str('*'+s))
        print()
f.close()