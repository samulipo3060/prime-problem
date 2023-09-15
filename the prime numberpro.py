prime_numbers = []
for numbers in range(1,80):
    if numbers>1:
        for items in range(2,numbers):
            if numbers%items == 0:
                break
        else:
           prime_numbers.append(numbers)
print(prime_numbers)






