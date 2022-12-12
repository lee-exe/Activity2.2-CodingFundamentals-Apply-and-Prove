initial_investment = int(input("Initial investment: "))
target_value = int(input("Target value: "))
interest_rate = float(input("Interest rate: "))
new_value = initial_investment + (initial_investment * interest_rate)
years = 0

while new_value:
    years += 1
    new_value += new_value

    if new_value > target_value:
        break

print("It would take approximately {} years to reach your goal.".format(years))



