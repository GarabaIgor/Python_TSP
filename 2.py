# -*- coding: utf-8 -*-
import numpy as np

import random
13
low = 100
high = 1000
size = 169
col = row = np.sqrt(size)
alpha = 4
beta = 2.5
#graph = np.random.randint(low,high,(size,)).reshape(row,col)

#graph = np.array([[110, 510, 788, 191, 130, 559, 772, 647, 801, 563, 872, 683, 130,
#        706, 236, 422, 147, 298, 135, 111],
#       [623, 345, 903, 386, 498, 456, 498, 414, 177, 515, 147, 453, 669,
#        350, 328, 875, 815, 847, 864, 875],
#       [355, 801, 140, 916, 700, 768, 963, 185, 824, 787, 627, 306, 648,
#        617, 926, 597, 682, 904, 540, 663],
#       [989, 579, 497, 128, 470, 903, 389, 248, 529, 533, 894, 451, 412,
#        464, 598, 706, 935, 949, 721, 679],
#       [331, 364, 360, 447, 465, 819, 145, 319, 714, 461, 299, 909, 614,
#        138, 870, 754, 896, 985, 712, 198],
#       [593, 216, 121, 208, 205, 990, 601, 817, 212, 624, 190, 447, 601,
#        505, 181, 505, 490, 411, 303, 184],
#       [768, 500, 462, 721, 259, 603, 106, 234, 786, 431, 822, 531, 896,
#        216, 599, 860, 608, 953, 129, 172],
#       [594, 678, 620, 229, 185, 130, 331, 460, 252, 238, 729, 845, 571,
#        619, 886, 189, 225, 822, 286, 656],
#       [579, 136, 373, 201, 221, 122, 879, 470, 307, 571, 938, 895, 923,
#        262, 572, 266, 570, 924, 891, 636],
#       [286, 253, 296, 156, 464, 252, 801, 127, 372, 204, 173, 252, 442,
#        749, 439, 671, 823, 676, 589, 637],
#       [153, 872, 218, 739, 381, 471, 223, 722, 940, 237, 200, 907, 743,
#        225, 790, 264, 636, 902, 286, 504],
#       [498, 248, 449, 168, 344, 255, 211, 746, 147, 928, 702, 497, 468,
#        692, 431, 454, 431, 493, 384, 640],
#       [476, 189, 334, 648, 116, 910, 429, 174, 873, 948, 690, 573, 589,
#        584, 879, 381, 370, 495, 388, 956],
#       [263, 436, 358, 268, 355, 656, 876, 758, 760, 765, 417, 381, 406,
#        676, 426, 704, 887, 314, 309, 906],
#       [404, 313, 917, 257, 847, 775, 874, 834, 368, 726, 256, 242, 764,
#        476, 606, 585, 411, 215, 988, 161],
#       [355, 190, 178, 457, 886, 375, 319, 497, 318, 561, 238, 601, 876,
#        509, 862, 178, 960, 153, 294, 144],
#       [165, 430, 167, 194, 717, 183, 648, 213, 382, 982, 382, 395, 186,
#        923, 555, 284, 132, 559, 946, 699],
#       [297, 838, 438, 136, 455, 467, 233, 397, 824, 458, 901, 477, 850,
#        899, 747, 569, 857, 787, 422, 844],
#       [421, 420, 577, 811, 993, 869, 197, 976, 257, 880, 975, 144, 895,
#        635, 585, 410, 145, 500, 361, 396],
#       [953, 525, 534, 119, 763, 513, 821, 852, 565, 226, 160, 154, 750,
#        787, 171, 306, 288, 749, 261, 133]])

graph = np.array([[110, 510, 788, 191, 130, 559, 772, 647, 801, 563, 872, 683, 130
                   ],
                  [623, 345, 903, 386, 498, 456, 498, 414, 177, 515, 147, 453, 669
                   ],
                  [355, 801, 140, 916, 700, 768, 963, 185, 824, 787, 627, 306, 648
                   ],
                  [989, 579, 497, 128, 470, 903, 389, 248, 529, 533, 894, 451, 412
                   ],
                  [331, 364, 360, 447, 465, 819, 145, 319, 714, 461, 299, 909, 614
                   ],
                  [593, 216, 121, 208, 205, 990, 601, 817, 212, 624, 190, 447, 601
                   ],
                  [768, 500, 462, 721, 259, 603, 106, 234, 786, 431, 822, 531, 896
                   ],
                  [594, 678, 620, 229, 185, 130, 331, 460, 252, 238, 729, 845, 571
                   ],
                  [579, 136, 373, 201, 221, 122, 879, 470, 307, 571, 938, 895, 923
                   ],
                  [286, 253, 296, 156, 464, 252, 801, 127, 372, 204, 173, 252, 442
                   ],
                  [153, 872, 218, 739, 381, 471, 223, 722, 940, 237, 200, 907, 743
                   ],
                  [498, 248, 449, 168, 344, 255, 211, 746, 147, 928, 702, 497, 468
                   ],
                  [476, 189, 334, 648, 116, 910, 429, 174, 873, 948, 690, 573, 589
                   ],
                  ])



#pher = np.zeros((row,col))
np.fill_diagonal(graph,0)

#Симметричная матрица
#for x in range(int(row)):
#    for y in range(int(row)):
#        graph[y][x] = graph[x][y]
print graph
print " "

tau = np.random.uniform(1.0,1.5,(size,)).reshape(row,col)
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
            tau[self.T[-2]][x] *= 0.9

        Lk = calc_distance(self.T)

        tau[self.T[-2]][self.T[-1]] += self.delta_tau/Lk

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
for x in range(10):

    obj = AntColony(start)
    obj.run_colony()



print "Иди в ближний выходим из стартовой:"
n_obj = neighbour()
n_obj.get_near(start)
print "T: %s L:%s " % (n_obj.near_list, calc_distance(n_obj.near_list))
