#Author: Sebastian Byczkowski
#Coroutines

from random import *
a = ['Oceans 11','Contagion','That Thing You Do!', 'Band of Brothers', 'Goodfellas', 'Gladiator', 'Jurrasic Park']
b = ['Steven Soderbergh','Tom Hanks','Martin Scorsese', 'Steven Spielberg', 'Ridley Scott']

def movgen(x):
    for i in x:
        yield i

count = 1
rannum = randint(4,7)
print rannum
while count <= rannum:
    print '------------'
    count1 = 0
    movies = movgen(a)
    directors = movgen(b)
    while count1 < 2:
        try:
            print movies.next()
            print directors.next()
        except Exception:
            count1 += 1
            continue
    count += 1



