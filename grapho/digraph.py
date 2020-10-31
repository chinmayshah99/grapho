import copy

from .graph import Graph


class DirectedGraph(Graph):
    '''
        Directed graph
        Usage:\n
        g = DirectedGraph()\n
        or another instance of directed graph can be passed as an argument\n
        g1 = DirectedGraph(g)
        Note: It creates a copy of the item and does not maintain the reference
    '''

    def __init__(self, graph=None):
        """[summary]

        Raises:
            ValueError: If the paramter graph is not of type Graph and is non-empty 
        """        
        if graph is None:
            super().__init__()
        elif isinstance(graph, DirectedGraph):
            # create a copy
            # not shallow copy
            self._graph = {key: value[:] for key, value in graph.graph.items()} 
            # need to deepcopy this because don't know what user stores inside
            self._node_data = copy.deepcopy(graph._node_data) 
            self._edge_data = copy.deepcopy(graph._edge_data)  
            self._node_count = graph.node_count
            self._edge_count = graph.edge_count
        else:
            raise ValueError("Either empty ")

    def in_degree(self, node):
        '''
            Returns in degree of a node
            # TODO
        '''
        pass

    def out_degree(self, node):
        '''
            Returns out degree of a node
            # TODO
        '''
        pass
