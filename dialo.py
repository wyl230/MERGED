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
secddia = [Actor('b01',pos),Actor('b02',pos) ]
thirdia = [Actor('c01',pos),Actor('c02',pos) ]
forthdia = [Actor('d01',pos),Actor('d02',pos) ]

alldialogue.append(firstdia)
alldialogue.append(secddia)
alldialogue.append(thirdia)
alldialogue.append(forthdia)