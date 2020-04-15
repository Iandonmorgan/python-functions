def calc_dollars(**coins):
    # The function should look at each key (pennies, 
    # nickels, dimes and quarters) and perform the 
    # appropriate math on the integer value to determine 
    # how much money you have in dollars. Store that value 
    # in a variable named `dollarAmount` and print it.
    total = 0
    for key, value in coins.items():
        if key == "pennies":
            total += value
        elif key == "nickels":
            total += (value * 5)
        elif key == "dimes":
            total += (value * 10)
        elif key == "quarters":
            total += (value * 25)
    print(f'${(total/100):.2f}')        

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)