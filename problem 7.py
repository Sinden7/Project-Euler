counter = 1
num = 3
while counter != 10001:
    for i in range(2,num):
        if num % i == 0:
            num += 1
            break

    else:
        num += 1
        counter += 1


print(f"The 10001st prime number is {num-1}")