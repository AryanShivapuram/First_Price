import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm




n = int(input("no of times to run the game:"))
mean = int(input("mean of probability distribution of expected signals:"))
print(" ")
 
for p in range(n):
    print("Game ",p+1)
    stdev = random.uniform(1,2.5)
    
    sig_list=np.zeros((5))
    game=np.zeros((5))
    
    for j in range(5):
        sig_list[j]=np.random.normal(mean,stdev,1)  
        
    game[sig_list.argmax()] += 1
    print(" ")
    print(sig_list)
    print(game)
    print("winner of this round is ",sig_list.argmax()+1,"th player")
    print(" ")
    
    for i in range(4):
        for k in range(5):
            if (k!=sig_list.argmax()):
                sig_list[k]=random.uniform(sig_list[k]*(0.995),sig_list[k]*(1.05))
            else:
                sig_list[k]=random.uniform(sig_list[k]*(0.995),sig_list[k]*(1.005))
                
        print(sig_list)
        game[sig_list.argmax()] += 1
        print(game)
        print("winner of this round is ",sig_list.argmax()+1,"th player")
        print(" ")
        
    i_count=[]
    for l in range(5):
        if (game[l]==game.max()):
            i_count.append(l)
    
    winner = random.randint(0,len(i_count)-1)
        
    print("the winner of game",p+1,"is",i_count[winner]+1,"th player")
    print(" ")
    print(" ")