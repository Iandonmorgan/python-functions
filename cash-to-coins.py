dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def calc_coins(num):
    number = num * 100
    while number > 0:
        if number % 25 == 0:
            number -= 25
            piggyBank["quarters"] += 1
        elif number % 10 == 0:
            number -= 10
            piggyBank["dimes"] += 1
        elif number % 5 == 0:
            number -= 5
            piggyBank["nickels"] += 1
        else:
            number -= 1
            piggyBank["pennies"] += 1

    print(piggyBank)

calc_coins(dollarAmount)