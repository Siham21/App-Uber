from Car import Car
if __name__=="__main__":
    print("hello world")
    car = Car()
    car.licence = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.licence = "ATZ123"
    car2.driver = "Andrea Herrera"
    print(vars(car2))

