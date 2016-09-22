---
published: true
title: 파이썬 중급 4일차
layout: post
category: programming_kr
permalink: /programming_kr/python_4
---

### 클래스
1. Animal Class
2. State type(string): "dog", "cat", "fish"
3. State type weight : 
4. Behavior "먹이를 먹습니다."


``` python

class Animal:
    def __init__(self, name, weight):
        self.weight = weight
        self.name = name

    # polymorphism 
    # 함수가 다른 형태로 사용할 수 있을 떄 
    # - Parametic Polymorphism
    
    def eat(self, *args):
        #print([i for i in args])
        if not args:
            print("먹이를 먹습니다.")
        else:
            print("\n".join(i+"를 먹이를 먹습니다." for i in args))

    def swim(self):
        print("swim" if self.name=="fish" else "dead")


    def weight_is_heavier_than(self, other):
        print(self.name+"이 더 무겁습니다." if self.weight > other.weight else other.name+'이 더 무겁습니다.' )



d4 = Animal("dog", 4)
d4 = Animal("dog", 4)
c6 = Animal("cat", 6)
c3 = Animal("cat", 3)
f1 = Animal("fish", 1)


f1.eat("소세지","햄버거")
f1.swim()
d4.swim()

```

<br>

### 상속

1. 삼각형 사각형 
2. width, height를 가진다. 
3. area = w * h / 2, area = w * h 
  
    
``` python

 class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def is_bigger_than(self, other):
        return True if self.area() > other.area() else False


class Rect(Shape):
    def area(self):
        return self.width * self.height


class Tri(Shape):
    def area(self):
        return (self.width * self.height) / 2


r1 = Rect(10,20)
t1 = Tri(10,20)

print(r1.area())
print(t1.area())
print(r1.is_bigger_than(t1))
 
 ```




