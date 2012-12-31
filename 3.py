# -*- coding: utf-8 -*-
import numpy as np

import random
low = 1
high = 10
size = 16
col = row = np.sqrt(size)
alpha = 1
beta = 1

graph = np.random.randint(low,high,(size,)).reshape(row,col)
#graph = np.array([[110, 510, 788, 191, 130, 559, 772, 647, 801, 563, 872, 683, 130
#                  ],
#                  [623, 345, 903, 386, 498, 456, 498, 414, 177, 515, 147, 453, 669
#                  ],
#                  [355, 801, 140, 916, 700, 768, 963, 185, 824, 787, 627, 306, 648
#                  ],
#                  [989, 579, 497, 128, 470, 903, 389, 248, 529, 533, 894, 451, 412
#                  ],
#                  [331, 364, 360, 447, 465, 819, 145, 319, 714, 461, 299, 909, 614
#                  ],
#                  [593, 216, 121, 208, 205, 990, 601, 817, 212, 624, 190, 447, 601
#                  ],
#                  [768, 500, 462, 721, 259, 603, 106, 234, 786, 431, 822, 531, 896
#                  ],
#                  [594, 678, 620, 229, 185, 130, 331, 460, 252, 238, 729, 845, 571
#                  ],
#                  [579, 136, 373, 201, 221, 122, 879, 470, 307, 571, 938, 895, 923
#                  ],
#                  [286, 253, 296, 156, 464, 252, 801, 127, 372, 204, 173, 252, 442
#                  ],
#                  [153, 872, 218, 739, 381, 471, 223, 722, 940, 237, 200, 907, 743
#                  ],
#                  [498, 248, 449, 168, 344, 255, 211, 746, 147, 928, 702, 497, 468
#                  ],
#                  [476, 189, 334, 648, 116, 910, 429, 174, 873, 948, 690, 573, 589
#                  ],
#                  ])
np.fill_diagonal(graph,0)
tau = np.random.uniform(1.0,3.0,(size,)).reshape(row,col)
#tau = np.random.random_integers(low=1,high=3,size=(4,4))
np.fill_diagonal(tau,0)

def calc_distance(way):

    distance = 0
    for x in range(1,len(way)):
        distance += graph[way[x-1]][way[x]]
        #print "Distance of %s  is  %s" % (way,self.L)
    return distance

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

class  Ant:
    city_quant = row-1

    def __init__(self,start):
        self.J = range(int(row))
        self.J.remove(start)
        self.T = []
        self.T.append(start)
        self.see()

    def see(self):
        self.nu = []
        for x in range(int(row)):
            if not graph[self.T[-1]][x]:
                self.nu.append(0.0)
            else:
                self.nu.append(1.0/graph[self.T[-1]][x])



    def calc_prob(self):
        self.prob = []
        self.denom = 0
        for one_of_next in self.J:
            self.denom += (tau[self.T[-1]][one_of_next]**alpha) * (self.nu[one_of_next]**beta)
#        print self.denom
        for one_of_next in range(int(row)):
            if one_of_next in self.J:
                self.prob.append(((tau[self.T[-1]][one_of_next]**alpha) * (self.nu[one_of_next]**beta))/self.denom)
#                print "tau %f * nu %f = %f" %(tau[self.T[-1]][one_of_next],self.nu[one_of_next],tau[self.T[-1]][one_of_next]*self.nu[one_of_next])
#                print  self.prob
            else:
                self.prob.append(0.0)

    def calc_next_city(self):
        if len(self.J) == 1:
            self.next_city = self.J[-1]
        elif len(self.J) == 0:
            self.next_city = self.T[0]
        else:
            self.rul_list = []
            for x in range(int(row)):
                if not self.prob[x]:
                    self.rul_list.append(0.0)
                else:
                    self.rul_list.append(sum(self.prob[:x+1]))
            rnd = random.uniform(0.0,1.0)
#            print "rnd"
#            print rnd
            for x in self.rul_list:
                if rnd <= x:
                    self.next_city = self.rul_list.index(x)
#                    print "rul_list"
#                    print self.rul_list
#                    print "next_city"
#                    print self.next_city
                    break

    def go_to_next_city(self):
        self.T.append(self.next_city)
        if self.J:
            self.J.remove(self.next_city)
#            print self.J
#            print self.T
        else:
            self.L = calc_distance(self.T)
            self.change_pher()
            print "Length: " + "-"*80 + "%d" % self.L
            print self.T


    def change_pher(self):
#        way = self.T[:]
#        way.append(self.T[0])
        Q = 50
        ro = 0.9
        self.L = calc_distance(self.T)
        self.delta_tau = Q/self.L
        print "delta tau: %f" % self.delta_tau
        for x in range(len(self.T)-1):
            tau[self.T[x]][self.T[x+1]] += self.delta_tau
        for x in range(int(row)):
            for y in range(int(row)):
                if x!=y:
                    if tau[x][y]<=0: tau[x][y] = np.random.uniform(1.0,3.0)
                    else: tau[x][y] *= ro


print tau
print



for x in range(10):
    obj = Ant(0)
    for x in range(int(row)):

        obj.calc_prob()
        obj.calc_next_city()
        obj.go_to_next_city()
#    print x
    print tau

#print [x.argmax() for x in tau]


print "graph:"
print graph
#print "tau:"
#print tau
#print "nu:"
#print obj.nu


print "Иди в ближний выходим из стартовой:"
n_obj = neighbour()
n_obj.get_near(0)
print "T: %s L:%s " % (n_obj.near_list, calc_distance(n_obj.near_list))

