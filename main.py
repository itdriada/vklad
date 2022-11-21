from client import Client
from vklad import SuperVklad, CapitalVklad

if __name__ == '__main__':

    ivan = Client('Иван Петров', 400000, 8, 12)
    elena = SuperVklad('Елена Петрова', 600000, 9, 12)
    ekaterina = SuperVklad('Екатерна Долгова', 450000, 8, 16)
    sergey = CapitalVklad('Сергей Иванов', 670000, 12, 14)

    print(ivan)
    print(ivan.vklad(), '\n')
    print(elena)
    print(elena.vklad(), '\n')
    print(ekaterina)
    print(ekaterina.vklad(), '\n')
    print(sergey)
    print(sergey.vklad(), '\n')