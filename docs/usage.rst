=====
Usage
=====

To use grapho in a project::

    import grapho


To create a Directed Graph: 

    from grapho.digraph import DirectedGraph

    g = DirectedGraph()

---------
Functions
---------
To add a node
    
    g.add_node('a')

To add an edge

    g.add_edge('node_1', 'node_2') # default weight
    g.add_edge('node_1', 'node_2', 4.0) # provide weight as argument

To delete a node

    g.delete_node('a')

To delete an edge

    g.delete_edge('node_1', 'node_2')


----------
Properties
----------

Count of number of nodes

    g.node_count

Count of number of edges

    g.edge_count

List of nodes

    g.nodes

Return Graph in dictionary form

    g.graph
