# sum of even numbers till 100
final_sum = 0

# method one

for number in range(0, 101):
    if number > 0 and number % 2 == 0:
        final_sum += number
print(final_sum)

# method two
final_sum = 0
for number in range(2, 101, 2):
    final_sum += number
print(final_sum)

