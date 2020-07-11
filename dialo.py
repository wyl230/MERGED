import pgzrun
from pgzero.actor import Actor
class dialogue :
    __slots__ = (   'detail' )
    def __init__(self,detail):
        self.detail = detail
alldialogue = []
firstdia = [ ]
pos = (500,510)
firstdia.append(Actor('a01',pos))
firstdia.append(Actor('a02',pos))
firstdia.append(Actor('a03',pos))
secddia = [Actor('b01',pos),Actor('b02',pos) ,Actor('b03',pos)]
thirdia = [Actor('c01',pos),Actor('c02',pos) ]
forthdia = [Actor('d01',pos),Actor('d02',pos) ]
alldialogue.append(firstdia)
alldialogue.append(secddia)
alldialogue.append(thirdia)
alldialogue.append(forthdia)
d1= [Actor('e01',pos),Actor('e02',pos),Actor('e03',pos),Actor('e04',pos)]

d2= [Actor('f01',pos),Actor('f02',pos)]
d3=[Actor('g01',pos),Actor('g02',pos),Actor('g03',pos)]
d4=[Actor('h01',pos),Actor('h02',pos)]
d5 = [Actor('i01',pos)]

alldialogue.append(d1)
alldialogue.append(d2)
alldialogue.append(d3)
alldialogue.append(d4)
alldialogue.append(d5)