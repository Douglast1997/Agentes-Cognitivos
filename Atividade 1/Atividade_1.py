import pandas as pd
import numpy as np
from collections import deque

from sympy import HeuristicGCDFailed


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]

 
    # This is heuristic function which is having equal values for all nodes
    def h(self, start,end):
       DirectDistances = np.array([[0, 10, 18, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8], 
       [-1, 0, 8.5, 14.8, 26.2, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],
       [-1, -1, 0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
       [-1, -1, -1, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
       [-1, -1, -1, -1, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
       [-1, -1, -1, -1, -1, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
       [-1, -1, -1, -1, -1,-1, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],
       [-1, -1, -1, -1, -1,-1, -1, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
       [-1, -1, -1, -1, -1,-1, -1, -1, 0, 13.5, 11.2, 10.9, 21.2, 26.6],
       [-1, -1, -1, -1, -1,-1, -1, -1, -1, 0, 17.6, 24.2, 18.7, 21.2],
       [-1, -1, -1, -1, -1,-1, -1, -1, -1, -1, 0, 14.2, 31.5, 35.5],
       [-1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, 0, 28.8, 33.6],
       [-1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, 0, 5.1],
       [-1, -1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, 0]])

       panda_df = pd.DataFrame(data = DirectDistances[0:, 0:],
       index = ['E' + str(i + 1) 
       for i in range(DirectDistances.shape[0])],
       columns = ['E' + str(i + 1) 
       for i in range(DirectDistances.shape[1])])
       #print("Começo: {}".format(start))
       #print("Final: {}".format(end))
    
       if panda_df[end][start] == -1:
           HeuristicGain = panda_df[start][end]
       else:
           HeuristicGain = panda_df[end][start]

       #print(HeuristicGain)
       return HeuristicGain
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        IsFirstTime = True
        open_lst = set([start])
        print("Fronteira: {}".format(open_lst))

        closed_lst = set([])
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        

        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v,stop) < poo[n] + self.h(n,stop):
                    n = v;


            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Caminho: {}'.format(reconst_path))
                print("Custo Final: {:0.2f}".format(poo[stop]))
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                    #print(poo[m])
                    
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
                        
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
                            
            
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
            
            if(IsFirstTime):
                print("Ponto: {}, Custo: {:0.2f} ".format(start, poo[start] + self.h(start,stop)))
                print("_____________________________________________________________________")
                IsFirstTime = False

            print("Fronteira: {}".format(open_lst))
            openToList = list(open_lst)
            for i in range(len(openToList)):
                print("Ponto: {}, Custo: {:0.2f} ".format(openToList[i], poo[openToList[i]] + self.h(openToList[i],stop)))

            print("_____________________________________________________________________")


 
        print('Path does not exist!')
        return None

adjac_lis = {
    'E1': [('E2', 10)],
    'E2': [('E1', 10), ('E3',8.5), ('E9',10), ('E10',3.5)],
    'E3': [('E2', 8.5), ('E4',6.3), ('E9',9.4), ('E13',18.7)],
    'E4': [('E3', 6.3), ('E5',13), ('E8',15.3), ('E13',12.8)],
    'E5': [('E4', 13), ('E6',3), ('E7',2.4), ('E8',30)],
    'E6': [('E5', 3)],
    'E7': [('E5', 2.4)],
    'E8': [('E4', 15.3), ('E5',30), ('E9',9.6), ('E12',6.4)],
    'E9': [('E2', 10), ('E3',9.4), ('E8',9.6), ('E11',12.2)],
    'E10': [('E2', 3.5)],
    'E11': [('E9', 12.2)],
    'E12': [('E8', 6.4)],
    'E13': [('E3', 18.7), ('E4',12.8), ('E14',5.1)],
    'E14': [('E13', 5.1)],
  

}
graph1 = Graph(adjac_lis)

startStation = input("Digite o ponto de inicío: ")
endStation = input("Digite o ponto de fim: ")

station = ["E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14"]
IsStationListed = (startStation.upper() in station) and (endStation.upper() in station)
print("_____________________________________________________________________")
if IsStationListed:
    graph1.a_star_algorithm(startStation.upper(), endStation.upper())
else:
    print("Uma das linhas selecionadas não existe")
