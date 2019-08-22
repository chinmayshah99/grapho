#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from grapho.graph import Graph

class TestGraph(unittest.TestCase):
    """Tests for `greedybfs` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.grabh = Graph()

    def tearDown(self):
        """Tear down test fixtures, if any."""
        # print(self.grabh.nodes)
        self.grabh = None

    # add data to node in a list
    def test_add_node_data(self):
        self.grabh.add_node("t_a_n_d_1")

        data = [132,"sdfsdf", (34,454), {1:'hi', 2: "no_hi"}]
        self.grabh.add_node_data("t_a_n_d_1", data)
        assert(data == self.grabh.get_node_data("t_a_n_d_1"))

    def test_add_node_data_1(self):
        self.grabh.add_node("t_a_n_d_1_1")
        data = "some info"
        self.grabh.add_node_data("t_a_n_d_1_1", data)
        assert([data] == self.grabh.get_node_data("t_a_n_d_1_1"))
    
    def test_set_node_data(self):
        self.grabh.add_node("t_s_n_d_1")
        data = [1,2,3]
        self.grabh.add_node_data("t_s_n_d_1", data)
        assert(data == self.grabh.get_node_data("t_s_n_d_1"))
        new_data = [4,5,6]
        self.grabh.set_node_data("t_s_n_d_1", new_data)
        assert(new_data == self.grabh.get_node_data("t_s_n_d_1"))  

    def test_append_node_data(self):
        self.grabh.add_node("t_ap_n_d_1")
        data = "some info"
        self.grabh.add_node_data("t_ap_n_d_1", data)
        assert([data] == self.grabh.get_node_data("t_ap_n_d_1"))
        some_more_data = "hello, world"
        self.grabh.append_node_data("t_ap_n_d_1", some_more_data)
        
        data =[data]
        data.append(some_more_data)
        new_data = self.grabh.get_node_data("t_ap_n_d_1")

        assert(data == new_data)

    def test_delete_node_data(self):
        node_name = "t_d_n_d_1"
        self.grabh.add_node(node_name)
        data = [1,2,3]
        self.grabh.add_node_data(node_name, data)

        self.grabh.delete_node_data(node_name)
        self.assertRaises(AttributeError, self.grabh.get_node_data, node_name)

    # add data to node in a list
    def test_add_edge_data(self):
        self.grabh.add_node("t_a_e_d_1")
        self.grabh.add_node("t_a_e_d_2")
        
        self.grabh.add_edge("t_a_e_d_1", "t_a_e_d_2")
        data = [132,"sdfsdf", (34,454), {1:'hi', 2: "no_hi"}]
        self.grabh.add_edge_data("t_a_e_d_1", "t_a_e_d_2", data)
        
        list_from_graph = self.grabh.get_edge_data("t_a_e_d_1", "t_a_e_d_2")
        assert(data == list_from_graph)

    def test_add_edge_data_1(self):
        self.grabh.add_node("t_a_e_d__1_1")
        self.grabh.add_node("t_a_e_d_1_2")
        self.grabh.add_edge("t_a_e_d__1_1", "t_a_e_d_1_2")
        
        data = "some info"
        self.grabh.add_edge_data("t_a_e_d__1_1", "t_a_e_d_1_2", data)
        
        assert([data] == self.grabh.get_edge_data("t_a_e_d__1_1", "t_a_e_d_1_2"))
    
    # checks for error if edge does not exist
    def test_add_edge_data_2(self):
        self.assertRaises(AttributeError, self.grabh.get_edge_data, "t_a_e_d_1_2", 't_a_e_d__1_1')

    # checks for error if node does not exist
    def test_add_edge_data_3(self):
        self.assertRaises(AttributeError, self.grabh.get_edge_data, "some random", 't_a_e_d__1_1')

    def test_set_edge_data(self):
        self.grabh.add_node("t_s_e_d__1")
        self.grabh.add_node("t_s_e_d__2")
        self.grabh.add_edge("t_s_e_d__1", "t_s_e_d__2")
        
        data = [1,2,3]
        self.grabh.add_edge_data("t_s_e_d__1", "t_s_e_d__2", data)
        
        assert(data == self.grabh.get_edge_data("t_s_e_d__1", "t_s_e_d__2"))
        
        new_data = [4,5,6]
        self.grabh.set_edge_data("t_s_e_d__1", "t_s_e_d__2", new_data)
        data_set = self.grabh.get_edge_data("t_s_e_d__1", "t_s_e_d__2")
        assert(new_data == data_set)
    
    
    def test_append_edge_data(self):
        self.grabh.add_node("t_ap_e_d__1")
        self.grabh.add_node("t_ap_e_d__2")
        self.grabh.add_edge("t_ap_e_d__1", "t_ap_e_d__2")

        data = "some info"
        self.grabh.add_edge_data("t_ap_e_d__1", "t_ap_e_d__2", data)
        graph_data = self.grabh.get_edge_data("t_ap_e_d__1", "t_ap_e_d__2")
        assert([data] == graph_data)
        
        some_more_data = "hello, world"
        self.grabh.append_edge_data("t_ap_e_d__1", "t_ap_e_d__2", some_more_data)
        
        data =[data]
        data.append(some_more_data)
        graph_data = (self.grabh.get_edge_data("t_ap_e_d__1", "t_ap_e_d__2"))

        assert(data == graph_data)
    
    def test_delete_edge_data(self):
        self.grabh.add_node("t_d_e_d__1")
        self.grabh.add_node("t_d_e_d__2")
        self.grabh.add_edge("t_d_e_d__1", "t_d_e_d__2")

        data = [1,2,3]
        self.grabh.add_edge_data("t_d_e_d__1", "t_d_e_d__2", data)

        self.grabh.delete_edge_data("t_d_e_d__1", "t_d_e_d__2")
        self.assertRaises(AttributeError, self.grabh.get_edge_data, "t_d_e_d__1", "t_d_e_d__2")
