from .graph import Graph


class DirectedGraph(Graph):
    '''
        Directed graph
        {
            node: [[nodeA, weigh1], [nodeB, weigh2]],
            nodeA: [[nodeC, weigh3]]
        }
    '''

    def __init__(self, graph=None):
        '''

        '''
        super().__init__(graph)

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
