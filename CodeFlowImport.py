import CodeFlowInterpreter
import CodeFlowTest


a = 9

b = 8

print(a+b)

c = 'hey'

d = a+b

list = [1, 2, 3, 4]

print(c, d)

g = input('whats your name: ')

while g == 'me':
    while g == 'you':
        print('no')

for i in range(3):
    for i in list:
        pass

CodeFlowInterpreter.Flow(__file__)
# CodeFlowTest.Flow(__file__)
#input()
