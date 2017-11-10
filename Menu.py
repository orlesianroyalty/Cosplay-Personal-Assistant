import urllib
import numpy as np 

print("Hello, I'm your cosplay personal assistant!")
print("How can I can help you today?")

class Budget:
    spent = 0
    available = 0
    totalBudget = 0
    bought = []

    def getTotalBudget():
        return totalBudget

    def setTotalBudget(number):
        totalBudget = number

    def getSpent() {
        return spent
    }

    def getAvailable() {
        return available
    }

    def spendMoney(number) {
        spent += number
        available - spent
    }

    def addBoughtItem(boughtItem) {
        bought.append(boughtItem)
    }


class boughtItems:
    name = ""
    price = 0
    
    def setName(string):
        name = string

    def getName():
        return name

    def setPrice(number):
        price = number

    def getPrice():
        return price    