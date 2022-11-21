from client import Client

class SuperVklad(Client):

    def __init__(self, name, summa, percent, period):
        super().__init__(name, summa, percent, period)

    def vklad(self):
        if self.summa > 500000:
            total = (self.summa * self.percent) / 100 + self.summa
            return f"Предложение от банка: Бонусный вклад. \nИтоговая сумма: {total}"
        else:
            total = super().vklad()
            return total


class CapitalVklad(Client):
    def __init__(self, name, summa, percent, period):
        super().__init__(name, summa, percent, period)

    def vklad(self):

        total = self.summa * (1 + self.percent) * self.period
        return f"Предложение от банка: Вклад с капитализацией процентов. \nИтоговая сумма: {total}"
