import sys

class node:
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
        self.walls = []
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

                

                        


        