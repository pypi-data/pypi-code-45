# encoding: utf-8

from progressbar    import progressbar
from edit_distance2 import ed


class Similarity(object):


    @classmethod
    def __similarity__(cls, t1, t2, threshold):

        print(1 - ed(t1, t2) / (max(len(t1), len(t2)) + .0000001))

        return (1 - ed(t1, t2) / (max(len(t1), len(t2)) + .0000001)) >= threshold


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
            u'我爱你国家'
        ]

    y = Similarity.similarity(X, .6)

    print(y)
