class CashRegister:
  def __init__(self, discount=0, price=0):
    self._discount = discount
    self.total = 0
    self.items = []
    self.price = price
    self.prices = []
    
  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.quantity = quantity
    self.items.extend([title] * quantity)    
    self.prices.extend([price] * quantity)
    
  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, new_discount):
    if hasattr(self, 'total'):
        self.total = self.total * (100 - new_discount) / 100 
    else:
        self.total = 0

    
  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total * (100 - self._discount) / 100
      print(f'After the discount, the total comes to ${int(self.total)}.')
    
    else:
      print('There is no discount to apply.')
      
  def new_register_items(self):
    return self.items
  
  def void_last_transaction(self):
    if self.items:
        last_item_index = len(self.items) - 1
        last_item_price = self.prices[last_item_index]
        self.total -= last_item_price * self.quantity
        del self.items[last_item_index]
        del self.prices[last_item_index]
    else:
        print("No items to void.")
        self.total = 0.0