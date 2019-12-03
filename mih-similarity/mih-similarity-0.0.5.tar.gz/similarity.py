# encoding: utf-8

from progressbar           import progressbar
from edit_distance2        import ed
from nltk.metrics.distance import edit_distance


class Similarity(object):


    @classmethod
    def __similarity__(cls, t1, t2, threshold):

        return (1 - edit_distance(t1, t2) / (max(len(t1), len(t2)) + .0000001)) >= threshold


    @classmethod
    def similarity(cls, X, threshold=.8):

        y = [[0]]
        
        for i, t1 in progressbar(enumerate(X[1:])):
            flag = True

            for j, tids in enumerate(y):
                t2 = X[tids[0]]
                if cls.__similarity__(t1, t2, threshold):
                    y[j].append(i+1)
                    flag = False
                    break

            if flag:
                y.append([i+1])

        return y



if __name__ == '__main__':

    X = [
            u'我爱你中国',
            u'你好',
            u'我爱你国家',
            u'我爱你中国',
            u'我爱你中国',
            u'我爱你中国',
            u'我爱你中国',
            u'你好',
            u'你好',
            u'我爱你中国',
            u'002型航母就这样',
            u'曝出了?院士称等到神器上舰',
            u'中国国产航母下水引起世界震动',
            u'界不断猜测中国的航母',
            u'实用要求，但我们不会',
            u'停止建造航母的脚步，因为',
            u'001型航母远远没有达到',
            u'我们满意的水平，现有的航母规模也无法满足未来中国',
            u'海军海上维权的需求。美国媒体',
            u'"金字塔"报',
            u'也说中国未来至少需要6艘航母。此外，中',
            u'国社会经济正处在产业升级、生产转'
        ]

    y = Similarity.similarity(X, .6)

    print(y)
