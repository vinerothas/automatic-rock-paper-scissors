from action import *
import random

class Player:
    # player types
    _random = 0
    _sequential = 1
    _mostCommon = 2
    _historian = 3
    _names = ['random', 'sequential', 'mostCommon', 'historian']

    def __init__(self, playerType, number, memory=1):
        self.playerType = playerType
        self.number = number
        if(playerType == Player._sequential):
            self.lastMove = None
        if(playerType == Player._mostCommon):
            self.opponentMoves = [0, 0, 0]
        if(playerType == Player._historian):
            self.history = []
            self.memory = memory

    def __str__(self):
        if self.playerType == Player._historian:
            return Player._names[self.playerType] + "#" + str(self.number) + '(' + str(self.memory) + ')'
        return Player._names[self.playerType] + "#" + str(self.number)

    def chooseAction(self):
        if (self.playerType == Player._random):
            return Action(random.randint(0, 2))

        elif (self.playerType == Player._sequential):
            if (self.lastMove is None or self.lastMove == Action._scissors):
                self.lastMove = Action._rock
                return Action(Action._rock)
            elif (self.lastMove == Action._rock):
                self.lastMove = Action._paper
                return Action(Action._paper)
            elif (self.lastMove == Action._paper):
                self.lastMove = Action._scissors
                return Action(Action._scissors)

        elif (self.playerType == Player._mostCommon):
            return Player.findMostPlayedCounter(self.opponentMoves)

        elif (self.playerType == Player._historian):
            if(len(self.history)<= self.memory):
                return Action(random.randint(0, 2))
            pattern = []
            mostPlayed = [0,0,0]
            #retrieve latest pattern
            for x in range(len(self.history)-self.memory,len(self.history)):
                pattern.append(self.history[x])
            #check the whole history for occurrences of the patter
            for x in range(0,len(self.history)-self.memory):
                match = True
                #for each element in history, check if it becomes a pattern
                for y in range(0,self.memory):
                    if(self.history[x+y] != pattern[y]):
                        match = False
                        break
                if match :
                    #if pattern found then save the next action played after the pattern
                    mostPlayed[self.history[x+self.memory]] += 1
            return Player.findMostPlayedCounter(mostPlayed)


    def receiveAction(self, action):
        if(self.playerType == Player._mostCommon):
            self.opponentMoves[action.actionType]+=1
        elif(self.playerType == Player._historian):
            self.history.append(action.actionType)

    # occurrences: an array containing number of rock, paper, and scissors played by opponent
    # returns: counter to the most common action or random if not available
    @staticmethod
    def findMostPlayedCounter(occurrences):
        if (occurrences[Action._rock] > occurrences[Action._paper]
            and occurrences[Action._rock] > occurrences[Action._scissors]):
            return Action(Action._paper)
        if (occurrences[Action._paper] > occurrences[Action._rock]
            and occurrences[Action._paper] > occurrences[Action._scissors]):
            return Action(Action._scissors)
        if (occurrences[Action._scissors] > occurrences[Action._paper]
            and occurrences[Action._scissors] > occurrences[Action._rock]):
            return Action(Action._rock)
        else:
            return Action(random.randint(0, 2))