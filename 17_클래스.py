class Character:
    def __init__(self, hp, mp):
        self.hp = hp
        self.mp = mp
        self.height = 100
        
    def fireball(self):
        print('파이어볼을 발사합니다.')

lupi = Character(500, 999)
print(lupi.hp)
print(lupi.height)

lupi.fireball()