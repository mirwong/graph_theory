

class Node(object):
    '''A graph theory node'''

    def __init__(self, graph, connectedNodes=[], startState=False):
        self.graph = graph
        self.neighbors = connectedNodes
        self.state = startState
        self.type = "undirected" # to allow to extend to directed graphs

    def __str__(self):
        pass

    def __eq__(self, other):
        return (self.state == other.get_state())

    def get_graph(self):
        return self.graph

    def get_neighbors(self):
        return self.neighbors

    def get_state(self):
        return self.state

    def num_edges(self):
        return len(self.neighbors)

    def has_edge(self, other):
        if self.type == "not directed":
            if other in self.neighbors:
                return True
            else:
                return False

    def is_connected(self):
        if len(self.neighbors) == (self.graph.get_size()-1):
            return True
        else:
            return False

    def create_edge(self, other):
        if other not in self.neighbors:
            self.neighbors.append(other)
            other.neighbors.append(self)
            return True
        else:
            return False


class Graph(object):
    '''A graph theory graph'''

    def __init__(self, num_nodes):
        self.size = num_nodes
        self.nodes
        for n in range(self.size):
            self.nodes.append(Node(self))

    def __str__(self):
        pass

    def get_size(self):
        return self.size

    def get_nodes(self):
        return self.nodes

    def is_connected(self):
        if all([node.is_connected() for node in self.nodes]):
            return True
        else:
            return False
