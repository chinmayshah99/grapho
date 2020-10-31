from .graph import Graph


class UnDirectedGraph(object, Graph):
    '''
        UnDirected graph
        {
            node: [[nodeA, weigh1], [nodeB, weigh2]],
            nodeA: [[nodeC, weigh3]]
        }
    '''

    def __init__(self, graph=None):
        '''
            
        '''

        super().__init__(graph)
