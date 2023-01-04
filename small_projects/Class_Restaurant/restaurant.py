import random


class Restaurant:

    date = 1
    workers = random.randint(1, 5)
    wage = 15

    def __init__(self, restaurant_name, restaurant_fund):
        self.restaurant_name = restaurant_name
        self.restaurant_fund = restaurant_fund
        print('A new restaurant named', self.restaurant_name+'!')
        print('Your have $', self.restaurant_fund, 'fund')

    def next_day(self):
        print('Day'+str(Restaurant.date)+':')
        Restaurant.date += 1
        self.restaurant_fund += Restaurant.today_profit() - Restaurant.workers_wage()

        print('Your fund:', self.restaurant_fund)

    @staticmethod
    def workers_wage():
        Restaurant.wages = Restaurant.workers*Restaurant.wage
        print('Today workers wages: $'+str(Restaurant.wages))
        return Restaurant.wages

    @staticmethod
    def today_profit():
        Restaurant.profit = random.randint(-500, 500)
        print('Today profit from food is: $'+str(Restaurant.profit))
        return Restaurant.profit
