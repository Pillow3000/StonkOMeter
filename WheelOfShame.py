
import json
import random


def ChangeStock(currentStock, currentOwner):

    owners, stocks = [], []

    with open("StockData.json", 'r') as f:
        data = json.load(f)

        # Creates lists from data in JSON file
        for people in data:
            owners.append(people)

        # Takes Random Owner and checks if they're current Owner

        newOwner = random.choice(owners)

        if newOwner != currentOwner:
            pass
        else:
            ChangeStock(currentStock, currentOwner)

        for stock in data[newOwner]:

            stocks.append(stock)

        # Takes Random Stock and checks if it's current Stock
        newStock = random.choice(stocks)

        if newStock != currentStock:
            return newStock, newOwner
        else:
            ChangeStock(currentStock, currentOwner)
