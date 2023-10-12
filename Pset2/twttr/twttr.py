text = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
output = print("Output: ", end="")

for x in text:
    if x.casefold() not in vowels:
        print(x, end="")

print()
