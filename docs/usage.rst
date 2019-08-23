=====
Usage
=====

To use grapho in a project::

    import grapho


To create a Directed Graph: 
.. code-block:: python

    from grapho.digraph import DirectedGraph

    g = DirectedGraph()

---------
Functions
---------
To add a node
    
    g.add_node('a')

To add an edge
.. code-block:: python
    g.add_edge('node_1', 'node_2') # default weight
    g.add_edge('node_1', 'node_2', 4.0) # provide weight as argument

To delete a node
.. code-block:: python

    g.delete_node('a')

To delete an edge
.. code-block:: python

    g.delete_edge('node_1', 'node_2')


----------
Properties
----------

Count of number of nodes
.. code-block:: python

    g.node_count

Count of number of edges
.. code-block:: python

    g.edge_count

List of nodes
.. code-block:: python

    g.nodes

Return Graph in dictionary form
.. code-block:: python

    g.graph
