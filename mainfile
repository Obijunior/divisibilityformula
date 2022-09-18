import math
import re

x = int(input("X value : "))
y = int(input('Y value : '))
y_digits = []
t = str(y)

for j in t:
  y_digits.append(j)

y_int = []
i = 0

while i < len(y_digits):
  j = int(i)
  placeholder = int(y_digits [j])
  y_int.append(placeholder)
  i += 1

y_length = len(y_digits)
r = ""
j = 1

while j < len(y_int):
  r = r + str(y_int[j])
  j += 1
 
z = float(x * y)

i = int(r) / y_int[0]
i = str(i)

#removes decimal sign
i = i.replace(".", "")

n = "1." + i
n = float(n)

q = z/n

z = str(z)
n = str(n)
q = str(q)

print("x * y = " + z)
print("n = " + n)
print("CHECKING - (x*y)/n = " + q)

  
