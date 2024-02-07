import numpy as np

def get_combinations(die_a,die_b):
    combinations=[]
    for i in range(0,len(die_a)):
        for j in range(0,len(die_b)):
            combinations.append([die_a[i],die_b[j]])
    return combinations

def get_sums(combinations):
    sums={}
    for i in combinations:
        temp_sum=sum(i)
        if temp_sum in sums:
            sums[temp_sum]+=1
        else: sums[temp_sum]=1
    return sums
def get_probabilities(sums,total_combinations):
    prob_sums={}
    for i in sums:
        prob_sums[i]=round(sums[i]/total_combinations,ndigits=3)
    return prob_sums

def undoom_dice(die_a,die_b):
    original_combinations=get_combinations(die_a,die_b)
    original_sums=get_sums(original_combinations)
    for i in range(111114, 133335):
        new_die_a=list(map(int,str(i)))
        if max(new_die_a)>4: 
            continue
        for j in range (111118,177779):
            new_die_b=list(map(int,str(j)))
            new_combinations=get_combinations(new_die_a,new_die_b)
            new_sums=get_sums(new_combinations)
            if new_sums==original_sums : break
        if new_sums==original_sums : break
    return new_die_a,new_die_b


die_a=[1,2,3,4,5,6]
die_b=[1,2,3,4,5,6]
# PART A
# 1

combinations=get_combinations(die_a,die_b)
total_combinations=len(combinations)
print("The total possible combinations of the result of rolling two dice are:",total_combinations)
print()

#2

combinations_np=np.array(combinations).reshape(6,-1,2)
print("The combinations are:")
for i in combinations_np:
    print(*i,sep=",")
print()

#3
sums=get_sums(combinations)
prob_sums=get_probabilities(sums,total_combinations)
print("The probability of each sum of the faces of two dice are:")
for i in prob_sums:
    print(i,":",prob_sums[i])
print()

# PART 2
# 1
new_die_a,new_die_b=undoom_dice(die_a,die_b)
print("The new dice are:")
print("Die A: ",new_die_a)
print("Die B: ",new_die_b)
print()

new_combinations=get_combinations(new_die_a,new_die_b)
new_combinations_np=np.array(new_combinations).reshape(6,-1,2)
print("The new combinations are:")
for i in new_combinations_np:
    print(*i,sep=",")
print()

print("The probability of each sum of the faces of the two dice are the same, which are:")
new_sums=get_sums(new_combinations)
new_prob_sums=get_probabilities(new_sums,total_combinations)
for i in new_prob_sums:
    print(i,":",new_prob_sums[i])
print()

