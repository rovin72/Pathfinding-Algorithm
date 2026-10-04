MAPGRAPH=[[-1, 1, 1, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 5,-1,-1,-1,-1,-1],
        [-1,-1,-1, 5,-1,-1,-1,-1,-1],
        [-1,-1,-1, 5,-1,-1,-1,-1,-1],
        [-1,-1,-1, 5,-1,-1,-1,-1,-1],
        [-1,-1,-1, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 1, 1,-1,-1,-1,-1,-1],
        [ 1, 1, 1, 1,-1,-1,-1,-1,-1],
        [ 1, 1, 1, 1,-1,-1,-1,-1,-1],
        [ 1,-1,-1, 5, 5, 5, 5,-1,-1],
        [ 1,-1,-1, 5, 5, 5, 5,-1,-1],
        [ 1, 5, 5, 5, 1, 1, 5,-1,-1],
        [ 5, 5, 5, 5, 5, 5, 5,-1,-1],
        [-1, 5, 5,-1,-1,-1, 5,-1,-1],
        [-1, 5, 5, 5,-1,-1, 5,-1,-1],
        [-1,-1,-1, 5, 5, 5, 5,-1,-1],
        [-1,-1,-1, 5, 1, 5, 5,-1,-1],
        [-1, 5, 5, 5, 1,-1,-1,-1,-1],
        [-1, 5, 5, 5, 1,-1,-1,-1,-1],
        [-1,-1,-1, 5, 1, 1, 1,-1,-1],
        [-1,-1,-1, 5, 5, 5, 1,-1,-1],
        [-1, 5, 1, 5,-1,-1, 1,-1,-1],
        [-1, 5, 5, 1,-1,-1, 1,-1,-1],
        [ 1, 5, 5, 5, 5, 1, 5,-1,-1],
        [-1,-1,-1, 5, 1, 1, 1,-1,-1],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [-1, 5, 5, 5, 5, 5, 5, 5, 5],
        [-1, 5, 5, 5, 5, 5, 5, 5, 5],
        [-1, 5, 5, 5, 5, 1, 5, 5, 5],
        [-1, 5, 1, 1, 5, 5, 5, 5, 1],
        [-1, 1, 5, 5,-1,-1, 5,-1,-1],
        [-1, 5, 5, 5,-1,-1, 5,-1,-1],
        [-1, 5, 5, 5, 5, 5, 5,-1,-1],
        [ 1,-1,-1, 5, 5, 5, 5,-1,-1],
        [ 1, 1, 1, 1, 5, 5, 5,-1,-1],
        [ 1, 1, 1, 1, 5, 5, 5,-1,-1],
        [ 1, 1, 1, 1,-1,-1,-1,-1,-1],
        [ 5, 1, 1, 1,-1,-1,-1,-1,-1],
        [ 5, 5, 1, 1,-1,-1,-1,-1,-1],
        [-1, 5, 1, 1,-1,-1,-1,-1,-1],
        [-1, 1, 1, 1,-1,-1,-1,-1,-1],
        [-1, 5, 1, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 5,-1,-1,-1,-1,-1],
        [-1, 5, 5, 5,-1,-1,-1,-1,-1],
        [-1, 5, 5, 5,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 5, 5,-1,-1,-1,-1,-1,-1],
        [-1, 5, 5,-1,-1,-1,-1,-1,-1],
        [-1, 5, 5,-1,-1,-1,-1,-1,-1],
        [-1, 1, 5,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 5, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 1,-1,-1,-1,-1,-1,-1],
        [-1, 1, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 1, 1,-1,-1,-1,-1,-1],
        [-1, 5, 1, 5,-1,-1,-1,-1,-1],
        [-1, 1, 1, 1,-1,-1,-1,-1,-1],
        [-1, 1, 5, 1,-1,-1,-1,-1,-1],
        [-1, 5, 1, 1,-1,-1,-1,-1,-1],
        [-1, 1, 1, 1,-1,-1,-1,-1,-1],
        [-1,-1, 1, 1,-1,-1,-1,-1,-1]]


class position():
    def __init__(self, x,y,score,tempscore=float('inf')):
        self.x=x
        self.y=y
        self.score=score
        self.neighbours=[]   
        self.tempscore=tempscore
        self.currentpath=[]

def main():
    startpos=(2,0)
    endpos=(2,77)
    posMap=[]
    for i in range(len(MAPGRAPH)):
        rowPos=[]
        for j in range(len(MAPGRAPH[i])):
            currentpos=position(j,i,MAPGRAPH[i][j])
            rowPos.append(currentpos)
        posMap.append(rowPos)

    for i in range(len(posMap)):
        for j in range(len(posMap[i])):
            if posMap[i][j].score<0:
                continue
            currentpos=posMap[i][j]
            #computes neighbours
            if j>0:
                if posMap[i][j-1].score>=0:
                    currentpos.neighbours.append(posMap[i][j-1])
            if i>0:
                if posMap[i-1][j].score>=0:
                    currentpos.neighbours.append(posMap[i-1][j])
            if j<(len(posMap[i])-1):
                if posMap[i][j+1].score>=0:
                    currentpos.neighbours.append(posMap[i][j+1])
            if i<(len(posMap)-1):
                if posMap[i+1][j].score>=0:
                    currentpos.neighbours.append(posMap[i+1][j])


    currentNode=posMap[startpos[1]][startpos[0]]
    currentNode.tempscore=currentNode.score
    currentNode.currentpath=[(currentNode.x,currentNode.y)]

    exploredNodes=set()

    exploringNodes=[]

    exploringNodes.append(currentNode)
    while True:
        for i in currentNode.neighbours:
            if i not in exploredNodes:
                updatedscore=i.score+currentNode.tempscore
                if updatedscore<i.tempscore:
                    if i.tempscore==float('inf'):
                        exploringNodes.append(i)
                        
                    i.tempscore=updatedscore
                    i.currentpath=[*currentNode.currentpath,(i.x,i.y)]
                    currentlocation=exploringNodes.index(i)

                    while i.tempscore<exploringNodes[parent(currentlocation)].tempscore:
                        exploringNodes[parent(currentlocation)],exploringNodes[currentlocation]=exploringNodes[currentlocation],exploringNodes[parent(currentlocation)]
                        currentlocation=parent(currentlocation)

        exploredNodes.add(currentNode)

        if len(exploringNodes)>1:
            exploringNodes[0]=exploringNodes.pop()
        else:
            break

        currentlocation=0
        
        while True:
            smallest=currentlocation
            leftChild=2*currentlocation+1
            rightChild=2*currentlocation+2
            if leftChild>=len(exploringNodes):
                break
            elif rightChild>=len(exploringNodes):
                if exploringNodes[leftChild].tempscore<=exploringNodes[currentlocation].tempscore:
                    exploringNodes[currentlocation],exploringNodes[leftChild]=exploringNodes[leftChild],exploringNodes[currentlocation]
                break
            else:
                if exploringNodes[leftChild].tempscore<exploringNodes[smallest].tempscore:
                    smallest=leftChild
                if exploringNodes[rightChild].tempscore<exploringNodes[smallest].tempscore:
                    smallest=rightChild
                if smallest==currentlocation:
                    break
                else:
                    exploringNodes[currentlocation],exploringNodes[smallest]=exploringNodes[smallest],exploringNodes[currentlocation]
                    currentlocation=smallest



        currentNode=exploringNodes[0]

        if currentNode.x==endpos[0] and currentNode.y==endpos[1]:
            break
    print(posMap[endpos[1]][endpos[0]].currentpath)


        


def parent(location):
    return (location-1)//2
                    
          
main()



