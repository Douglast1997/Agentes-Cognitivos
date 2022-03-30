from pickle import TRUE

from sympy import true
import graphadjacencylist


def main():

    g = create_graph()
    print(g)

   


def create_graph():

    g = graphadjacencylist.GraphAdjacencyList()

    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_vertex("G")

    g.add_edge("A", "B", directed=True, weight=12)
    g.add_edge("A", "C", directed=True, weight=14)
    

    g.add_edge("B", "C", directed=True, weight=9)
    g.add_edge("B", "D", directed=True, weight=38)

    g.add_edge("C", "D", directed=True, weight=24)
    g.add_edge("C", "E", directed=True, weight=7)

    g.add_edge("D", "G", directed=True, weight=9)
    
    g.add_edge("E", "D", directed=True, weight=13)
    g.add_edge("E", "G", directed=True, weight=29)
    g.add_edge("E", "F", directed=True, weight=9)


    return g

def heuristic_function(start,end):
    return 1

def initialise(start_node,end_node):
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        


    




main()