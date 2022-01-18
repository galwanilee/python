import datetime


class Bilet:
    def __init__(self,price,nomer,type):
        self.price=price
        self.nomer=nomer
        self.type=type
    def get_nomer(self):
        return self.nomer
    def get_price(self):
        if self.type==1:
            return self.price
        elif self.type==2:
            return self.price*0.6
        elif self.type==3:
            return self.price*0.5
        elif self.type==4:
            return self.price*1.1
    def pri(self):
        print('><Печать билета><')
        print(f'========================\n\tNumber ={self.nomer}\t\n\ttype={self.type}\t\n========================')
def get(g,number):
    for i in range(len(g)):
        if g[i].get_nomer()==number:
            print(f'Price= {g[i].get_price()}')
            g[i].pri()
            break

if __name__ == '__main__':
    g=[]
    g.append(Bilet(100,123,1))
    g.append(Bilet(50, 124, 3))
    g.append(Bilet(100, 125, 2))
    g.append(Bilet(50, 126, 1))
    g.append(Bilet(100, 127, 2))
    g.append(Bilet(100, 128, 4))
    g.append(Bilet(75, 129, 3))
    g.append(Bilet(100, 130, 2))
    g.append(Bilet(75, 131, 1))
    get(g,123)


    while True:
        print('Вы хотите закать пиццу')
        today = datetime.date.today()
        wd = datetime.date.weekday(today)
        print(wd)
        if wd==0:
            print('Понедельник- гавайская')
            perem=0
            while(perem!=1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem=int(input())
        if wd==1:
            print('Вторник- мясная')
            perem = 0
            while (perem != 1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem = int(input())
        if wd==2:
            print('Среда- папирони')
            perem = 0
            while (perem != 1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem = int(input())
        if wd==3:
            print('Четверг- сырная')
            perem = 0
            while (perem != 1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem = int(input())
        if wd==4:
            print('Пятница- сладкая')
            perem = 0
            while (perem != 1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem = int(input())
        if wd==5:
            print('Суббота- чизбургер пицца')
            perem = 0
            while (perem != 1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem = int(input())
        if wd==6:
            print('Воскресенье- Митболл пицаа')
            perem = 0
            while (perem != 1):
                print('Добавить 1)Ничего\n2)Ананас \n3)Огурцы \n4)Бортик сырный \n5)Помидоры')
                perem = int(input())
        perem=input()
