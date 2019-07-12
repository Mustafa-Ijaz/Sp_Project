# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:14:27 2019

@author: Bilal
"""

import random
import heapq
# Number of individuals in each generation
POPULATION_SIZE = 100
# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
# Target string to be generated
TARGET = "FALL/16/BScs/035"
class Individual:
    '''
    Class representing individual in population
    '''
    def __init__(self, chromosome,fitness):
        self.chromosome = chromosome
        self.fitness = fitness
        
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        return (GENES[random.randint(0,len(GENES)-1)])
    
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''
        for i in range(len(TARGET)):
            self.chromosome+=self.mutated_genes()
            
    def mate(self, par2):
        '''
        Perform mating and produce new offspring
        '''
        # chromosome for offspring
        child_chromosome = ''
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):
            prob = random.random()
            if(prob < 0.45):
                child_chromosome+=gp1
            elif(prob > 0.45 and prob <0.90):
                child_chromosome+=gp2
            else:
                child_chromosome+=self.mutated_genes()
        return child_chromosome
    
    def cal_fitness(self):
        self.fitness=0
        for i in range(len(TARGET)):
            if(TARGET[i]!=self.chromosome[i]):
                self.fitness+=1
                
population=[]
for i in range(POPULATION_SIZE):
    ind=Individual('',0)
    ind.create_gnome()
    ind.cal_fitness()
    heapq.heappush(population,[ind.fitness,ind.chromosome])
    
for i in range(100000):
    sol1=heapq.heappop(population)
    sol2=heapq.heappop(population)
    ind1 =Individual(sol1[1],sol1[0])
    ind2 =Individual(sol2[1],sol2[0])
    ind3= Individual(ind1.mate(ind2),0)
    ind3.cal_fitness()
    sol3=[ind3.fitness,ind3.chromosome]
    
    print("Generation: " + str(i+1) + " Solution: " + sol3[1] + " Fitness: " + str(sol3[0]))
    if(TARGET==sol3[1]):
        break
    else:
        heapq.heappush(population,[sol1[0],sol1[1]])
        heapq.heappush(population,[sol2[0],sol2[1]])
        heapq.heappush(population,[sol3[0],sol3[1]])