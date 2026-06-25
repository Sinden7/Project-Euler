counter = 0
for i in range(1,138001):
    square = i**2
    if square % 2 == 1:
        counter += square

print(counter)
