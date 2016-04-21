def create_training_sets_trips(feature_function, items):
    featuresets = [(feature_function(key), value) for (key, value) in items]
    third = int(float(len(featuresets)) / 3.0)
    return items[0:third], items[third:third*2], items[third*2:], featuresets[0:third], featuresets[third:third*2], featuresets[third*2:]

train_items, dev_items, test_items, train_features, dev_features, test_features = create_training_sets_trips(f_func, data)

def create_training_sets(feature_function, items):
    featuresets = [(feature_function(key), value) for (key, value) in items]
    halfsize = int(float(len(featuresets)) / 2.0)
    train_set, test_set = featuresets[halfsize:], featuresets[:halfsize]
    return train_set, test_set
train, test = create_training_sets(f_func, data)

from sklearn.naive_bayes import MultinomialNB

cl = nltk.NaiveBayesClassifier.train(train_set)
print "%.3f" % nltk.classify.accuracy(cl, test_set)
cl.show_most_informative_features(40)
cl.prob_classify(featurize(name)) # get a confidence for the prediction

from nltk.classify import SklearnClassifier
from sklearn.svm import SVC
svmc = SklearnClassifier(SVC(), sparse=False).train(train_features)

dtc = nltk.classify.DecisionTreeClassifier.train(train_features, entropy_cutoff=0, support_cutoff=0)  

import numpy
import scipy

from nltk.classify import maxent
nltk.classify.MaxentClassifier.ALGORITHMS
# ['GIS','IIS','CG','BFGS','Powell','LBFGSB','Nelder-Mead','MEGAM','TADM']

# MEGAM or TADM are not rec'd for text classification
mec = nltk.classify.MaxentClassifier.train(train_features, 'GIS', trace=0, max_iter=1000)

from sklearn import cross_validation
cv = cross_validation.KFold(len(train_features), n_folds=10, indices=True, shuffle=False, random_state=None)

for traincv, evalcv in cv:
    classifier = nltk.NaiveBayesClassifier.train(train_features[traincv[0]:traincv[len(traincv)-1]])
    print 'accuracy: %.3f' % nltk.classify.util.accuracy(classifier, train_features[evalcv[0]:evalcv[len(evalcv)-1]])



import sklearn
from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
pipeline = Pipeline([('tfidf', TfidfTransformer()),
                     ('chi2', SelectKBest(chi2, k=2000)),
                     ('nb', MultinomialNB())])
pipecl = SklearnClassifier(pipeline)
pipecl.train(train_features)