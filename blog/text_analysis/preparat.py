import os
import re
import pymorphy2
from collections import OrderedDict
from blog.text_analysis.neural_imdb_word2vec_training import Word2VecTrain


class PrepText:

    def __init__(self, f):
        self.__flag = False
        self.__txt = f
        self.__total_words = 0
        self.__work_file = ""
        self.__file = ""
        self.__morph = pymorphy2.MorphAnalyzer()
        self.__lsWord = {}
        self.__make_dict()

    def __make_dict(self):
        self.__txt.strip("\n")
        # выбираем слова через регулярные выражения
        p, p1 = re.compile("([а-яА-Я-']+)"), re.compile("([!?])")
        res, res1 = p.findall(self.__txt), p1.findall(self.__txt)
        if len(res) > 0:
            self.__flag = True
        # создаем словарь. Ключ-слово, Значение-частота повторения
        # ищем слова
            for key in res:
                if key in self.__lsWord:
                    value = self.__lsWord[key]
                    self.__lsWord[key] = value + 1
                    self.__total_words += 1
                else:
                    self.__lsWord[key] = 1
                    self.__total_words += 1
        # ищем "?" и "!"
            for key in res1:
                key = key.lower()
                if key in self.__lsWord:
                    value = self.__lsWord[key]
                    self.__lsWord[key] = value + 1
                else:
                    self.__lsWord[key] = 1
            self.__normalform()

    def __normalform(self):
        cr = {}
        for key in self.__lsWord:
            words = self.__morph.parse(key)[0].normal_form
            cr[words] = self.__lsWord[key]
        self.__lsWord = OrderedDict(sorted(cr.items()))

    def get_lsWord(self):
        return self.__lsWord

    def get_flag(self):
        return self.__flag

    def get_words(self):
        return Word2VecTrain.review_to_wordlist(self.__txt)

    def get_txt(self):
        return self.__txt

    def get_totalword(self):
        return self.__total_words
