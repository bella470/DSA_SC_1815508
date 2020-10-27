a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

a = a % 42
b = b % 42
c = c % 42
d = d % 42
e = e % 42
f = f % 42
g = g % 42
h = h % 42
i = i % 42
j = j % 42

num = [a, b, c, d, e, f, g, h, i, j]
a_set = set(num)
distinct_num = len(a_set)
print(distinct_num)