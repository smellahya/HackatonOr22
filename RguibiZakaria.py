#inputExample, please Changeit
startTime = [1,2,3,3]
endTime =  [3,4,5,6]
profit =  [50,10,40,70]

class BinaryTreeNode:
  def __init__(self, data):
      #data = [start,end, index,profit]
    self.data = data
    self.bestChild = -1
    self.Aggregatedcost = -1
    self.children = []


def FindBestJob(startTime,endTime,profit):
    myTreeHead = BinaryTreeNode([0,1,-2,0])
    def addNodeToTree(myTreeHead,Node):
        #if endTimeLess ThanStartime
        if(myTreeHead.data[1]<=Node.data[0]):
            myTreeHead.children.append(Node)
        if myTreeHead.children:
            for elm in myTreeHead.children:
                addNodeToTree(elm,Node)

    def nonMutuallyExclusive(startJob,endJob):
        for i in range(0,len(startTime)):
            data = BinaryTreeNode([startTime[i],endTime[i], i,profit[i]])
            addNodeToTree(myTreeHead,data)


    def maxCost(myTreeHead):
        if myTreeHead.children:
            for elm in myTreeHead.children:
                cost,indexOfBestChild= maxCost(elm)
                if myTreeHead.bestChild==-1 or myTreeHead.Aggregatedcost < cost:
                    myTreeHead.bestChild = indexOfBestChild 
                    myTreeHead.Aggregatedcost= cost             
            return myTreeHead.Aggregatedcost + myTreeHead.data[3],myTreeHead.data[2]
        else :
            return myTreeHead.data[3],myTreeHead.data[2]
    def FormatOutput(myTreeHead):
        bestChild = -2
        profit=0
        while(bestChild!=-1):
            profit += myTreeHead.data[3]
            indexOfbestchild = myTreeHead.bestChild
            if not myTreeHead.children:
                break
            else:
                for elm in myTreeHead.children:
                    if elm.data[2]==indexOfbestchild:
                        myTreeHead = elm
        print(profit)
    nonMutuallyExclusive(startTime, endTime)
    maxCost(myTreeHead)
    FormatOutput(myTreeHead)
        
FindBestJob(startTime,endTime,profit)
