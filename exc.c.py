l_prime: list[int] = []
for i in range(2, 201, 1):
    divider: int = 2
    while divider < i:
        if i % divider == 0:
            break
        divider += 1
    if divider < i:
        print(f"{i} is not prime")
    else:
        l_prime.append(i)
print(l_prime)
