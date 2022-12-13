user_salary = int(input("Please enter your salary: £"))
personal_allowance = 12570
tax_free_message = "You do not earn more than the National Personal Allowance.\n" \
                   "As a result, you will not be taxed this tax year."
tax_rates = [0.19, 0.3, 0.41, 0.46]


def incomeTax1(salary, allowance, tfm):
    income = salary
    pa = allowance

    if income > pa:
        if salary <= 23000:
            icTax = (salary - pa) * tax_rates[0]
        elif 23000 < salary <= 40000:
            icTax = (salary - pa) * tax_rates[1]
        elif 40000 < salary <= 15000:
            icTax = (salary - pa) * tax_rates[2]
        elif salary > 150000:
            icTax = (salary - pa) * tax_rates[3]
        print(f"Your yearly income tax is: {icTax}")
    else:
        print(tfm)


incomeTax1(user_salary, personal_allowance, tax_free_message)


