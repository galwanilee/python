class Rectangle:
    def __init__(self,a,b):
        self.length=1
        self.width=1
        self.num=a
        self.den=b
    def per(self):
        print(2*(self.length+self.width))
    def sq(self):
        print(self.width*self.length)
    def set_length(self,length):
        self.length=length
    def set_width(self,width):
        self.width=width
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_ab(self):
        print(f'чисельник = {self.num} знаменник = {self.den}')
        print(f'{self.num/self.den}')

class Shop:
    def __init__(self,price,describe,lb):
        self.price=price
        self.describe=describe
        self.lb=lb


class Сlient:
    def __init__(self,l,n,p,number):
        self.lastname=l
        self.name=n
        self.patronymic=p
        self.fnumber = number
class Order(Shop,Сlient):
    def obsh(self):
        return self.price

class File:
    def __init__(self,file):
        self.prizvesheile=file
    def file1(self):
        with open(self.prizvesheile) as infile:
            lines = 0
            words = 0
            characters = 0
            for line in infile:
                wordslist = line.split()
                lines = lines + 1
                words = words + len(wordslist)
                characters += sum(len(word) for word in wordslist)
        print(lines)
        print(words)
        print(characters)
class Student:
    def __init__(self,firstname,name,otchestvo,number,ozen):
        self.prizveshe = firstname
        self.name = name
        self.otchestvo = otchestvo
        self.fnumber = number
        self.zen=ozen
    def se(self):
        return sum(self.zen)/len(self.zen)
    def pri(self):
        print(f'{self.prizveshe} {self.name} {self.otchestvo}  -  {self.se()}' )
class Group:
    def add(self):
        first=Student('Har','Alex','Jar',12,[1,5,2,5])
        first.pri()
        second=Student('Har1','Alex2','Jar1',12,[4,4,3,5])
        second.pri()
        third = Student('Har2', 'Alex2', 'Jar2', 12, [5, 4, 3, 5])
        third.pri()
        fours = Student('Har3', 'Alex3', 'Jar3', 12, [5, 5, 3, 5])
        fours.pri()
        fifth = Student('Har4', 'Alex4', 'Jar4', 12, [5, 5, 5, 5])
        fifth.pri()


class Binaty_TREE:
    def __init__(self):
        self.otchestvob=[]
    def add_mas(self,el):
        self.otchestvob.append(el[0])
    def price(self,tovar,pri):
        from collections import Counter
        c = Counter(self.otchestvob)
        try:
            print(f'Товар {tovar} в базе {c[tovar]} раз цена -{c[tovar]*pri}')
        except:
            pass
if __name__ == '__main__':
    a=Rectangle(4,5)
    a.set_width(10)
    a.set_length(5)
    a.per()
    a.sq()
    a.get_ab()

    b=File('test.txt')
    b.file1()

    c=Group()
    c.add()


    d=Binaty_TREE()
    d.add_mas(['gar',125125])
    d.add_mas(['tov', 52])
    d.add_mas(['train', 5])
    d.add_mas(['gar', 125125])
    d.add_mas(['tov', 52])
    d.add_mas(['train', 5])
    d.price('train',5)
    d.price('tov',12)
