from gensim.models import Word2Vec
from sklearn.externals import joblib
from blog.text_analysis.preparat import PrepText

ADVERT_RF = "blog/text_analysis/classifier_dumps/randomforestTRAINED_advert.pkl"
ADVERT_WORD2VEC_TRAINED = "blog/text_analysis/word2vec_dumps/300features_40minwords_10context_RU_advert"

class Advert:

    def __init__(self, obj):
        self.__value = 0.0
        self.__obj = obj
        self.__txt = obj.get_txt()
        self.__forest = joblib.load(ADVERT_RF)
        self.__model = Word2Vec.load(ADVERT_WORD2VEC_TRAINED)
        self.__num_features = 200 # Размерность векторов в Word2Vec модели

    def __str__(self):
        return "%.2f" % self.get_mark()

    def get_mark(self):
        return self.pred(self.__txt)

    def pred(self, txt):
        return self.__forest.predict(
            PrepText.makeFeatureVec(PrepText.review_to_wordlist(txt), self.__model, self.__num_features))
