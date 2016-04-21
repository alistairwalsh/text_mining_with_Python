import nltk

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

tokenization_pattern = r'''(?x)    # set flag to allow verbose regexps
([A-Z]\.)+        # abbreviations, e.g. U.S.A.
| \w+(-\w+)*        # words with optional internal hyphens
| \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
| \w+[\x90-\xff]  # these are escaped emojis
| [][.,;"'?():-_`]  # these are separate tokens
'''
word_tokenizer = nltk.tokenize.regexp.RegexpTokenizer(tokenization_pattern)

sentence = '''
We are looking for suitable applicants to fill the positions of Delicatessen Assistant Manager and 
Delicatessen Supervisor at our Edmonton store. 
The applicants must have at least 1 year management/supervisory 
experience in a large Delicatessen Department including strong team leadership qualities.
'''

test_sents = '''
We are looking for suitable applicants to fill the positions of Delicatessen Assistant Manager and 
Delicatessen Supervisor at our Edmonton store. 
The applicants must have at least 1 year management/supervisory 
experience in a large Delicatessen Department including strong team leadership qualities.
'''

train_sents = '''
We are looking for suitable applicants to fill the positions of Delicatessen Assistant Manager and 
Delicatessen Supervisor at our Edmonton store. 
The applicants must have at least 1 year management/supervisory 
experience in a large Delicatessen Department including strong team leadership qualities.
'''

nltk.pos_tag(sentence) # tokenized sentence
nltk.pos_tag(test_sents) 
# nltk.batch_pos_tag(sentences) # for lots of tokenized sentences

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents()
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger.evaluate(test_sents)) # eval the tagger

def build_backoff_tagger(train_sents):
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    t3 = nltk.TrigramTagger(train_sents, backoff=t2)
    return t3
ngram_tagger = build_backoff_tagger(train_sents)

import pickle # or cPickle
with open('pickled_file.pickle', 'wb') as f:
    pickle.dump(ngram_tagger, f)

with open('pickled_file.pickle', 'r') as f:
    tagger = pickle.load(f)

import string
nopunct = [w for w in text if w not in string.punctuation]
' '.join(nopunct[0:100])

from nltk.corpus import stopwords
normalized = [w for w in text6 if w.lower() not in stopwords.words('english')]

from nltk.corpus import stopwords
my_stops = stopwords
my_stops.append("shoebox")

pstemmer = nltk.PorterStemmer()
lstemmer = nltk.LancasterStemmer()
wnlemmatizer = nltk.WordNetLemmatizer()


fd = nltk.FreqDist(data)
fd.plot()
fd.plot(50, cumulative=True)
fd.most_common(12)

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(text)
finder.nbest(bigram_measures.pmi, 10)

technical_term = r"T: {<(JJ|NN|NNS|NNP|NNPS)>+<(NN|NNS|NNP|NNPS|CD)>|<(NN|NNS|NNP|NNPS)>}"
cp = nltk.RegexpParser(technical_term)

# for count, sent in enumerate(brown.sents()[100:104]):
#     print("Sentence #" + str(count) + ":")
#     parsed = cp.parse(nltk.pos_tag(sent))
#     print(parsed)
#     print("\nTechnical Terms:\n")
#     for tree in parsed.subtrees():
#         if tree.label() == "T":
#             print(tree)