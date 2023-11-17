class Car:
    def __init__(self, speed, engine_power, color, model):
        self.speed = speed
        self.color = color
        self.nitro_speed = False
        self.model = model
        self.engine_power = engine_power

    def turn(self, direction):
        print(f"The {self.model} turns {direction}.")

    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.model} accelerates to {self.speed} km/h.")

    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        print(f"The {self.model} slows down to {self.speed} km/h.")

    def start(self):
        print(f"{self.model} starts with engine power {self.engine_power}.")

    def stop(self):
        self.speed = 0
        print(f"{self.model} stops.")

    def change_gear(self, gear):
        print(f"{self.model} changes to gear {gear}.")

Car = Car(120, 500, "blue", "Mustang")
Car.start()
Car.accelerate(50)  
Car.change_gear(3)
Car.brake(10)  
Car.stop()
