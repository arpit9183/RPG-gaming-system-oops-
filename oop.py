import time


class Player:
    def __init__(self,health,level,weapon):
        self.health=health
        self.level=level
        self.weapon=weapon

    def attack(self,Enemy):
        Enemy.health -= self.weapon.damage
        if Enemy.health<=0:
            self.level += Enemy.level

    def heal(self):
        if self.level>1:
            if self.health<=50:
                self.level -= 1
                self.health += 50
            else:
                print("you have enough health\nGo on soldier")
        else:
            print("Not enough levels \n minimum 2 level required")

    def change_weapon(self):
        if self.level >5:
            for i in weapons:
                Weapon.display(i)
            ch=int(input("make your choice(1/2/3/4)"))
            if ch==1:
                print("already selected")
                return Player.change_weapon(player)
            if ch==2 and player.level>=5:
                player.weapon=axe
                player.level -= axe.cost
            if ch==3 and player.level>=10:
                player.weapon=machete
                player.level -= machete.cost
            if ch==4 and player.level>=20:
                player.weapon=katana
                player.level -= katana.cost

    def display(self):
        print("HEALTH->", self.health, "LEVEL->", self.level, "WEAPON->")
        Weapon.display(self.weapon)




class Enemy:
    def __init__(self,name,health,damage,level):
        self.name=name
        self.health=health
        self.damage=damage
        self.level=level

    def attack_player(self,Player):
        Player.health -= self.damage

    def display(self):
        print("NAME->",self.name ,"DAMAGE->", self.damage ,
              "LEVEL->", self.level,"HEALTH->100")



class Weapon:
    def __init__(self,name,damage,cost):
        self.name=name
        self.damage=damage
        self.cost=cost

    def display(self):
        print("NAME->",self.name ,"DAMAGE->", self.damage ,
              "COST->", self.cost)




stick=Weapon('stick',20,1)
player=Player(health=100,level=1,weapon=stick)

axe=Weapon('axe',30,5)
machete=Weapon('machete',40,10)
katana=Weapon('katana',50,20)

goblin = Enemy('goblin',100,15,1)
samurai = Enemy('samurai',100,25,5)
fighter = Enemy('fighter',100,45,10)

weapons=[stick,axe,machete,katana]
enemy=[goblin,samurai,fighter]


play_again = "y"

while play_again == "y":

    print("stats of your player")
    Player.display(player)

    print("select enemy")

    choice=input("goblin/samurai/fighter:")

    if choice == "goblin":
        choice = goblin
    elif choice == "samurai":
        choice = samurai
    elif choice == "fighter":
        choice = fighter

    if choice in enemy:

        print("lets start the battle")

        i=1

        while player.health >0 and choice.health >0:

            print("round", i)

            print("player is attacking")
            player.attack(choice)

            print("enemy is attacking")
            Enemy.attack_player(choice,player)

            print("round", i , "results")
            print("player health=",player.health,
                  "enemy health",choice.health)

            i +=1

            count=3

            while count>0:
                print(count)
                time.sleep(1)
                count-=1

        if player.health<=0:
            print("you lost\nGAME OVER")
            break

        else:
            print("you won the match and are rewarded with ",
                choice.level,"levels")

            heal=input("do you want to heal(y/n)")

            if heal=='y':
                Player.heal(player)
            else:
                print("ok")

        if player.level >= 5:
            change = input("Do you want to change weapon? (y/n): ")

            if change=='y':
                player.change_weapon()

    else:
        print("make valid choice")

    play_again = input("Do you want to fight again? (y/n): ").lower()

    if play_again == "y":
        goblin.health = 100
        samurai.health = 100
        fighter.health = 100