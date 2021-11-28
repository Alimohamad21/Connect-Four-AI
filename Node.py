class Node:
    def __init__(self,  parent, score, max_or_min):

        self.max_or_min = max_or_min
        self.parent = parent
        self.score = score
        self.children = []

    def addChild(self,child):
        self.children.append(child)

    def getChildren(self):

        return self.children


    def printTree(self, iden_num):

        if self.max_or_min:
            my_string = "MAX"
        else:
            my_string = "MIN"
        print(iden_num*'\t', my_string, " Score: ", self.score)
        for child in self.children:
            child.printTree(iden_num+1)




