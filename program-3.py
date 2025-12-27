a = int(input("Enter a number: "))

# decide how many odd numbers to print
if a % 2 == 0:
    limit = a - 1
else:
    limit = a

result = []

for i in range(1, limit + 1):
    result.append(2 * i - 1)

print("Output:", result)
