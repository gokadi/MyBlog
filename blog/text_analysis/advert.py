from blog.text_analysis.neural_imdb_word2vec_using import Word2VecUsage

class Advert:

    def __init__(self, obj):
        self.__value = 0.0
        self.__obj = obj
        self.__txt = obj.get_txt()

    def get_mark(self):
        o = Word2VecUsage()
        return 1 - o.pred(self.__txt)

    def __str__(self):
        return "%.2f" % self.get_mark()
