import re
import os
import string
import functools
from itertools import product
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
cities = os.path.join(THIS_FOLDER, 'stopcity.txt')    # stopcity - файл содержащий список городов
with open(cities) as file:
    cities = file.read()

"""wordside - библиотека для работы с текстом
   Существующие проблемы:
"""
class wordside(object):
    def modifier(words, type):
        """Функция получает набор данных от пользователя, чистит данные от лишних символов и выводит список строк по слову в строке.
        Параметр type содержит информацию о том, какие символы удалять.
        Тип удаляемых символов передаётся в переменную type без пробелов в виде 'quotesplusprepconj'
        !!!Нужно обратить внимание, что при удалении всех знаков пунктуации или минусов удаляются дефисы в словах.!!!
        """
        marks = ''
        result = []
        if 'punct' in type:                               # Удаление всех знаков пунктуации
            marks += string.punctuation + '\r'
        if 'quotes' in type:                              # Удаление всех видов кавычек
            marks += '[“”‘«»„“]'
        if 'exclamation_mark' in type:                    # Удаление восклицательных знаков
            marks += '!'
        if 'space' in type:                               # Удаление пробелов и знаков табуляции
            marks += '   '
        if 'plus' in type:                                #Удаление знаков плюс
            marks += '+'
        if 'minus' in type:                               #Удаление знаков минус
            marks += '-'
        if 'prep' in type:                                # Удаление предлогов
            for word in words.strip().split(' '):
                if morph.parse(word)[0].tag.POS == 'PREP':
                    words.replace(word, '')
        if 'npro' in type:                                # Удаление местоимений-существительных
            for word in words.strip().split(' '):
                if morph.parse(word)[0].tag.POS == 'NPRO':
                    words.replace(word, '')
        if 'conj' in type:                                # Удаление союзов
            for word in words.strip().split(' '):
                if morph.parse(word)[0].tag.POS == 'CONJ':
                    words.replace(word, '')
        if 'prcl' in type:                                # Удаление частиц
            for word in words.strip().split(' '):
                if morph.parse(word)[0].tag.POS == 'PRCL':
                    words.replace(word, '')
        if 'intj' in type:                                # Удаление междометий
            for word in words.strip().split(' '):
                if morph.parse(word)[0].tag.POS == 'INTJ':
                    words.replace(word, '')
    
        if marks != '':
            words = re.sub('[{}]'.format(re.escape(marks)), '', words) # Удаление символов
        else:
            return 'Введите тип удаляемых символов'
        words = list(words.lower().split(' '))
        if words[-1] == '':
            words.remove(words[-1])
        if 'pass' in type:                                # Удаление пустых строк
            while '' in words:
                words.remove('')
        if 'dub' in type:                                # Удаление дублирующихся слов
            words = list(set(words))
        if 'decl' in type:                                # Удаление дублирующихся слов и склонений
            while len(words) > 0:
                result.append(words[0])
                words = list(set(words) - set(declension(words[0])))
            return result
        return words
    
    
    def declension(userinput):
        """Функция получает одно или несколько слов ивозвращает список списков склонений заданных слов.
    
        """
        result = []
        decls = []
        userinput = modifier(userinput, 'punct') 
        for word in userinput:
            words = morph.parse(word)[0].lexeme        # Получение списка склонений
            for element in words:                      # Отчистка от лишних данных
                decl = str(element).split(' ')
                if len(decl[-3].replace("'", '').replace(',', '')) > 2:
                    decls.append(decl[-3].replace("'", '').replace(',', ''))
            if word not in decls:                      # Проверка наличие изначальной формы в результирующем списке
                decls.append(word)
            if len(userinput) == 1:
                return decls
            result.append(decls)
            decls = []
        return result
    
    
    def counter(words, deldub = False, deldecl = False):
        """Функция считает количество слов.
        Возвращает список, в котором первый элемент - количество слов, второй - все слова через пробел.
        Если передать переменной deldub значение True, будут удалены повторяющиеся слова,
        если передать переменной decl значение True, так-же будут удалены повторяющиеся склонения слов.
        
        """
        if deldub == False:
            words = modifier(words, 'punct')
        elif deldub == True and deldecl == False:
            words = modifier(words, 'punctdub')
        elif deldecl == True:
            words = modifier(words, 'punctdecl')
        words.insert(0, ('Количество слов - ' + str(len(words))))
        return words
    
    
    def generator(words):
        """Функция получает на вход список строк, и выводит список сочетаний слов из входных строк.
    
        """
        for text in words:
            words[words.index(text)] = modifier(text, 'punct')
        result = []
        while [] in words:
            words.remove([])
        genwords = list(product(*words))          # Создание списка сочетаний
        for i in genwords:
            result.append(' '.join(i))            # Преобразование множества в строку
        return result
    
    
    def lemma(words):
        """Функция получает строку, разбивает её на список по словам и выводит список нормальных форм слов.
    
        """
        words = modifier(words, 'punct')
        for i in words:
            words[words.index(i)] = morph.parse(i)[0].normal_form   
        return words
    
    
    def cityremover(text, punct = False, stopcity = cities):
        """Функция получает текст и удаляет из него города
           Если параметр punct в значении True - функция отчищает текст от знаков пунктуации 
        """
        if punct == True:
            text = modifier(text, 'punct')
        else:
            text = text.split(' ')
        words = [word for word in text if modifier(word, 'punct')[0] not in stopcity]
        words = ' '.join(words)
        return words
    
    
    def trimutm(urls):
        """Функция получает ссылку или несколько ссыло разделённых переносом строки(\n) и удаляет из неё utm метки.
        Если вводится одна ссылка - выводится строка, если несколько - список строк.
    
        """
        urls = urls.split('\n')
        while '' in urls:
            urls.remove('')
        while '\r' in urls:
            urls.remove('\r')
        result = []
        for url in urls:
            if "utm_" not in url:          # Проверка на содержание utm метки
               result.append(url)
               continue
            matches = re.findall('(.+\?)([^#]*)(.*)', url)
            if len(matches) == 0:
               result.append(url)
               continue
            match = matches[0]
            query = match[1]
            sanitized_query = '&'.join([p for p in query.split('&') if not p.startswith('utm_')])   # Отчистка от метки
            result.append(match[0]+sanitized_query+match[2])
        if len(urls) == 1:
            return result[0]
        else:
            return result
    
    
    def crossminus(userinput):
        """ Функция получает на вход строку состоящую из фраз разделённых переносом строки и производит добавление слов с префиксом '-' не входящих в данную фразу,
            но входящих в стальные фразы.
            Основное предназначение - создание ключевых фраз для рекламных кампаний
        """
        words = []
        allwords = []
        result = []
        for keys in userinput.split('\n'):                # Преобразование входной строки в список списков слов
            keys = modifier(keys, 'punct')
            words.append(keys)
        dub = set(functools.reduce(set.__and__, (set(i) for i in words)))  # Определение слов повторяющихся во всех фразах
        for key in words:
            allwords += key
        allwords = set(allwords)
        allwords ^= dub
        for key in words:
            for word in allwords:
                if word not in key:
                    key.append('-' + word)
        for i in range(len(words)):
            result.append(' '.join(words[i]))
        return result
