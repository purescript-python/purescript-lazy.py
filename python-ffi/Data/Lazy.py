def defer(thunk):
    cache_ = [None, thunk]

    def result():
        v, thunk = cache_
        if thunk is None:
            return v

        cache_[0] = thunk()
        cache_[1] = None
        return cache_[0]

    return result


def force(l):
    return l()
