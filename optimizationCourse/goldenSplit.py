def goldenSplit(x, t, epsilon, direction, rk, func):
        '''
        黄金分割法
        param
        t:搜索区间
        direction:搜索方向
        return：搜索结果t
        '''
        a, b = t[0], t[1]
        t1 = a + 0.618*(b-a)
        t2 = a + 0.382*(b-a)
        fi1, fi2 = func(x-t1*direction, rk), func(x-t2*direction, rk)
        while abs(t2 - t1) >= epsilon:
            print('t2', t2, 't1', t1)
            if fi1 < fi2:
                a = t2
                t2, fi2 = t1, fi1
                t1 = a + b - t2
                fi1 = func(x-t1*direction, rk)
            else:
                b = t1
                t1, fi1 = t2, fi2
                t2 = a + 0.382*(b-a)
                fi2 = func(x-t2*direction, rk)
        return (t1 + t2)/2