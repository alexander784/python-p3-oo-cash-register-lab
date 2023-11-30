#!/usr/bin/env python3


class CashRegister:
  def __init__(self, discount=0):
    ##initialize discount attribute with value passed as an argument
    self.discount = discount
     ##total attribute = 0
    self.total = 0
    ##Store items added to cash register
    self.items = []
    #store information about previous transactions
    self.previous_transactions = []
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
        ##Calculate cost of items and add to the running total
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(item)        
      self.previous_transactions.append({"item": item, "quantity": quantity, "price": price})    

  def apply_discount(self):
    ##Check discount
    if self.discount:
      #Calculate Discounted Total
      self.total = int(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")


##Handle void transaction
  def void_last_transaction(self):
    if not self.previous_transactions:
      return "There are no transactions to void."
    self.total -= (
      self.previous_transactions[-1]["price"]
        * self.previous_transactions[-1]["quantity"]
        )
    for _ in range(self.previous_transactions[-1]["quantity"]):
      self.items.pop()
    self.previous_transactions.pop()