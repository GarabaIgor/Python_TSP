# -*- coding: utf-8 -*-
import numpy as np
import random



low = 100
high = 900
size = 25
col = row = np.sqrt(size)
alpha = 5
beta = 1


graph = np.random.randint(low,high,(size,)).reshape(row,col)
#pher = np.zeros((row,col))
np.fill_diagonal(graph,0)
for x in range(int(row)):
    for y in range(int(row)):
        graph[y][x] = graph[x][y]
print graph
print " "

#print "\ntau: "

#tau = np.random.randint(1,3,(size,)).reshape(row,col)
tau = np.random.uniform(0.5,0.7,(size,)).reshape(row,col)
np.fill_diagonal(tau,0)
#print tau

#self.self.near_list = []




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

        #Начальный город
        #self.current_city = Ant.city_quant
        self.current_city = start

#        Ant.city_quant -=1
        #Города которые нужно поситить
        self.J = range(int(row))
        self.J.remove(self.current_city)
        self.T = []
        self.T.append(int(self.current_city))


    def see(self):
        self.nu = []
        for x in range(int(row)):
            if not graph[self.current_city][x]:
                self.nu.append(0.0)
            else:
                self.nu.append(1.0/graph[self.current_city][x])

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
                break
#        print self.rul_list
#        print self.next_city

    def go_to_next_city(self):

        self.J.remove(self.next_city)
        self.T.append(self.next_city)

        #near(0)
        n_obj = neighbour()
        res = n_obj.get_near(self.T[0])
        self.Q = calc_distance(res)

        self.L = calc_distance(self.T)
        self.delta_tau = float(self.Q)/self.L



        for x in range(int(row)):
            tau[self.T[-2]][x] *= (1.0-0.1)

        tau[self.T[-2]][self.T[-1]] += self.delta_tau/5.0


        #Просто дописываем последнюю
        if len(self.T) == int(row):
            self.T.append(self.T[0])
            self.L = calc_distance(self.T)
        



class ann_imitation:
    def __init__(self,start,size):
        self.curr_solution = range(int(size))
        self.curr_solution.remove(start)
        self.curr_solution.insert(0,start)
        self.curr_solution.append(start)
        self.temperature = 10.0#100.0
        self.cool_rating = 0.9#0.9999
    def one_iter(self):
        self.w_solution = self.curr_solution[1:-1]
        random.shuffle(self.w_solution)
        self.w_solution.insert(0,self.curr_solution[0])
        self.w_solution.append(self.curr_solution[-1])
        self.w_solution_mark = calc_distance(self.w_solution)
        self.curr_solution_mark = calc_distance(self.curr_solution)
        if(self.w_solution_mark < self.curr_solution_mark):
            self.curr_solution = self.w_solution[:]
            self.temperature *= self.cool_rating
        elif(self.w_solution_mark > self.curr_solution_mark):
            prob = np.exp(-(self.w_solution_mark-self.curr_solution_mark)/self.temperature)
            if(random.random() <= prob):
                self.curr_solution = self.w_solution[:]
                self.temperature *= self.cool_rating
            else:
                self.temperature *= self.cool_rating
    def run(self):
        ind_iter = 0
        while(self.temperature > 0.1):
            ind_iter +=1
            self.one_iter()
            print "Iteration:%s  Way: %s and size: %s temperature:%s" %(ind_iter, self.curr_solution,self.curr_solution_mark,self.temperature)


#Количество муравьев равно количеству городов
class AntColony:
    def __init__(self,start):

        Ant.city_quant = row-1
        self.colony = []
        for x in range(int(row)):
            self.colony.append(Ant(start))
    def run_colony(self):
        for x in range(int(row-1)):
            for ant in self.colony:
                ant.see()
                ant.calc_prob()
                ant.calc_next_city()
            #Все перешли в города, а потом феромоны изменились(подсыпали испарилось)
            for ant in self.colony:
                ant.go_to_next_city()
        #Просто приписываю последнюю вершину
#        for ant in self.colony:
#            ant.T.append(ant.T[0])
        print "Муравьиная колония:"
#        print tau
        for ant in self.colony:

            print "T: %s L: %s" % (ant.T, ant.L)

#один муравей ходит
#class AntColony:
#    def __init__(self):
#
#        Ant.city_quant = row-1
#        self.colony = []
#        for x in range(1):
#            self.colony.append(Ant())
#    def run_colony(self):
#        for x in range(int(row-1)):
#            for ant in self.colony:
#                ant.see()
#                ant.calc_prob()
#                ant.calc_next_city()
#                ant.go_to_next_city()
#                print " "
#                print tau
#                print "T: %s L: %s Q:%s" % (ant.T, ant.L,ant.Q)
#        print "***RESULTS***"
#        for ant in self.colony:
#
#            print "T: %s L: %s" % (ant.T, ant.L)




start = 1

##print tau
#for x in range(10):
#    obj = AntColony()
#    obj.run_colony()
#    #print tau
#
#    print "Near list:%s" % self.near_list
#    print calc_distance(self.near_list)
##an_obj = ann_imitation(9,row)
##an_obj.run()

# Для многих

for x in range(10):

    obj = AntColony(start)
    obj.run_colony()
    #n_obj = neighbour()
    #res = n_obj.get_near(0)
#s = calc_distance(res)
#print "way:%s size:%s" % (res,s)
print "-"* 100
print "Иди в ближний выходим из стартовой:"
n_obj = neighbour()
n_obj.get_near(start)

print "T: %s L:%s " % (n_obj.near_list, calc_distance(n_obj.near_list))

print "Иди в ближний все:"
n_obj.get_near_all(start)
print "-"* 100

an_obj = ann_imitation(start,size=row)
an_obj.run()







