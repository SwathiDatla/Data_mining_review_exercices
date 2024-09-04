import itertools
#creating a     list
numbers = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]
#compute permutations
permutations = list(itertools.permutations(numbers))
#print the first five permutations for brevity
print("first 5 permutaions:")
for perm in permutations[:5]:
    print(perm)
    
    #combinations
combinations = list(itertools.combinations(numbers, 3))
#print the first 5 combinations for brevity
print("first 5 combinations of length 3:")
for comb in combinations[:5]:
    print(comb)
