from blog.text_analysis.preparat import PrepText
from blog.text_analysis.gramm import GrammMark
from blog.text_analysis.wateriness import Water
from blog.text_analysis.orfogr import Orthography
from blog.text_analysis.inform import Informativity
from blog.text_analysis.tonalcy import Tonal
from blog.text_analysis.neural_imdb_word2vec_using import Word2VecUsage
from blog.text_analysis.neural_imdb_word2vec_training import Word2VecTrain

def analysis(f):
    # w2v_train = Word2VecTrain()
    obj = PrepText(f)
    if obj.get_flag() == True:
        # vocab = obj.get_lsWord()
        gramm = GrammMark(obj)
        water = Water(obj)
        orth = Orthography(obj)
        info = Informativity(obj)
    # o = Word2VecUsage()
    # print("оценка пробная:")
    #print(o.pred("Естественно в фильме, кто главные темы, имеют смертность, ностальгию и потерю невиновности, возможно, не удивительно, что это оценено более высоко зрителями старшего возраста, чем младшие. Однако, есть мастерство и полнота к фильму, которым любой может наслаждаться.","RU"))
    # print(o.pred("Фильм был замечательный"))
        ton = Tonal(obj)
        print(water.get_mark())
        print(gramm.get_mark())
        print(orth.get_mark())
        print(info.get_mark())
    # print(ton.get_mark())
        total_mark = (water.get_mark() + gramm.get_mark() + orth.get_mark() + info.get_mark())/4
        print("Общая оценка качества текста: %.2f" % total_mark)
        total_mark_str = "%.2f" % total_mark
        return gramm,water, orth, info, total_mark_str, ton.get_mark()
    else:
        gramm,water, orth, info, total_mark, ton = 0, 0, 0, 0, 0, 0
        return gramm,water, orth, info, total_mark, ton
