import math

def aval(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0 :
            return False
    return True

j = 0 
i=2_000_000_000
while True:
    i+=1
    if aval(i) and aval((i-2)):
        print(i)
        j+=1
    if j >= 1000:
        print(j)
        exit()
