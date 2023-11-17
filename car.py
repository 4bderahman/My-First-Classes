class Car:
    def __init__(self, speed, color, nitro_speed, model):
        self.speed = speed
        self.color = color
        self.nitro_speed = nitro_speed
        self.model = model

    def turn(self, direction):
        print(f"The car turns {direction}")

    def accelerate(self):
        self.speed += 10
        print(f"The car accelerates to {self.speed} km/h")

    def brake(self):
        self.speed -= 10
        print(f"The car slows down to {self.speed} km/h")

    def boost(self):
        if self.nitro_speed:
            self.speed += 50
            print(f"Boost activated! Speed is now {self.speed} km/h")

car1 = Car(200, "red", True, "Porche")
car1.turn("left")
car1.accelerate()
car1.brake()
car1.boost()