def searchInterval(x, rk, direction, func, t0 = 0.5, h0 = 1.1, alpha = 1.1):
        '''
        确定搜索区间
        '''
        k, t, h= 0, t0, h0
        tk = t
        tk_1 = tk + h
        fik, fik_1 = func(x-tk*direction, rk), func(x-tk_1*direction, rk)
        if fik > fik_1:
            h = alpha*h
            t, tk = tk, tk_1
            fik = fik_1
            tk_1 = tk + h
            fik_1 = func(x-tk_1*direction, rk)
            while fik > fik_1:
                h = alpha*h
                t, tk = tk, tk_1
                fik = fik_1
                tk_1 = tk + h
                fik_1 = func(x-tk_1*direction, rk)
        else:
            h = -h
            t = tk_1
            tk_1 = tk + h
            fik_1 = func(x-fik_1*direction, rk)
            while fik > fik_1:
                h = alpha*h
                t, tk = tk, tk_1
                fik = fik_1
                tk_1 = tk + h
                fik_1 = func(x-tk_1*direction, rk)
        return [min([t, tk_1]), max([t, tk_1])]