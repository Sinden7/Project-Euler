# Code is not optimised whatsoever, incredibly slow so I need
# to come back and fix it some day - J.S (17/09/2026)

num =  600851475143
for i in range(1,num):
    if num % i == 0:
        half = i/2
        for j in range(2,int(half+1)):
            if i % j == 0:
                break
        else:
            highest = i

print(highest)

