#-----------------------------------------------------------------------------------------------------------------------

# Part 1

import math
import random
def alphabeta_algo(d, node_i, optimizer, l_tree, alpha, beta):
    if d == 5:

        return l_tree[node_i]

    if optimizer:
        maxval = -math.inf
        for i in range(2):
            maxed =alphabeta_algo(d + 1, node_i * 2 + i, False, l_tree, alpha, beta)
            maxval = max(maxval, maxed)
            alpha = max(alpha, maxed)
            if beta <= alpha:
                break
        return maxval
    else:
        minval = math.inf
        for i in range(2):
            mined = alphabeta_algo(d + 1, node_i * 2 + i, True, l_tree, alpha, beta)
            minval = min(minval, mined)
            beta = min(beta, mined)
            if beta <= alpha:
                break
        return minval


def match(gamer1=int(input("Enter starting player number : ")), depth=5):
    round=0
    if gamer1==1:
        gamer=True
    else:
        gamer=False

    winner_arr=[0,0]
    roundWinner_arr=[]
    alpha_inital=-math.inf
    beta_initial=math.inf
    for i in range(3):
        playoff_tree = []
        for i in range(2 ** depth):
            value = random.choice([-1, 1])
            playoff_tree.append(value)

        if gamer==1:
            winning_gamer=alphabeta_algo(depth, 0, gamer, playoff_tree, alpha_inital, beta_initial)

        elif gamer==0:
            winning_gamer = alphabeta_algo(depth, 0, gamer, playoff_tree, alpha_inital, beta_initial)

        if winning_gamer==1:
            roundWinner_arr.append("Subzero")
            winner_arr[1] += 1

        elif winning_gamer==-1:
            roundWinner_arr.append("Scorpion")
            winner_arr[0] += 1

        gamer= not gamer

    if winner_arr[0]>winner_arr[1]:
        print("Game winner: Scorpion")
    else:
        print("Game winner: Subzero")
    print(f"Total rounds played: {winner_arr[0]+winner_arr[1]}")
    for i in range(3):
        print(f"Winner of Round {i}: {roundWinner_arr[i]}")

match()

#-----------------------------------------------------------------------------------------------------------------------

# Part 2

import math

def alphabeta_dm_algo(n, tree_depth, alpha, beta, gamer_max_f):
    if tree_depth==0:
        return n.value
    if gamer_max_f:
        maxval = -math.inf
        for i in n.child:
            vals = alphabeta_dm_algo(i, tree_depth - 1, alpha, beta, False)
            maxval = max(maxval, vals)
            alpha = max(alpha, vals)
            if beta <= alpha:
                break
        return maxval
    else:
        minval = math.inf
        for j in n.child:
            vals = alphabeta_dm_algo(j, tree_depth - 1, alpha, beta, True)
            minval = min(minval, vals)
            beta = min(beta, vals)
            if beta <= alpha:
                break
        return minval
class Node:
    def __init__(self, nodevals, child_node=[]):
        self.value=nodevals
        self.child=child_node
def pacman(c):
    providedvals=[3, 6, 2, 3, 7, 1, 2, 0]

    l=[]
    for val in providedvals:
        l.append(Node(val))
    secondlevel=[]
    for i in range(0, len(l), 2):
        lchild = l[i]
        rchild = l[i + 1]
        secondlevel.append(Node(None, [lchild, rchild]))
    firstlevel = []
    for i in range(0, len(secondlevel), 2):
        lchild = secondlevel[i]
        rchild = secondlevel[i + 1]
        firstlevel.append(Node(None, [lchild, rchild]))
    root= Node(None, firstlevel)

    val_wo_magic=alphabeta_dm_algo(root, 3, -math.inf, math.inf, True)
    lsub_max= max(providedvals[:4])-c
    rsub_max=max(providedvals[4:])-c

    if lsub_max>val_wo_magic and lsub_max-val_wo_magic>=rsub_max-val_wo_magic :

        print(f"The new minimax value is {lsub_max}. Pacman goes left and uses dark magic.")
    elif rsub_max>val_wo_magic and lsub_max-val_wo_magic<=rsub_max-val_wo_magic:
        print(f"The new minimax value is {rsub_max}. Pacman goes right and uses dark magic.")
    else:
        print(f"The minimax value is {val_wo_magic}. Pacman does not use dark magic.")

pacman(int(input("Enter the value of c : ")))

#-----------------------------------------------------------------------------------------------------------------------
