class Enemy:
    life = 3

    def attack(self):
        self.life -= 1
        print("Ouch that hurts")

    def check(self):
        print("Your health is at", self.life)



e1 = Enemy()
e2 = Enemy()

e1.attack()
e2.attack()
e2.attack()
e2.check()
e1.check()