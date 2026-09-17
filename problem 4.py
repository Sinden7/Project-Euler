def palindrome():
    highest = 0
    for i in range(100,1000):
        for j in range(100,i):
            num = i*j
            p_holder = num
            new_num = 0
            while num != 0:
                first_num = num % 10
                new_num = (new_num * 10) + first_num
                num = num // 10

            
            if p_holder == new_num:
                if new_num > highest:
                    highest = new_num

    print(highest)
       
palindrome()  