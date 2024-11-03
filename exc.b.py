while True:
    try:
        num: int = int(input("enter a nuber between 10-99: "))
        while not 10 <= num <= 99:
            print(f"the number {num} is not a valid response")
            num: int = int(input("enter a nuber between 10-99: "))
        break
    except:
        print("Try again")

if num % 10 > num // 10:
    print((num % 10) * 10 + num // 10)
else:
    print(num)
