from blog.text_analysis.preparat import PrepText
from blog.text_analysis.gramm import GrammMark
from blog.text_analysis.wateriness import Water
from blog.text_analysis.orfogr import Orthography
from blog.text_analysis.inform import Informativity
from blog.text_analysis.tonalcy import Tonal
from blog.text_analysis.advert import Advert

class Analysis:

    def __init__(self, f):
        self.total = 0
        self.obj = PrepText(f)
        if self.obj.get_flag() == True:
            self.gramm = GrammMark(self.obj).get_mark()
            self.water = Water(self.obj).get_mark()
            self.orth = Orthography(self.obj).get_mark()
            self.info = Informativity(self.obj).get_mark()
            self.ton = Tonal(self.obj).get_mark()
            self.adv = Advert(self.obj).get_mark()

    def analyse(self):
        if self.obj.get_flag() == True:
            print(self.water)
            print(self.gramm)
            print(self.orth)
            print(self.info)
            print(self.ton)
            print(self.adv)
            self.total_mark = (self.water + self.gramm + self.orth + self.info+self.adv*self.ton) / 4
            print("Общая оценка качества текста: %.2f" % self.total_mark)
            return self.gramm, self.water, self.orth, self.info, self.total_mark, self.ton, self.adv
        else:
            self.gramm, self.water, self.orth, self.info, self.total_mark, self.ton, self.adv = 0, 0, 0, 0, 0, 0, 0
            return self.gramm, self.water, self.orth, self.info, self.total_mark, self.ton, self.adv
