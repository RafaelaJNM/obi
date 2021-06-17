n = int(input())#plano que ganha
m = int(input())#meses

tot = 0
for i in range(m):
    nm = int(input())#usou no mes
    tot += nm

cal = (n*m) - tot
res = cal + n

print(res)