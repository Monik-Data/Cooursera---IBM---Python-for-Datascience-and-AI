print("hello, Python!")

name = "moein nikpour"

r = name[::2]
print(r)
len(r)

name.upper()
str(1 + 1)
"ABC".replace("AB", "ab")

s = "nikpourmoein@gmail.com"
r = s.split('@')
r
del(r[0])
r
r.append(['moein', 'nik', 'hamed'])
r
r[1][0][2]
r.extend(['school', 'Banna', 'umberella'])
r

q = ('zebra', 'cat', 'dog', 'fish')
q
q_sorted = sorted(q)
q_sorted
w = ('shark')
q_new = ('spider', 'shark') + q[1:]
q_new


set_a = {'apple', "orange", 'banana'}
set_b = {'apple', "cucumbers", 'banana'}


set_a & set_b
set_a.union(set_b)
'banana' in set_a
set_b.issubset(set_a)

set_a.add("Hello")
set_a
set_a.remove("apppke")

'orange' in set_a


set_a.difference(set_b)
set_a.intersection(set_b)
set(set_a).issuperset(set_b)

a = [1, 2, 3, 4]
b = set([1, 2, 3, 4])
c = (1, 2, 3, 4)
d = set(a)
sum(a)print("hello, Python!")

name = "moein nikpour"

r = name[::2]
print(r)
len(r)

name.upper()
str(1 + 1)
"ABC".replace("AB", "ab")

s = "nikpourmoein@gmail.com"
r = s.split('@')
r
del(r[0])
r
r.append(['moein', 'nik', 'hamed'])
r
r[1][0][2]
r.extend(['school', 'Banna', 'umberella'])
r

q = ('zebra', 'cat', 'dog', 'fish')
q
q_sorted = sorted(q)
q_sorted
w = ('shark')
q_new = ('spider', 'shark') + q[1:]
q_new


set_a = {'apple', "orange", 'banana'}
set_b = {'apple', "cucumbers", 'banana'}


set_a & set_b
set_a.union(set_b)
'banana' in set_a
set_b.issubset(set_a)

set_a.add("Hello")
set_a
set_a.remove("apppke")

'orange' in set_a


set_a.difference(set_b)
set_a.intersection(set_b)
set(set_a).issuperset(set_b)

a = [1, 2, 3, 4]
b = set([1, 2, 3, 4])
c = (1, 2, 3, 4)
d = set(a)
sum(a)
sum(b)
sum(c)
sum(d)
b.add(7)

tdic = {'apple': "Yellow", 'orange': "Orange"}
tdic['cucumbers'] = ['hello', 'Mellow', 1]

tdic
tdic["cucumbers"]


set(tdic)

tdic.keys()
tdic.values()
b
1 in {'1', '2'}

sum(b)
sum(c)
sum(d)
b.add(7)

tdic = {'apple': "Yellow", 'orange': "Orange"}
tdic['cucumbers'] = ['hello', 'Mellow', 1]

tdic
tdic["cucumbers"]


set(tdic)

tdic.keys()
tdic.values()
b
1 in {'1', '2'}

squares = ['red', 'yellow', 'Blue']

for i,square in enumerate(set_a):
    print (square )
    print (i )


def add1 (a,b):
    c=a+b
    return c

add1 (1,2)


def MJ():
    print('Michael Jackson')

def MJ1():
    print('Michael Jackson')
    return(None)

MJ()
MJ1()

print(MJ())
print(MJ1())

# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var = artist
    print(internal_var, "is an artist")

printer1(artist)




myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

# ================ Classes ======================
# Import the library
import matplotlib.pyplot as plt
%matplotlib inline

class circle (object):

    # cosntructor
    def __init__(self , radius = 3, color = 'blue' ):
        self.radius = radius
        self.color = color

    # Method
    def drawcircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)




c1 = circle (10,'red')
c1.drawcircle()
dir (circle)
c1.color = 'yellow'
c1.radius
c1.drawcircle()
c1.add_radius(20)
