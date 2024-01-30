import sys

class Node:
    def __init__(self,state,parent,action ) -> None:
        self.parent = parent
        self.state = state
        self.action = action

class StackFrontier:
    #4 dfs 
    def __init__(self) -> None:
        frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contain_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier)==0
    
    def remove(self):
        if len(self.frontier)==0:
            raise Exception("empty frontier")
        else :
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1] 
            return node
        
class queueFrontier(StackFrontier):

    def remove(self):
        if len(self.frontier)==0:
            raise Exception("empty frontier")
        else :
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
class maze:

    def __init__(self, filename) -> None:
        #properties: height, width, walls, start, end, solution

        with open(filename) as f:
            contents = f.read()
        
        #validating the start and goal points
        if contents.count("S") != 1:
            raise Exception ("the maze should have one starting point")
        if contents.count("G") != 1:
            raise Exception ("the maze should have one goal point")
        
        contents = contents.splitlines()
        self.height = len(contents)
        #calculate each line length and return the biggest(the max)
        self.width = max(len(line)for line in contents)

        #tracking the walls, start, and goal
        self.walls = [] #this wall variable: each element is a row,  
        for i in range (self.height):
            wallsInRow=[]
            for j in range(self.width):
                try:
                    if contents[i][j] == "S":
                        self.start = (i,j)
                        wallsInRow.append(False)
                    elif contents[i][j] == "G":
                        self.end =(i,j)
                        wallsInRow.append(False)
                    elif contents[i][j] == " ":
                        wallsInRow.append(False)
                    else:
                        wallsInRow.append(True)
                except IndexError:
                    wallsInRow.append(False)
                self.walls.append(wallsInRow)

        self.solution = None

    def neighbors(self, state):        
        row, col = state
        candidates = [
            ("up",(row-1,col)),
            ("down",(row+1,col)),
            ("right",(row,col+1)),
            ("left",(row,col-1))
        ]

        #result var will help determine if a position is on an edge or not 
        # also will help what are the walls around this neighbor
        result = []
        for action , (r,c) in candidates: #getting data from the candidatets list
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append(((action , (r,c))))
        return result
    
    def print(self):
        solution = self.solution if self.solution[1] is not None else None
        print()
        for i,row in enumerate(self.walls):
            for j,col in enumerate(row):
                if col :
                    print("█", end="")
                elif (i,j) == self.start:
                    print("S", end="")
                elif (i,j) == self.end:
                    print("G", end="")
                elif self.solution is not None and (i,j) in self.solution:
                    print("*", end="")
            print()
        print()

    
    def solve(self):
        
        self.exploredNum = 0 #number of states explored
        self.explored = set() #set of items exeplored
        
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier
        frontier.add(start)

        while True:

            if frontier.empty():
                raise Exception("there's no solution")
            
            node = frontier.remove()
            self.exploredNum += 1


        