import CodeFlowTest

a = 5
b = '4'
c=a+int(b)
print(c)
if c == 9:
  print('square!')

while 1 == 9:
  pass

for i, v in enumerate([1,2,3,4,5]):
  print(i, v)


CodeFlowInterpreter.Flow(__file__)
