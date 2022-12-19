class account:

    # _<var name> defines this SHOULD BE PRIVATE
    _pin = "1234"
    _money = 500
    _password = "password"

    # Getter
    def displayMoney(self, password):
        if password == self._password:
            return self._money
        else:
            return "Invalid Password!"

    # Setter
    def withdrawMoney(self, pin, amount):
        if pin == self._pin:
            self._money -= amount
            return self._money
        else:
            return "Invalid PIN"


demoAccount = account()
print(demoAccount)
print(demoAccount.displayMoney("password"))
print(demoAccount.withdrawMoney("1234", 210))

