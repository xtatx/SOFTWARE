from car import Car
from account import Account
from uberX import UberX
from user import User

if __name__ == "__main__":
    print("Inicializando la info de los carros")

    print("Car")
    car = Car("AMS256", Account("Andres Herrera", "ASD12365", "fernandeztatiana011@gmail.com", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberx = UberX("KLO365", Account("Marco Lois", "SGHJ1236", "fernandeztatiana011@gmail.com", "7856"), "Toyota", "Corolla")
    print(vars(uberx))
    print(vars(uberx.driver))

    print("User")
    user = User("Mariana Valle", "SDFG125F", "fernandeztatiana011@gmail.com", "7856")
    print(vars(user))
