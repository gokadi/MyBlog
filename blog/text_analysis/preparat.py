import re
import pymorphy2
from collections import OrderedDict
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import numpy as np

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

    def get_words(self):  # используется для проверки на водность и орфографию, т.к. в частотном словаре нет повторений
        return self.review_to_wordlist(self.__txt)

    def get_txt(self):
        return self.__txt

    def get_totalword(self):
        return self.__total_words

    @staticmethod # Делим анализируемый текст на список слов
    def review_to_wordlist(review, remove_stopwords=False):
        # Делим преложение на список слов (list of words)
        # 1. Очистка от html тегов и URLов
        review = re.sub(r'^https?:\/\/.*[\r\n]*', '', review, flags=re.MULTILINE)
        review_text = BeautifulSoup(review, "html.parser").get_text()
        # 2. Оставить только буквы
        review_text = re.sub("[^а-яА-Я]", " ", review_text)
        # 3. Привести текст к нижнему регистру и разделить на слова
        words = review_text.lower().split()
        # 4. Удалить стоп слова (по флагу)
        if remove_stopwords:
            # stops = set(stopwords.words("english"))
            stops = set(stopwords.words("russian"))
            words = [w for w in words if not w in stops]
        # 5. Вернуть список слов
        return (words)

    @staticmethod # Представляем текст (в виде списка слов) в виде чисел (усредненный вектор по всем словам в тексте)
    def makeFeatureVec(words, model, num_features):
        # Усредняем вектора для всех слов в обзоре
        # Инициализируем массив
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0.
        # Index2word - список, содержащий слова из словаря модели. Конвертируем в set
        index2word_set = set(model.wv.index2word)
        # Для всех слова в обзоре, если они в словаре, суммируем вектора
        for word in words:
            if word in index2word_set:
                nwords = nwords + 1.
                featureVec = np.add(featureVec, model[word])
        # Усредняем получившийся вектор
        featureVec = np.divide(featureVec, nwords)
        return featureVec