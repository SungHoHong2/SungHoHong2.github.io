# Class, Object, Instance
# A는 Object이다.
# A는 사람 Class의 Instance이다

# 클래스를 객체로 실체화 하는 과정
class Person():
    #name = "Nonamed"
    #age = 0

    def __init__(self, name, age):
        print("사람 생성했습니다.")
        self.name = name
        self.age = age

    def __add__(self, other):
        print("{myname}이 {partner}와 적극적으로 만난다.".format(myname = self.name, partner = other.name))

    def hello(self):
        print("안녕하세요 {age}살 {name} 입니다.".format(name=self.name, age = self.age))

    def meet(self, another):
        print("{myname}이라는 사람이 {another_name}을 만났습니다.".format(myname= self.name, another_name =another.name))

    def __str__(self):
        return self.name


a = Person("",0)

print(Person) #Class
print(a) #Object
print(a.name)
print(a.age)


# 클래스에 값 입력 가능
a.name = "안수찬"
a.age = 30

print(a.name)
print(a.age)


# Class내 Function 실행하기
a.hello()


# 기본적으로 변수의 은닉 개념이 있는가?
b = Person("홍성호", 29)
b.hello()


# 타 클래스 입력
a.meet(b)
a.__add__(b)
print(a)



# Triangle
# width , height
# get_area, is_bigger_than

class Triangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        self.area = int((self.width*self.height)/2)
        return self.area

    def is_bigger_than(self, other):
        return self.area if self.area>other.area else other.area


a = Triangle(10,20)
b = Triangle(20,30)

print(a.get_area())
print(b.get_area())
print(a.is_bigger_than(b))


# acmipc
# 알고스팟