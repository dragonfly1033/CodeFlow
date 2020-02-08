import CodeFlowInterpreter
import CodeFlowTest


a = 9

b = 8

print(a+b)

c = 'hey'

d = a+b

print(c, d)

g = input('whats your name: ')

while g == 'me':
    print('no')

CodeFlowInterpreter.Flow(__file__)
# CodeFlowTest.Flow(__file__)
#input()
