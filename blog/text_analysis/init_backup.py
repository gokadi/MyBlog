from blog.text_analysis.preparat import PrepText
from blog.text_analysis.gramm import GrammMark
from blog.text_analysis.wateriness import Water
from blog.text_analysis.orfogr import Orthography
from blog.text_analysis.inform import Informativity
from blog.text_analysis.tonalcy import Tonal
from blog.text_analysis.neural_imdb_word2vec_using import Word2VecUsage
from blog.text_analysis.neural_imdb_word2vec_training import Word2VecTrain

class Analysis:

    def __init__(self, f):
        self.progress = 0
        self.total = 0
        self.obj = PrepText(f)
        if self.obj.get_flag() == True:
            self.gramm = GrammMark(self.obj)
            self.water = Water(self.obj)
            self.orth = Orthography(self.obj)
            self.info = Informativity(self.obj)
            self.ton = Tonal(self.obj)

    def analyse(self):
        # w2v_train = Word2VecTrain()
        # obj = PrepText(f)
        if self.obj.get_flag() == True:
        #     # vocab = obj.get_lsWord()
        #     gramm = GrammMark(obj)
        #     water = Water(obj)
        #     orth = Orthography(obj)
        #     info = Informativity(obj)
        #     # o = Word2VecUsage()
        #     # print("оценка пробная:")
        #     # print(o.pred("Естественно в фильме, кто главные темы, имеют смертность, ностальгию и потерю невиновности, возможно, не удивительно, что это оценено более высоко зрителями старшего возраста, чем младшие. Однако, есть мастерство и полнота к фильму, которым любой может наслаждаться.","RU"))
        #     # print(o.pred("Фильм был замечательный"))
        #     ton = Tonal(obj)
            print(self.water)
            print(self.gramm)
            print(self.orth)
            print(self.info)
            print(self.ton)
            self.total_mark = (self.water + self.gramm + self.orth + self.info) / 4
            print("Общая оценка качества текста: %.2f" % self.total_mark)
            self.total_mark_str = "%.2f" % self.total_mark
            return self.gramm, self.water, self.orth, self.info, self.total_mark_str, self.ton
        else:
            self.gramm, self.water, self.orth, self.info, self.total_mark, self.ton = 0, 0, 0, 0, 0, 0
            return self.gramm, self.water, self.orth, self.info, self.total_mark, self.ton

    def proceed(self):
        progress, totalsize = self.ton.proceed_class().get_progress()
        return progress, totalsize


