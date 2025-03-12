"""Syntactic sugar - Fancy word"""
def is_even(num: int):
    return num % 2 == 0


print(3.+(4))
print(3 + 4)

threes = []
numbers = [1, 5, 3, 4, 3, 1, 3]
for num in numbers:
    if num == 3:
        threes.append(num)
    else:
        threes.append("NO")
print(threes)

print([2*num if num == 3 else "NO"*3 for num in numbers])

print([is_even(num) for num in numbers])

dicts = {"one": 1, "two": 2}

reversals = {value: key for key, value in dicts.items()}

print(reversals)
