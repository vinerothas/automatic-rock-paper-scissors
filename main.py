import plotly.graph_objs as go
from plotly.offline import plot
from player import *

class SingleGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        a1 = self.player1.chooseAction()
        a2 = self.player2.chooseAction()
        result = str(self.player1) + ": " + str(a1) + ". " + str(self.player2) + ": " + str(a2) + " -> "
        if a1 == a2:
            result += "Draw"
        elif a1 > a2:
            result += str(self.player1) + " won"
        else:
            result += str(self.player2) + " won"
        print(result)


class MultipleGames:
    def __init__(self, player1, player2, games):
        self.player1 = player1
        self.player2 = player2
        self.games = games
        self.points1 = 0
        self.points2 = 0
        self.pointRatio = [0]
        self.gameCounter = 1

    def playSingle(self):
        a1 = self.player1.chooseAction()
        a2 = self.player2.chooseAction()
        result = "Game#"+str(self.gameCounter)+": "+str(self.player1) + ": " + str(a1) + ". " + str(self.player2) + ": " + str(a2) + " -> "
        if (a1 == a2):
            result += "Draw"
            self.points1 += 0.5
            self.points2 += 0.5
        elif (a1 > a2):
            result += str(self.player1) + " won"
            self.points1 += 1
        else:
            result += str(self.player2) + " won"
            self.points2 += 1
        print(result)
        self.player1.receiveAction(a2)
        self.player2.receiveAction(a1)

    def playTournament(self):
        while self.gameCounter <= self.games:
            self.playSingle()
            self.gameCounter += 1
            if(self.points2!=0):
                self.pointRatio.append(self.points1 / (self.points2+self.points1))
            else:
                self.pointRatio.append(1)

        xValues = []
        for x in range(0, self.games+1):
            xValues.append(x)
        trace = go.Scatter(x= xValues,y =self.pointRatio)
        data = [trace]
        plot(data, filename='graph.html')


def main():
    print("Type of game: 1 - single, 2 - multiple")
    print("Choose type of game")
    gameType = int(input())
    p1 = getPlayer(1)
    p2 = getPlayer(2)
    if gameType == 1:
        game = SingleGame(p1, p2)
        game.play()
    elif (gameType == 2):
        print("\nChoose number of games")
        games = int(input())
        game = MultipleGames(p1,p2,games)
        game.playTournament()


def getPlayer(number):
    while (True):
        print('\nPlayer#'+str(number))
        print("Type of player: 1 - random, 2 - sequential, 3 - mostCommon, 4 - historian")
        print("Choose player type")
        playerType = int(input())
        if playerType == 4:
            print("Choose memory for historian")
            memory = int(input())
            return Player(Player._historian, number, memory)
        else:
            return Player(playerType - 1, number)

main()
