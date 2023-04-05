# Task 6
# Створіть список із числами, які є в обох списках.

a = [1, 2, 3, 4]
b = [1, 2, 3]
c=(a+b)
for i in c:
    if c.count(i) > 1:
        c.remove(i)
print(sorted(c))