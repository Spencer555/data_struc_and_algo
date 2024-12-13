'''
a graph is a set of values related in a pair wide fashion
each item is called a node or a vertex
nodes are connected with edges 
they are great data struc to modify real world relationship reping links 
can represent friendship, networks, www, roads one city to another , etc

linked lists are a type of tree, trees are a type of graph

types of graph 
directed and undirected
directed
flows one way 
e.g twitter profile

undirected
flows both ways
e.g facebook friendship


and weighted and unweighted 

unweighted graph 
there is no info in the edges or links


weighted graph 
there is info in the edges

google maps use it to calculate the shortes path to get to a place 



cyclic and acyclic

cyclic 
vertices connected in a circualr fashion can move in a circular fashion
e.g google maps

acyclic
u cant go in a circular fashion
'''


# ways to represent graph
# edge list 
# a connection for items that itself are arrays
graph = [[0,2], [2,3], [2,1], [1,3]]


# adjacent list 
# where the index is the node and the value is the nodes neighbours 
# 0 is connected to two
# 1 is connected to 2,3
# 2 is connected to 0,1,3
graph1 = [[2], [2,3], [0,1,3], [1,2]]


# adjacent matrix 
# it has 0 and ones indicating if the node x has a connection to y 0 means no and one means yes
graph2 = {
    0: [0 ,0,1,0],
    1: [0 ,0,1,1],
    2: [1 ,1,0,1],
    3: [0 ,1,1,0],
}




# graph implementation undirected
class Graph:
    
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
        
        
    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes +=1
    
    def addEdge(self, node1, node2):
        # undirected so it goes both ways 
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        
    
    

    def showConnection(self):
        for vertex, neighbors in self.adjacentList.items():
            print(vertex, end = '-->')
            print(' '.join(neighbors))

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
print(myGraph)
myGraph.showConnection()


'''
graphs 

pro 
usefull when it comes to relationtionship 
u usually would never have to implement ur own graph in production

cons 
scaling is hard - because it can get complicated



'''