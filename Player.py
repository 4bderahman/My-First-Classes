class Player:
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank

    def pass_ball(self):
        print(f"{self.name} passes the ball!")

    def shoot(self):
        print(f"{self.name} shoots towards the goal!")

    def jump(self):
        print(f"{self.name} jumps for the header!")

player1 = Player("Hakimi", 25, 1)
player1.pass_ball()
player1.shoot(   )
player1.jump()