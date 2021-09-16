n = int(input())
fatorial = n
if n == 0:
    fatorial = 1
while n > 1:
    fatorial = fatorial * (n - 1)    
    n = n - 1
print(fatorial)
