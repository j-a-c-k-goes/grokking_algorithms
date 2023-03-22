`The shortest distance is variable, contextual.`
`Most interesting distance???`
`The shortest path is not guaranteed to be the fastest path.`
# Breadth First Search

## Introduction to Graphs
The breadth-first search is a graph algorithm. It does not deal with the X and Y axis. But it does enable finding the shortest distance between two things; Model the problem as a graph. Solve using breadth-first search. _Note: Shortest and Fastest are not interchangeable. Shortest path means least amount of segments._

## What is a graph?
A graph models a set of connections. And each graph is made up of _nodes_ and _edges_.

A node can be directly connected to other nodes, which are called __neighbors__. And graphs are a way to model how and where things are connected to one another. 

## Breadth-first search
Breadth-first search is a graph-based algorithm. It answers:
1. Is there a path from node A to node B?
2. What is the shortest path from node A to node B?

With a breadth-first algorithm, the entirety of the network is searched by order of connections ( first degree, second degree, and so on...). And each time you search for someone, you will add all of their connections to the search. Searching people in the order in which they are added requires using the __queue__ data structure. 

## Queues
Queues are similar to stacks. Random elements cannot be accessed. And the only two operations are _enqueue_ and _dequeue_. ALso, the queue is a _First In, First Out_ data structure; stacks are _Last In, First Out_.

## Implementing the Graph
Expressing the node connections in a graph can be done through a hash table. 

## Running Time
BreadthFirst Search requires at least an `O(number of edges)` runtime. And adding one person to the queue takes constant time `O(1)`. All in all, BreadthFirst Search takes `O(number of people/vertices + number of edges)` or `O(V+E)`. 
