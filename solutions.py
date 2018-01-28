#
1. Count no of letters and digits
countL = 0;
countD = 0;
for c in "Test123":
    if (c.isalpha()):
        countL = countL + 1;
    else :
        countD = countD + 1;
print("No of letters: ", countL);
print("No of digits: ", countD);

#
2. Remove punctuation
import string
s = "It's a good day"
for c in s:
    if c not in string.punctuation:
    print(c, end = '')

# 3. Sort alphabets in string
s = "bdca"
b = sorted(s)
c = ''.join(b)
print(c)

# 4. no of each vowel
s = "aabcdee"
vowel = "aeiou"
v = {}.fromkeys(vowel, 0)
for c in s:
    if c in v:
    v[c] = v[c] + 1
print(v)

# 5. palindrome string
s = "abba"
s1 = s[::-1]
if (s == s1):
    print("String is palindrome")
else :
    print("String is not palindrome")

# 6. tuple operations
tupleem = ()
print(tupleem)

tuple1 = (1, "test", 1.3)
print(tuple1)

print(tuple1[0: 2])

tuple2 = tuple1 + tuple('b')
print(tuple2)

l = list(tuple2)
print(l)

# 7. tuple to str
tuple1 = ('t', 'u', 's', 'h')
str1 = ''.join(tuple1)
print(str1)

# 8. del tuple element
tuple1 = ('t', 'u', 's', 'h')
l = list(tuple1)
l.remove('u')
t1 = tuple(l)
print(t1)

# 9. check whether item exists in tuple
tuple1 = ('t', 'u', 's', 'h')
for c in tuple1:
    if c is 'h':
    print("Element found")
else :
    print("Not found")

# 10. change last value tuple
tuple1 = ('t', 'u', 's', 'h')
l = list(tuple1)
l[-1] = 'a'
t1 = tuple(l)
print(t1)

# 11. string concat
x = "hello"
y = "world"
res = x + " " + y
print(res)

# 12. set operations
x = set([1, 2, 3, 4])
y = set([7, 8, 3, 4])
x.remove(3)
print(x)

print(x.union(y))
print(x.intersection(y))
print(x.difference(y))

# 13. array
from array
import array
x = array('I', [1, 2, 3, 4])
for i in x:
    print(i)

# 14. list unique elements
x = [1, 2, 3, 1, 4, 2]
y = set(x)
print(y)

# 15. array insertion
x = []
for i in range(3):
    x.append([])
for j in range(3):
    val = int(input("Enter value"))
x[i].append(val)
print(x)

# 16. 2 d array multiplication
import numpy as np
x = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 9, 10]
]
y = [
    [3, 2, 1],
    [5, 4, 3, ],
    [1, 7, 4]
]
res = np.multiply(x, y)
print(res)

# 17. factors of number
x = 10
for i in range(1, x + 1):
    if x % i == 0:
    print(i)

# 18. Find HCF / GCD
from math
import gcd
x = gcd(20, 8)
print(x)
