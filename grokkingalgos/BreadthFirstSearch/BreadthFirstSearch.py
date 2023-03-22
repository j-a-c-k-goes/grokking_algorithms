#!/usr/bin/python3.11
"""
    @name graph.py
    @datelastmodified 2023 03 21
    @purpose Implement a graph-based Breadth-first search.
"""
from collections import deque
class BreadthFirstSearch:
    def __init__(self):
        self.graph = dict()
        self.search_queue = deque()
    def get_graph(self):
        return self.graph
    def set_graph( self, new_graph: dict ):
        self.graph = new_graph
    def get_search_queue(self):
        return self.search_queue
    def default_connections(self) -> dict:
        self.graph[ "you" ] = [ "alice", "buddy", "claire" ]
        # First Degree Connections       
        self.graph[ "alice" ] = [ "peggy" ]
        self.graph[ "buddy" ] = [ "martin", "peggy"]
        self.graph[ "claire" ] = [ "dacoldest", "erin"]
        # Second degree connections
        self.graph[ "peggy" ] = list()
        self.graph[ "martin" ] = list()
        self.graph[ "dacoldest" ] = list()
        self.graph[ "erin" ] = list()
        return self.graph
    def person_is( self, current_connection:str, connection_looking_for:str ) -> bool:
        return current_connection.lower() == connection_looking_for.lower()
    def query( self, name:str ):
        connections = 0
        self.search_queue += self.graph[ "you" ] 
        searched = list()                        
        while self.search_queue:
            current_connection = self.search_queue.popleft()
            # Search person if not already searched. 
            if not current_connection in searched:
                if self.person_is( current_connection, name ):
                    print( f"Located { current_connection }! Person was { connections } connections away." )
                    break
                else:
                    self.search_queue += self.graph[ current_connection ] 
                    searched.append( current_connection )
                    print("Persons already searched:", searched )
                connections += 1
        return "Done"