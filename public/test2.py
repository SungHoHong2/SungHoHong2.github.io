animals = ['dog','cat', 'monkey']

for animal in animals:
    print(animal)

#Iterator
#print(animals.__iter__())           # List_iterator 객체 조회
#print(iter(animals))

animals_iterator = animals.__iter__()
print(animals_iterator.__next__())
print(next(animals_iterator))

#elements - > element iterator로 바꾼 다음에 -> next로 조회한다.







