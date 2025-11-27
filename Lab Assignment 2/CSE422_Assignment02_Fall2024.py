# ---------------------------------------------------------------------------------------------------------------------
# PART 1

import math
import random
def overPen(slots, C, T):
    arr=[]
    overL=0
    for i in range(T):
        sloti= slots[i * C:(i + 1) * C]
        c=max(sloti.count("1")-1,0)
        overL+=c
    return overL
def consPen(slots, C, T):
    penl=0
    for i in range(C):
        penc = 0
        for j in range(T):
            penc+=int(slots[j * C + i])
        penl+=abs(penc-1)
    return penl

def fitnessCal(slots, C, T):
    penl= -(overPen(slots, C, T) + consPen(slots, C, T))
    return penl
def pop(c, t, popsize):
    poplist=[]

    for j in range(popsize):
        pop = ""
        for i in range(c * t):
            pop+=random.choice('01')
        poplist.append(pop)
    return poplist
def parentSelect(pop):
    return random.choice(pop),random.choice(pop)
def cross(parent1, parent2, C, T):
    point=random.randint(0, C * T - 1)
    child1=parent1[0:point]+parent2[point:]
    child2=parent2[0:point]+parent1[point:]
    return child1,child2
def mut(child, C, T):
    point=random.randint(1, C * T - 1)
    list1=list(child)
    if list1[point]=="1":
        list1[point]="0"
    else:
        list1[point]="1"
    return "".join(list1)

def genAlgo(C, T, popsize, i):
    population=pop(C, T, popsize)
    lowest=-math.inf
    selectedSlot=None
    for j in range(i):
        newPop=[]
        for j in range(popsize // 2):
            parent1,parent2=parentSelect(population)
            child1,child2=cross(parent1, parent2, C, T)
            newPop.extend([mut(child1, C, T), mut(child2, C, T)])
        population=newPop

        for slots in population:
            fitnessVal=fitnessCal(slots, C, T)
            if fitnessVal>lowest:
                lowest = fitnessVal
                selectedSlot = slots
            if lowest==0:
                break
    return lowest,selectedSlot

with open("inputA.txt") as f:
    N,T=[int(i) for i in f.readline().split(" ")]
    courses=[f.readline() for i in range(N)]

with open("outputA.txt", "w") as f1:
    if T<N:
        f1.write("TimeSlots can't be less than Number of Courses")
        print("TimeSlots can't be less than Number of Courses")
    else:
        fitness,schedule=genAlgo(N, T, popsize=100, i=1000)
        print("Part1 =>")
        f1.write(str(schedule))
        f1.write("\n")
        print(schedule)
        f1.write(str(fitness))
        print(fitness)
        print("")

# ---------------------------------------------------------------------------------------------------------------------
# PART 2

import random

def two_point_crossover(parent1, parent2):
    length = len(parent1)
    point1 = random.randint(0, length - 2)
    point2 = random.randint(point1 + 1, length - 1)
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1, child2

fitness, schedule = genAlgo(N, T, popsize=100, i=1000)

parent1 = ''.join(random.choice(schedule) for i in range(N * T))
parent2 = ''.join(random.choice(schedule) for i in range(N * T))

child1, child2 = two_point_crossover(parent1, parent2)

print("Part2 =>")
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
