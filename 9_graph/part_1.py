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
graph2 = [
    [0 ,0,1,0],
    [0 ,0,1,1],
    [1 ,1,0,1],
    [0 ,1,1,0],
]