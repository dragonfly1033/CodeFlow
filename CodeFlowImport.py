import CodeFlowTest

a = 5
b = '4'
c=a+int(b)
print(c)
list=[1,2,3,4,5]
if c == 9:
  print('square!')

while 1 == 9:
  pass

for i in range(b, c):
  print(i)


CodeFlowInterpreter.Flow(__file__)
