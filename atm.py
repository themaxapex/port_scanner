def atm_withdrawl(balance, amount):
    if amount > balance:
        return "no suffisient fund", balance
    elif amount <= 0:
        return "invalid number", balance
    else:
        balance -= amount
        return "transaction successfull", balance
print(atm_withdrawl(160, 150))

