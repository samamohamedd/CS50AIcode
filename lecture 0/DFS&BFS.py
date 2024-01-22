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