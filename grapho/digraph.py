from .graph import Graph


class DirectedGraph(object, Graph):
    '''
        Directed graph
        {
            node = [[nodeA, weigh1], [nodeB, weigh2]],
            nodeA = [[nodeC, weigh3]]
        }
    '''

    def __init__(self, graph={}):
        '''
            sdfs
        '''
        super().__init__(graph)
