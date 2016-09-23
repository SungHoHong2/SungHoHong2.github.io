# Iterator 생성 -> __next__
# Iterable -> __iter__

class myrange:
    def __init__(self, n):
        self.i, self.n = (0, n)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


#for i in myrange(5):
#    print(i)

#for i in range(5):
#    print(i)


m1 = myrange(10)

# 데이터 조회
print(list(m1))

# 데이터 손실
print(list(m1))




class myrange_basic:      #iterable
    def __init__(self, n):
        self.n = n

    # 데이터가 중도에 소실되는 것을 방지
    def __iter__(self):
        return myrange_iterator(self.n)


class myrange_iterator:   #iterator
    def __init__(self, n):
        self.i, self.n = (0, n)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


m1 = myrange_basic(10)

# 데이터 조회
print(list(m1))

# 데이터 손실없음
print(list(m1))






