# encoding: utf-8

import numpy as np
import pandas as pd


def ed(s1, s2):

    d = np.empty((len(s1)+1, len(s2)+1))
    p = np.empty((len(s1)+1, len(s2)+1), dtype=tuple)
    f = np.empty((len(s1)+1, len(s2)+1), dtype='<S4')
    d[:] = np.nan
    p[:] = np.nan

    for i in range(len(s1)+1):
        d[i][0] = i
        p[i][0] = (i-1, 0)
        f[i][0] = 'del'

    for j in range(len(s2)+1):
        d[0][j] = j
        p[0][j] = (0, j-1)
        f[0][j] = 'ins'

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            det = d[i-1, j] + 1
            ins = d[i, j-1] + 1
            eql = 0 if s1[i-1] == s2[j-1] else 2
            sub = d[i-1, j-1] + eql

            #seq = [det, ins, sub]
            #seq = [det, sub, ins]
            seq = [sub, det, ins]  # the same
            #seq = [sub, ins, det]  # the same
            #seq = [ins, det, sub]
            #seq = [ins, sub, det]

            #index = [0, 1, 2]
            #index = [0, 2, 1]
            index = [1, 2, 0]  # the same
            #index = [2, 1, 0]  # the same
            #index = [1, 0, 2]
            #index = [2, 0, 1]

            d[i][j] = min(seq)

            # path
            idx = np.argmin(seq)

            if index[0] == idx:
                p[i][j] = (i-1, j)
                f[i][j] = 'del'
            elif index[1] == idx:
                p[i][j] = (i, j-1)
                f[i][j] = 'ins'
            elif index[2] == idx:
                p[i][j] = (i-1, j-1)
                if 0 == eql:
                    f[i][j] = 'eql'
                elif 2 == eql:
                    f[i][j] = 'sub'


    # min distance path
    m = np.ones((len(s1)+1, len(s2)+1))

    idx = (-1, -1)
    while((0, 0) != idx):
        m[idx[0], idx[1]] = 0    
        idx = p[idx[0]][idx[1]]

    t = np.ma.masked_array(d, mask=m)
    t = np.flipud(t)
    # print(pd.DataFrame(t).fillna(''))


    # operation flag
    t = np.ma.masked_array(f, mask=m)
    t = np.flipud(t)
    # print(pd.DataFrame(t).fillna(''))


    # for check only
    d = np.flipud(d)
    p = np.flipud(p)
    # print(pd.DataFrame(d))
    # print(pd.DataFrame(p))

    return d[0][-1]



if __name__ == '__main__':
    s1 = 'intention'
    s2 = 'execution'

    s1 = u'朱婷21分！瓦基弗银行3-1取欧冠两连胜，纳兹险葬送好局'
    s2 = u'朱婷砍21分得分王 率瓦基弗银行3-1夺欧冠两连胜'

    s1 = [u'朱婷', u'21', u'分', u'瓦基弗', u'银行', u'3', u'1', u'取', u'欧冠', u'两', u'连胜', u'纳兹', u'险', u'葬送', u'好局']
    s2 = [u'朱婷', u'砍', u'21', u'分', u'得分王', u'率', u'瓦基弗', u'银行', u'3', u'1', u'夺', u'欧冠', u'两', u'连胜']

    dt = ed(s1, s2)
    mx = max(len(s1), len(s2))
    print(dt, len(s1), len(s2), mx, dt/mx)
    un = len(set(s1) & set(s2))
    print(un, un/mx)
