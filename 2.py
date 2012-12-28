# -*- coding: utf-8 -*-
import numpy as np
import random

low = 1
high = 100
size = 100
col = row = np.sqrt(size)
alpha = 4
beta = 2.5
graph = np.random.randint(low,high,(size,)).reshape(row,col)
#pher = np.zeros((row,col))
np.fill_diagonal(graph,0)

#Симметричная матрица
#for x in range(int(row)):
#    for y in range(int(row)):
#        graph[y][x] = graph[x][y]
print graph
print " "

tau = np.random.uniform(1.0,2.0,(size,)).reshape(row,col)
np.fill_diagonal(tau,0)

class neighbour:
    def __init__(self,):
        self.near_list = []
        self.near_listS = []
    def get_near(self,start):
        self.near(start,self.near_list)
        self.near_list.append(int(start))
        return self.near_list[:]
    def get_near2(self,start):
        self.near(start,self.near_list)
        #self.near_list.append(int(start))
        return self.near_list[:]
    def get_near_all(self,start):
        for x in range(int(row)):
            self.near_list = []
            self.near_listS.append(self.get_near2(x))
        for y in self.near_listS:
            self.roll_list(y,start)
        return self.near_listS[:]
    def roll_list(self,l,start):
        print l
        start_index = l.index(start)
        result_list = l[start_index:] +l[:start_index]

        result_list.append(start)
        print result_list,calc_distance(result_list)

    def near(self,start,near_list):
        #global self.near_list
        if not near_list:
            near_list.append(int(start))

        if len(near_list) == row:
            #print "!!!!!%s" % self.near_list
            return
        #for graphRow in graph:
        else:
            nonZeroIndexes = np.nonzero(graph[start])[0]
            min = graph[start].max()

            minInd = graph[start].argmax()

            for nonZeroInd in nonZeroIndexes:
                if (nonZeroInd not in near_list) and (graph[start][nonZeroInd] <= min):
                    minInd = nonZeroInd
                    min = graph[start][nonZeroInd]
                    #self.near_list.append(minInd)


            near_list.append(minInd)
            self.near(minInd,near_list)

def calc_distance(way):

    distance = 0
    for x in range(1,len(way)):
        distance += graph[way[x-1]][way[x]]
        #print "Distance of %s  is  %s" % (way,self.L)
    return distance

class  Ant:
    city_quant = row-1

    def __init__(self,start):
        self.current_city = start
        self.J = range(int(row))
        self.J.remove(self.current_city)
        self.T = []
        self.T.append(int(self.current_city))
        self.see()

    def see(self):
        self.nu = []
#        print self.nu
        for x in range(int(row)):
            if not graph[self.current_city][x]:
                self.nu.append(0.0)
            else:
                self.nu.append(1.0/graph[self.current_city][x])
#        print self.nu
                #self.nu = [1.0/graph[self.current_city][x] for x in range(row)]
    def calc_prob(self):
        self.prob = []
        self.denom = 0
        for next_city in self.J:
            self.denom += (tau[self.current_city][next_city]**alpha) * (self.nu[next_city]**beta)
            #print self.denom
        for next_city in range(int(row)):
            if next_city in self.J:
                self.prob.append(((tau[self.current_city][next_city]**alpha) * (self.nu[next_city]**beta))/self.denom)
            else:
                self.prob.append(0.0)
        self.current_city = self.T[-1]
    #        print self.T, self.current_city
    def calc_next_city(self):
        self.rul_list = []
        for x in range(int(row)):
            if not self.prob[x]:
                self.rul_list.append(0.0)
            else:
                self.rul_list.append(sum(self.prob[:x+1]))
        rnd = random.uniform(0.0,1.0)
        #        print rnd
        for x in self.rul_list:
            if rnd <= x:
                self.next_city = self.rul_list.index(x)
#                print self.nu
#                print tau
#                print self.prob
#                print rnd
#                print self.rul_list
#                print self.next_city
                break


    def go_to_next_city(self):

        self.J.remove(self.next_city)
        self.T.append(self.next_city)

        self.current_city = self.T[-1]

        #Просто дописываем последнюю
        if len(self.T) == int(row):
            self.T.append(self.T[0])
            self.L = calc_distance(self.T)

    def add_pher(self):
        n_obj = neighbour()
        res = n_obj.get_near(self.T[0])
        self.Q = calc_distance(res)

        self.L = calc_distance(self.T)
        self.delta_tau = float(self.Q)/self.L



        for x in range(int(row)):
            tau[self.T[-2]][x] *= (1.0-0.1)

        tau[self.T[-2]][self.T[-1]] += self.delta_tau/20.0

class AntColony:
    def __init__(self,start):

        Ant.city_quant = row-1
        self.colony = []
        for x in range(int(row)):
            self.colony.append(Ant(start))
    def run_colony(self):
        for x in range(int(row-1)):
            for ant in self.colony:

                ant.calc_prob()
                ant.calc_next_city()
                ant.go_to_next_city()
                ant.see()
                #Все перешли в города, а потом феромоны изменились(подсыпали испарилось)
            for ant in self.colony:
                ant.add_pher()

                #Просто приписываю последнюю вершину
            #        for ant in self.colony:
            #            ant.T.append(ant.T[0])
        print "Муравьиная колония:"
        #        print tau
        for ant in self.colony:

            print "T: %s L: %s" % (ant.T, ant.L)
#        print tau

start = 1

#print tau
for x in range(5):

    obj = AntColony(start)
    obj.run_colony()



print "Иди в ближний выходим из стартовой:"
n_obj = neighbour()
n_obj.get_near(start)
print "T: %s L:%s " % (n_obj.near_list, calc_distance(n_obj.near_list))
