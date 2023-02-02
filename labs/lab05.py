# lab05: OOP, inheritance

from operator import add, sub


# disc05: https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc05/

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard: # q1
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.
    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) # No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        """YOUR CODE HERE"""
        self.buttons = {}
        for button in args:
            self.buttons[button.pos]=button


    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output."""

        """YOUR CODE HERE"""
        if info not in self.buttons:
            return ''
        self.buttons[info].times_pressed += 1
        return self.buttons[info].key


    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""

        """YOUR CODE HERE"""
        output = ''
        for info in typing_input:
            output += self.press(info)
        return output

# lab04: https://inst.eecs.berkeley.edu/~cs61a/su22/lab/lab04/

class Minty: 
    """A mint creates coins by stamping on years. The update method sets the mint's stamp to Minty.present_year.
    >>> mint = Minty()
    >>> mint.year
    2021
    >>> dime = mint.create('Dime')
    >>> dime.year
    2021
    >>> Minty.present_year = 2101  # Time passes
    >>> nickel = mint.create('Nickel')
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Minty.present_year = 2176     # More time passes
    >>> mint.create('Dime').worth()    # 10 cents + (75 - 50 years)
    35
    >>> Minty().create('Dime').worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, type):
        "*** YOUR CODE HERE ***"
        return Coin(self.year, type)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = Minty.present_year

class Coin: # q2
    cents = 50

    def __init__(self, year, type):
        "*** YOUR CODE HERE ***"
        self.year = year
        self.type = type
        

    def worth(self):
        "*** YOUR CODE HERE ***"
        val = 0
        if self.type == 'Dime':
            val = 10
        if self.type == 'Nickel':
            val = 5
        if Minty.present_year == self.year:
            return val
        return val + Minty.present_year - self.year - Coin.cents


# hw04: https://inst.eecs.berkeley.edu/~cs61a/su22/hw/hw04/

class SmartFridge: # q3
    """"
    >>> fridgey = SmartFridge()
    >>> fridgey.add_item('Mayo', 1)
    'I now have 1 Mayo'
    >>> fridgey.add_item('Mayo', 2)
    'I now have 3 Mayo'
    >>> fridgey.use_item('Mayo', 2.5)
    'I have 0.5 Mayo left'
    >>> fridgey.use_item('Mayo', 0.5)
    'Oh no, we need more Mayo!'
    >>> fridgey.add_item('Eggs', 12)
    'I now have 12 Eggs'
    >>> fridgey.use_item('Eggs', 15)
    'Oh no, we need more Eggs!'
    >>> fridgey.add_item('Eggs', 1)
    'I now have 1 Eggs'
    """
    def __init__(self):
        self.items = {}
    def add_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if item not in self.items:
            self.items[item] = quantity
        else:
            self.items[item] += quantity
        return f'I now have {self.items[item]} {item}'
    def use_item(self, item, quantity):
        "*** YOUR CODE HERE ***"
        if (self.items[item] - quantity) <= 0:
            self.items[item] = 0
            return f'Oh no, we need more {item}!'
        else: 
            self.items[item] -= quantity
        return f'I have {self.items[item]} {item} left'

class VendingMachine: # q4
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please update your balance with $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please update your balance with $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.balance = 0
        self.stock = 0
    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock.'
        elif self.balance == self.price:
            self.balance = 0
            self.stock -= 1
            return f'Here is your {self.name}.'
        elif self.balance < self.price:
            return f'Please update your balance with ${self.price-self.balance} more funds.'
        elif self.balance > self.price:
            change = self.balance - self.price
            self.balance = 0
            self.stock -= 1
            return f'Here is your {self.name} and ${change} change.'
    def add_funds(self, amount):
        if self.stock == 0:
            return f'Nothing left to vend. Please restock. Here is your ${amount}.'
        self.balance += amount
        return f'Current balance: ${self.balance}'
    def restock(self, amount):
        self.stock += amount
        return f'Current {self.name} stock: {self.stock}'




    
# disc06: https://inst.eecs.berkeley.edu/~cs61a/su22/disc/disc06/

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Cat(Pet): # q5

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.life = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(f'{self.name} says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.life == 0:
            print ('This cat has no more lives to lose.')
        else:
            self.life -= 1


class NoisyCat(Cat): # q6
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()


# lab05: https://inst.eecs.berkeley.edu/~cs61a/su22/lab/lab05/

class Account: # q7
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount): # q6
        """Return the number of years until balance would grow to amount."""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        "*** YOUR CODE HERE ***"
        count = 0
        val = self.balance
        while val < amount:
            val += val*Account.interest
            count+=1
        return count


class FreeChecking(Account): # q8
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free
    'Insufficient funds'
    >>> ch.withdraw(3)    # And the second
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2

    "*** YOUR CODE HERE ***"
    def withdraw(self, amount):
        if self.free_withdrawals <= 0:
            return super().withdraw(amount+self.withdraw_fee)
        else:
            self.free_withdrawals -= 1
            return super().withdraw(amount)
    