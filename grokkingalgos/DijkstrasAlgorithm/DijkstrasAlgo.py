#!/usr/bin/python3.11
"""
    @name DijkstrasAlgo.py
    @datelastmodified 2023 03 21
    @purpose Implement Dijkstra's Algorithm for finding cheapest path to a destination.
"""
class DijkstrasAlgo:
    #.......................................... Constructor
    def __init__(self):
        self.processed_nodes = list()
        self.graph = dict()
        self.costs = dict()
        self.parents = dict()
    #.......................................... Getters
    def get_costs(self):
        return self.costs
    def get_graph(self):
        return self.graph
    def get_parents(self):
        return self.parents
    def get_processed_nodes(self):
        return self.processed_nodes
    #.......................................... Setters
    def set_costs(self, new_costs:dict):
        self.costs = new_costs
    def set_graph(self, new_graph:dict):
        self.graph = new_graph
    def set_parents(self, new_parents:dict):
        self.parents = new_parents
    #.......................................... Data / Graph Defaults
    def default_costs(self):
        print( "Establishing default costs." )
        infinity = float( "inf" )
        self.costs[ "node_a" ] = 6
        self.costs[ "node_b" ] = 2
        self.costs[ "finish_node" ] = infinity  
    def default_graph(self):
        print( "Establishing default graph." )
        self.graph[ "start_node" ] = dict()
        self.graph[ "start_node" ][ "node_a" ] = 6
        self.graph[ "start_node" ][ "node_b" ] = 2
        self.graph[ "node_a" ] = dict()
        self.graph[ "node_a" ][ "finish_node" ] = 1
        self.graph[ "node_b" ] = dict()
        self.graph[ "node_b" ][ "node_a" ] = 3
        self.graph[ "node_b" ][ "finish_node" ] = 5
        self.graph[ "finish_node" ] = dict()
    def default_parents(self):
        print( "Establishing default parent nodes." )
        self.parents[ "node_a" ] = "start_node"
        self.parents[ "node_b" ] = "start_node"
        self.parents[ "finish_node" ] = None 
    def defaults(self):
        self.default_graph()
        self.default_costs()
        self.default_parents()
    #.......................................... Data / Graph Methods
    def find_cheapest_node(self):
        print( "Finding the cheapest node." )
        """
            @method     find_cheapest_node
            @return     lowest_cost_node
            @purpose    Go through each node. If node is lowest cost\
                        and has not been processed, set it as new\
                        lowest node. Return lowest_cost_node.        
        """
        lowest_cost = float( "inf" )    # Value starts @ Infinity
        lowest_cost_node = None         # There is no lowest cost node yet. 
        for node in self.costs:
            cost = self.costs[ node ]
            lowest_cost_so_far = ( cost < lowest_cost )
            not_yet_processed = ( node not in self.processed_nodes )
            if lowest_cost_so_far and not_yet_processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    def implement(self):
        print( "Implementing Dijkstra's Algorithm." )
        """
            @method     implement
            @purpose    Find lowest-cost node not yet processed.\
                        If all nodes have been processed, exit loop.\
                        Otherwise: Traverse all neighbors of the node.\
                        Then, if it is cheaper to get to this node,\
                        update the cost for the node.\
                        Next, the node becomes the new parent for its neighbor.\
                        Finally, mark the node as processed. Find next node to process.
        """
        node = self.find_cheapest_node()
        print( "Checking if there are nodes to process." )
        while node is not None:
            print( f"---- { node }----" )
            cost = self.costs[ node ]
            neighbors = self.graph[ node ]
            for key in neighbors.keys():
                new_cost = cost + neighbors[ key ];
                if self.costs[ key ] > new_cost:
                    self.costs[ key ] = new_cost;
                    self.parents[ key ] = node; 
            self.processed_nodes.append( node )
            node = self.find_cheapest_node()
            def debug():
                """ 
                    @method     debug
                    @purpose    Use if you get lost or need clarity\
                                about what this method is doing under the hood.
                """
                print( "Node's cost:", cost )
                print( "Node's Neighbors:", neighbors )
                print( f"Node's Cost ({ cost }) + Neighbor's Cost({ neighbors[ key ] }) = { new_cost }" )
                print( f"{ self.costs[ key ] } is greater than { new_cost }" )
                print( "appending this node:", node )
        print("There are no more nodes to process.")
        self.view_cheapest_path()
    def view_cheapest_path(self):
        print( "Cheapest route:", "Start -->"," --> ".join( self.processed_nodes ) )
if __name__ == "__main__":
    di_algo = DijkstrasAlgo()
    di_algo.defaults()
    di_algo.implement()