import warnings
from abc import abstractmethod, ABCMeta


class Graph(object, metaclass=ABCMeta):
    '''
        graph in the form
        {
            node = [[nodeA, weigh1], [nodeB, weigh2]],
            nodeA = [[nodeC, weigh3]]
        }
    '''

    def __init__(self, graph={}):
        '''
            sdfs
        '''
        self._graph = graph
        self._node_data = {}
        self._edge_data = {}
        self._node_count = 0
        self._edge_count = 0

    @property
    def node_count(self):
        return self._node_count

    @property
    def edge_count(self):
        return self._edge_count

    def add_node(self, node):
        '''
            Adds node to the graph.
            If it already exists, raise an Error
        '''
        if node not in self._graph:
            self._graph[node] = []
            self._node_count += 1
        else:
            raise ValueError("Node " + str(node) + " already exists in graph")

    def add_node_from(self, nodes):
        '''
            add nodes from list of nodes
            #TODO
        '''
        pass

    def add_edge(self, start_node, end_node, weight=1):
        '''
            Adds edge from start_node to end_node
            If weight is not specified, defaults to 1
            If the edge already exists, updates the weight to given in argument
        '''

        if not self._is_number(weight):
            raise ValueError("{} is not a valid Number".format(weight))

        # check if start node already exists
        if start_node not in self._graph:
            warnings.warn("Node {} does not exist, adding it to graph".
                          format(str(start_node)), Warning)
            self.add_node(start_node)
        edges = self._graph[start_node]

        # check if end node already exists
        if end_node not in self._graph:
            warnings.warn("Node {} does not exist, adding it to graph".
                          format(str(end_node)), Warning)
            self.add_node(end_node)

        # check if edge already exists

        for edge in edges:
            if edge[0] == end_node:
                warnings.warn("Edge already exists with weight {}, \
                               updating it to {}".
                              format(str(edge[1]), str(weight)), Warning)
                edge[1] = weight
                return

        self._graph[start_node].append([end_node, weight])
        self._edge_count += 1

    def delete_node(self, node):
        '''
            Removoes all node dependecnies and then removes node
        '''
        self._node_exists(node)

        for key, values in self._graph.items():
            if key == node:
                # if edge exists from node,
                # just reduce the edge count as we'll be removing node later
                for edge in values:
                    self._edge_count -= 1
                continue
            else:
                for edge in values:
                    # if edge exists to node remove it
                    if edge[0] == node:
                        self.delete_edge(key, node)

        self._graph.pop(node, None)
        self._node_count -= 1

    def delete_edge(self, start_node, end_node):

        self._node_exists(start_node)
        self._node_exists(end_node)

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                self._graph[start_node].remove(edge)

        self._edge_count -= 1

    def delete_edge_from(self, edge_list):
        # deletes edge from the list of edges to be deleted
        # TODO
        pass

    def get_node_details(self, node):
        '''
            Returns all nodes connected to it in a dictionary
            dict = {
                node1: weigh1,
                node2: weigh2
            }
        '''
        if node in self._graph:
            temp_dict = {}
            edges = self._graph[node]

            for edge in edges:
                temp_dict[edge[0]] = edge[1]

            return temp_dict

        else:
            raise AttributeError("Node " + str(node) + " does not exist")

    def update_edge(self, start_node, end_node, weight=None):
        '''
            Updates the weight of the edge
            if the new weight is not specified, it deletes that edge
            if the edge is not found, it raise an error
        '''

        # check if nodes already exists
        self._node_exists(start_node)
        self._node_exists(end_node)

        if weight is None:
            self.delete_edge(start_node, end_node)

        if not self._is_number(weight):
            raise ValueError("{} is not a valid Number".format(weight))

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                edge[1] = weight
                return

        raise AttributeError("Edge from {} to {} does not exist".
                             format(start_node, end_node))

    @property
    def nodes(self):
        '''
            returns a list of all nodes
        '''
        return [*self._graph]

    @property
    def graph(self):
        '''
            returns the graph
        '''
        return self._graph

    def return_edges(self, node):
        if self._node_exists(node):
            return self._graph[node]

    def get_edge(self, start_node, end_node):
        '''
            Returns the edge weight,
            raise AttributeError incase edge does not exist
        '''

        self._node_exists(start_node)
        self._node_exists(end_node)

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                return edge[1]

        raise AttributeError("Edge does not exist")

    def _is_number(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False

    def _node_exists(self, node):
        '''
            check if node exists,
            returns True if does,
            Raises error in case not in node
        '''
        if node in self._graph:
            return True
        else:
            raise AttributeError("Node " + str(node) + " does not exist")

    def add_node_data(self, node, data):
        if self._node_exists(node):
            if isinstance(data, list):
                self._node_data[node] = data
            else:
                self._node_data[node] = [data]

    def get_node_data(self, node):
        if self._node_exists(node):
            if node in self._node_data:
                return self._node_data[node]
            else:
                AttributeError("Data does not exist")

    def set_node_data(self, node, data):
        '''
            Overwrites existing data in Node
        '''
        self.add_node_data(node, data)

    def append_node_data(self, node, data):
        '''
            Appends to existing data in node
        '''
        if self._node_exists(node):
            if node in self._node_data:
                existing_data = self._node_data[node]
                new_data = existing_data.append(data)
                self._node_data[node] = new_data
            else:
                warnings.warn("Node data for {} does not exist, \
                                creating an entry".format(str(node)), Warning)
                self.add_node_data(node, data)

    def _delete_node_data(self, node):
        if self._node_exists(node):
            if node in self._node_data:
                self._node_data.pop(node, None)
            else:
                ValueError("No data existsfor node {}".format(str(node)))

    def add_edge_data(self, start_node, end_node, data):
        if \
            self._node_exists(start_node) and \
            self._node_exists(end_node) and \
                self._edge_exists(start_node, end_node):

            if isinstance(data, list):
                edge_name = (start_node, end_node)
                self._node_data[edge_name] = data
            else:
                self._node_data[edge_name] = [data]

    def get_edge_data(self, start_node, end_node):
        if \
            self._node_exists(start_node) and \
            self._node_exists(end_node) and \
                self._edge_exists(start_node, end_node):

            edge_name = (start_node, end_node)
            if edge_name in self._edge_data:
                return self._node_data[edge_name]
            else:
                AttributeError("Data does not exist")

    def set_edge_data(self, start_node, end_node, data):
        '''
            Overwrites existing data in Node
        '''
        self.add_edge_data(start_node, end_node, data)

    def append_edge_data(self, start_node, end_node, data):
        '''
            Appends to existing Edge in node
        '''

        if \
            self._node_exists(start_node) and \
            self._node_exists(end_node) and \
                self._edge_exists(start_node, end_node):

            edge_name = (start_node, end_node)
            if edge_name in self._edge_data:
                existing_data = self._node_data[edge_name]
                new_data = existing_data.append(data)
                self._node_data[edge_name] = new_data
            else:
                warnings.warn("Edge data for {} and {} does not exist, \
                              creating an entry".
                              format(str(start_node), str(end_node)), Warning)

                self.add_edge_data(start_node, end_node, data)

    def _delete_edge_data(self, start_node, end_node):
        if \
            self._node_exists(start_node) and \
            self._node_exists(end_node) and \
                self._edge_exists(start_node, end_node):

            edge_name = (start_node, end_node)
            if edge_name in self._edge_data:
                self._node_data.pop(edge_name, None)
            else:
                ValueError("No data exists")

    def _edge_exists(self, start_node, end_node):
        '''
            Returns True is edge exists,
            Returns False otherwise
        '''

        edges = self._graph[start_node]
        for edge in edges:
            if edge[0] == end_node:
                return True

        return False
