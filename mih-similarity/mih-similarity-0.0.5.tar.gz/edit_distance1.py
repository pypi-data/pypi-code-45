# encoding: utf-8



def ed(s1, s2):

    if 0 == len(s1):
        return len(s2)

    if 0 == len(s2):
        return len(s1)


    d = ed(s1[:-1], s2) + 1
    i = ed(s1, s2[:-1]) + 1
    e = 0 if s1[-1] == s2[-1] else 2
    s = ed(s1[:-1], s2[:-1]) + e

    return min(d, i, s)




if __name__ == '__main__':
    s1 = 'intention'
    s2 = 'execution'

    s1 = u'朱婷21分！瓦基弗银行3-1取欧冠两连胜，纳兹险葬送好局'
    s2 = u'朱婷砍21分得分王 率瓦基弗银行3-1夺欧冠两连胜'

    print(ed(s1, s2))
