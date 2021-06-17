
a = int(input())
b = int(input())
c = int(input())

if a > b > c or c > b > a:
    meio = b
elif b > c > a or a > c > b:
    meio = c
elif b == c != a:
    meio = b
else:
    meio = a

print(meio)