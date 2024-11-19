
combinations = [(True, True), (True, False), (False, True), (False, False)]

print("AND ოპერატორი:")
for a, b in combinations:
    print(f"{a} AND {b} = {a and b}")  # AND ოპერატორი


print("\nOR ოპერატორი:")
for a, b in combinations:
    print(f"{a} OR {b} = {a or b}")  



# Input for the first number and convert it to an integer
first_number = int(input("Enter the first number: "))

# Input for the second number and convert it to an integer
second_number = int(input("Enter the second number: "))

# Check if the first number is greater than 30 and the second is less than 40
if first_number > 30 and second_number < 40:
    print("The first number is greater than 30 and the second number is less than 40.")
else:
    print("The first number is not greater than 30 or the second number is not less than 40.")
