SENTINEL: str = 'x'
results: list[int] = [0,0,0,0]
options = ['a', 'b', 'c', 'd']
while True:
    answer = input("enter your answer: ")
    if answer == SENTINEL:
        break
    if answer not in ['a', 'b', 'c', 'd']:
        print("not an option")
        continue
    results[options.index(answer)] += 1

for i in range(len(results)):
    print(f"{results[i]} students selected answer {options[i]} ")

print(f"{options[results.index(max(results))]} is the most common answer")
print(f"{options[results.index(min(results))]} is the least common answer")
