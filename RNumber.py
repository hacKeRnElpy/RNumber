import random
def range(n):
    for i in range(m, n):
        yield i + 1
print('Greetings to the random number generator')
m = int(input('of(not inclusive): '))
n =  int(input('to(inclusive): '))
chisloo=[]
for i in range(n):
    chisloo.append(i)
chisloo1=random.choice(chisloo)
print(chisloo1)