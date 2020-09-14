# Write your code here


class CoffeeMachine():
    coffee_types = ['espresso', 'latte', 'cappuccino']
    coffee_data = {'espresso': [250, 0, 16, 4], 'latte': [350, 75, 20, 7],
                   'cappuccino': [200, 100, 12, 6]}

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def print_state(self):
        print('\nThe coffee machine has:\n\
{} of water\n\
{} of milk\n\
{} of coffee beans\n\
{} of disposable cups\n\
{} of money'''.format(self.water, self.milk, self.beans, self.cups, self.money))

    def buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, '
              'back - to main menu:')
        option = input()
        if option == 'back':
            return
        ctype = self.coffee_types[int(option) - 1]
        required_water = self.coffee_data[ctype][0]
        required_milk = self.coffee_data[ctype][1]
        required_beans = self.coffee_data[ctype][2]
        price = self.coffee_data[ctype][3]
        if self.water < required_water:
            print('Sorry, not enough water!')
            return
        if self.milk < required_milk:
            print('Sorry, not enough milk!')
            return
        if self.beans < required_beans:
            print('Sorry, not enough coffee beans!')
            return
        if self.cups == 0:
            print('Sorry, not enough cups!')
            return

        print('I have enough resources, making you a coffee!')

        self.water -= required_water
        self.milk -= required_milk
        self.beans -= required_beans
        self.money += price
        self.cups -= 1

    def fill(self):
        print('\nWrite how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())

    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0

    def operate(self):
        while True:
            print('\nWrite action (buy, fill, take, remaining, exit):')
            action = input()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.print_state()
            elif action == 'exit':
                return



coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.operate()