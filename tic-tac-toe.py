class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        self.choice = input(f'{self.name}, введите координаты x,y от 1 до 3 без пробела ')
        return self.choice 

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rules = [['00','01','02'], ['10','11','12'], ['20','21','22'], 
                      ['00','10','20'], ['01','11','21'], ['02','12','22'],
                      ['00','11','22'], ['02','11','20']] 
 
    def get_winner1(self):
        if len(self.p1) == 3 and self.p1 in self.rules:
            player1.team = 'Крестики'
            return self.player1
        else:
            return None
        
    def get_winner2(self):
        if len(self.p2) == 3 and self.p2 in self.rules:
            player2.team = 'Нолики'
            return self.player2
        else:
            return None
             

    def play(self):
        count1 = 0
        count2 = 0
        self.p1 = []
        self.p2 = []
        while count1 != 3:
            v1 = self.player1.choose()
            if v1 not in self.p1 and v1 not in self.p2:
                self.p1.append(v1)
                count1 += 1
                if count1 == 3:
                    self.p1 = sorted(self.p1)
                    winner = self.get_winner1()
                    if winner:
                        break
            else:
                print('Эти координаты x,y уже были. Переход хода.')
            v2 = self.player2.choose()
            if v2 not in self.p1 and v2 not in self.p2:
                self.p2.append(v2)
                count2 += 1
                if count2 == 3:
                    self.p2 = sorted(self.p2)
                    winner = self.get_winner2()
                    if winner:
                        break
            else:
                print('Эти координаты x,y уже были введены. Переход хода.')
        if winner:
            print(f"{winner.name} из команды {winner.team} победил!")
        else:
            print("У нас ничья.")


# Пример использования
player1 = Player('Игрок 1')
player2 = Player('Игрок 2')
game = Game(player1, player2)
game.play()
