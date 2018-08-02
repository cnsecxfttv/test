import itertools
permut = itertools.permutations(range(1,8),4)
count_permut = []
for i in permut:
    count_permut.append(i)
    print(count_permut.index(i)+1, i)

print('number of permutations', + len(count_permut))

