class game:

    def __init__(self) -> None:
        intialState = [
            [" " , " " , " "],
            [" " , " " , " "],
            [" " , " " , " "]
        ]

        self.height = 3
        self.width = 3

    def player(self, state):
        countX = 0
        countO = 0
        for row in state :
            for item in row :
                if item == "X": countX += 1
                if item == "O": countO += 1
        if countX <= countO:
            return "X"
        return "O"
    
    def actions(self, state):
        actions =[]
        for i, row in enumerate(state) :
            for j,item in enumerate(row) :
                if item == " ": actions.append((i,j))
        return actions

    def result(self, state, action):
        r, c = action[0], action[1]
        state[r][c] = self.player()
        return state
    
    def terminate(self, state):
        pass

