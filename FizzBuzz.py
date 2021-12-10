for num in range(1, 100):
    if not num%3 or not num%5:
        if num%3 == 0:
            print("Fizz", end="")
        if num%5 == 0:
            print("Buzz", end="")
        print()
    else:
        print(num)
        
    