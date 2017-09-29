
class Action:
    _rock = 0
    _paper = 1
    _scissors = 2

    def __init__(self, actionType):
        self.actionType = actionType

    def __eq__(self, action):
        return type(self) == type(action) and self.actionType == action.actionType

    def __gt__(self, action):
        if (self.actionType == Action._rock and action.actionType == Action._scissors):
            return True
        if (self.actionType == Action._paper and action.actionType == Action._rock):
            return True
        if self.actionType == Action._scissors and action.actionType == Action._paper:
            return True
        return False

    def __str__(self):
        if (self.actionType == Action._rock):
            return "rock"
        if (self.actionType == Action._paper):
            return "paper"
        if (self.actionType == Action._scissors):
            return "scissors"
