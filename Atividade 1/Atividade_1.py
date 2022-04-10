import pandas as pd
import numpy as np
from collections import deque
import math
from sympy import HeuristicGCDFailed


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis #Inicializa a lista de adjacências
 
    def get_neighbors(self, v):
        return self.adjac_lis[v] #Retorna a lista de vizinhos

 
    # Essa é a função de Heuristica que foi definida como a distância direta entre duas linhas de trêm.
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
       index = ['E' + str(i + 1)  #Labels E1 até E14 do dataframe
       for i in range(DirectDistances.shape[0])],
       columns = ['E' + str(i + 1) #Labels E1 até E14 do dataframe
       for i in range(DirectDistances.shape[1])])
       
    
       if panda_df[end][start] == -1: #Pega o inverso que é a mesma distância
           HeuristicGain = panda_df[start][end]
       else:
           HeuristicGain = panda_df[end][start]

       HeuristicGain = HeuristicGain/25 #Precisa dividir os Kms por 25km/h para obter o tempo gasto
      
       return HeuristicGain #Retorna o custo da função Heuristica que é Tempo gasto
 
    def a_star_algorithm(self, start, stop):
        """Neste open_lst está uma lista de nós que foram visitados, que é a fronteira,
        mas cujos vizinhos nem sempre foram inspecionados, começam com
        o nó inicial.
        
        Closed_lst é uma lista de nós que foram visitados
        e cujos vizinhos sempre foram inspecionados.
        O Closed_lst é necessário para que os filhos não retorne para o pai."""
        
        IsFirstTime = True
        open_lst = set([start]) #Coloca o Nó incial na fronteira
        print("Fronteira: {}".format(open_lst))

        closed_lst = set([])
 
        # A variável poo tem distâncias/tempo de trajeto presentes desde o início até todos os outros nós
        # O valor default é +infinito
        poo = {}
        poo[start] = 0 #Definido g(n)
 
        # A variável par contém um mapeamento adjacente de todos os nós
        par = {}
        par[start] = start #Será utilizada como a condição de parada para reconstruir a lista
 
        
        while len(open_lst) > 0:
            n = None
 
            #Buscando um nó com o menor valor de custo;
            for v in open_lst:
                #Verificando se g(v) + h(v) < g(n) + h(n)
                if n == None or poo[v] + self.h(v,stop) < poo[n] + self.h(n,stop):
                    n = v;


            if n == None:
                print('O caminho não existe!')
                return None
 
            # Se o nó atual é a nó final
            # então começamos a Reconstruir o caminho de novo do início
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    #Busca quem é o pai do nó analisado e só termina o loop quando par[start] = start

                    #print("n: {}".format(n))
                    #print("par[{}]: {}".format(n,par[n]))
                    

                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
                
                print('Caminho: {}'.format(reconst_path))
                #print('Custo Final: {}'.format(poo[stop]))
                
                CustoFinalHoras = math.floor(poo[stop])
                CustoFinalMinutos = math.floor((poo[stop] - CustoFinalHoras)*60)
                CustoFinalSegundos = (((poo[stop] - CustoFinalHoras)*60) - CustoFinalMinutos)*60
                
                if CustoFinalHoras == 0:
                    print("Custo Final - Tempo do trájeto mais rápido é de: {:0.2f} Minuto(s) e {:0.2f} Segundo(s)".format(CustoFinalMinutos,CustoFinalSegundos))
                else:
                    print("Custo Final - Tempo do trájeto mais rápido é de: {:0.2f} Hora(s) e {:0.2f} Minuto(s) e {:0.2f} Segundo(s)".format(CustoFinalHoras,CustoFinalMinutos,CustoFinalSegundos))

                return reconst_path
 
            # para todos os vizinhos do nó atual faça
            for (m, weight) in self.get_neighbors(n): #Obtem todos os vizinhos de n e seu respectivo peso.
                
                weight = weight/25 #Necessário dividir o peso em Km pela velocidade km/h para obter o custo em Horas.
                
                # se o nó atual não estiver presente nem em Open_lst e closed_lst
                # adicione-o em open_lst, na fronteira, e definimos n como seu par[m]
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m) # Adicionamos na fronteira
                    par[m] = n   #Define que o pai de m é n.
                    poo[m] = poo[n] + weight #f(m) é o custo até n mais o peso de m. 
                    
                    
                # caso contrário, verifique se é mais rápido visitar primeiro n, depois m
                # e se for, atualize os dados par e os dados poo
                # e se o nó estava no closed_lst, mova-o para open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        print("Poo[{}]: {}".format(m,poo[m]))
                        print("Poo[{}] + {}".format(poo[n],weight))
                        poo[m] = poo[n] + weight
                        par[m] = n
                        print("Par[{}]: {}".format(m,n))
                        
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
                            
            
 
            # remova n do open_lst e adicione-o ao closed_lst
            # porque todos os seus vizinhos foram inspecionados
            open_lst.remove(n)
            closed_lst.add(n)
            
            if(IsFirstTime):
                #print("Ponto: {}, Custo: {:0.2f} ".format(start, poo[start] + self.h(start,stop)))

                CustoFinalHoras = math.floor(poo[start] + self.h(start,stop))
                CustoFinalMinutos = math.floor((poo[start] + self.h(start,stop) - CustoFinalHoras)*60)
                CustoFinalSegundos = (((poo[start] + self.h(start,stop) - CustoFinalHoras)*60) - CustoFinalMinutos)*60
                
                if CustoFinalHoras == 0:
                    print("Ponto: {}, Custo: - Tempo do trájeto mais rápido é de: {:0.2f} Minuto(s) e {:0.2f} Segundo(s)".format(start,CustoFinalMinutos,CustoFinalSegundos))
                else:
                    print("Ponto: {}, Custo: - Tempo do trájeto mais rápido é de: {:0.2f} Hora(s) e {:0.2f} Minuto(s) e {:0.2f} Segundo(s)".format(start,CustoFinalHoras,CustoFinalMinutos,CustoFinalSegundos))

                print("_____________________________________________________________________")
                IsFirstTime = False

            print("Fronteira: {}".format(open_lst))
            openToList = list(open_lst)
            for i in range(len(openToList)):
                #print("Ponto: {}, Custo: {:0.2f} ".format(openToList[i], poo[openToList[i]] + self.h(openToList[i],stop)))

                CustoFinalHoras = math.floor(poo[openToList[i]] + self.h(openToList[i],stop))
                CustoFinalMinutos = math.floor((poo[openToList[i]] + self.h(openToList[i],stop) - CustoFinalHoras)*60)
                CustoFinalSegundos = (((poo[openToList[i]] + self.h(openToList[i],stop) - CustoFinalHoras)*60) - CustoFinalMinutos)*60
                
                if CustoFinalHoras == 0:
                    print("Ponto: {}, Custo: - Tempo do trájeto mais rápido é de: {:0.2f} Minuto(s) e {:0.2f} Segundo(s)".format(openToList[i],CustoFinalMinutos,CustoFinalSegundos))
                else:
                    print("Ponto: {}, Custo: - Tempo do trájeto mais rápido é de: {:0.2f} Hora(s) e {:0.2f} Minuto(s) e {:0.2f} Segundo(s)".format(openToList[i],CustoFinalHoras,CustoFinalMinutos,CustoFinalSegundos))

            print("_____________________________________________________________________")

        print('O caminho não Existe!')
        return None

adjac_lis = {
    #Lista de Adjacências criada para representar o grafo das conexões das linhas de trêm. 
    #Com as distâncias e conexões reais
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
    print("Uma das linhas de trêm selecionadas não existe")
