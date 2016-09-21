from functools import reduce


# if절 사용하기
def usingCampus(n, *args):
    resultList = []
    for i in range(n)[1::]:
        element = ""
        for s in args:
            num, name = s
            element += name if i % num == 0 else ""
        resultList.append(element)
    return resultList

# print(usingCampus(100, (3, "fast"), (5, "campus")))


# *2 Lambda MAP
def multiplyTwo(n):
    return list(map(lambda x: x*2, range(n)))

#print(multiplyTwo(100))


# *2 multiply Less
def multipyLess(n):
    return list(map(lambda x: x*2 if x*2<n else False , range(n)))

#print(multipyLess(100))

# *2 multiply Commprehension
def multiplyLessComp(n):
    return list(i*2 for i in range(n) if i*2<n)

#print(multiplyLessComp(100))


# get positive for

def getPositive(elements):
    resultList =  []
    for element in elements:
        if element >= 0:
            resultList.append(element)
    return resultList

#print(getPositive([203,43,32,3,0,-1,-23]))


# get positive lambda

def getPositiveLamda(elements):
    return list(filter(lambda x: x>=0 , elements))

#print(getPositiveLamda([203,43,32,9,0,-1,-23]))


def getPositiveComp(elements):
    return list(i for i in elements if i >= 0 )


#print(getPositiveComp([203,43,32,9,0,-1,-23]))



# reduce

#adding 1 to 10
#print(reduce(lambda x, y : x+y, range(10+1)))



# reduce get means

data = [
      {"rent" : 50, "deposit" : 1000}
    , {"rent" : 60, "deposit" : 2000}
    , {"rent" : 90, "deposit" : 3000}
]

def get_means(data):
    return reduce(lambda x, y : {"rent" : x['rent']+ y['rent'], "deposit" : x['deposit']+ y['deposit']}, data)
#print(get_means(data))


def get_awesome_list(n, *args):
    return ["".join([ arg[1] if (i+1)%arg[0]==0 else "" for arg in args ]) for i in range(n)]


#숙제1
def get_awesome_list_lambda(n, *args):

    args = [ arg for arg in args]
    #print(args)
    #print(list(filter(lambda y : y[0]==3, args)))
    return list(map(lambda x : "".join(list(map(lambda y : y[1] if(x+1)%y[0]==0 else "", args))) , range(n)))


#print(get_awesome_list_lambda(100, (3, "fast"), (5, "campus")))



#숙제2
def snail(n):

    snail = [[0] * n for x in range(n)]

    x = 0
    y = 0

    count = 1
    shield = 0

    for i in range(n * n):
        snail[y][x] = count
        count += 1

        if x < n - 1 - shield and y == shield:
            x += 1
        elif x == n - 1 - shield and y < n - 1 - shield:
            y += 1
        elif x > shield and y == n - 1 - shield:
            x -= 1
        elif x == shield and y == n - 1 - shield:
            shield += 1
            y -= 1
        elif x == shield - 1 and y > shield:
            y -= 1


    for i in range(n):
        row = ""
        for j in range(n):
            row += " "+str(snail[i][j])
        print(row)

snail(5)






