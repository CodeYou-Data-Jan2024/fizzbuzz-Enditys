for num in range(1,101):
    outcome = ""
    if num % 3 == 0:
        outcome = outcome + "Fizz"
    if num % 5 == 0:
        outcome = outcome + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        outcome = outcome + str(num)
    print(outcome)