from contextlib import nullcontext
from imghdr import what


class BillCalculator:
    def __init__(self, bill, tipPer, howManyPeople):
        self.bill = bill
        self.tipPer = tipPer
        self.howManyPeople = howManyPeople

    def calBill(self):
        print(
            f"Bill : {self.bill} \nTip Percent : {self.tipPer} \nHow many people Split : {self.howManyPeople}")
        self.onePer = self.bill / 100
        self.tip = self.tipPer * self.onePer
        self.bill += self.tip
        self.eachBill = self.bill / self.howManyPeople
        self.eachBill = round(self.eachBill, 2)
        return "{:.2f}".format(self.eachBill)


print("Welcome to the tip Calculator.")
bill = input("What was the total Bill? : $")
tipPer = input(
    "What percentage tip would you like to give? 10 12 or 15 : ")
howManyPeople = input("How many people to split the bill? : ")
O = BillCalculator(float(bill), int(tipPer), int(howManyPeople))

print(O.calBill())
