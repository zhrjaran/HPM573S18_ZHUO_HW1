yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Tsinghua','Harvard','Stanford']
ours1 = mine + yours
ours2 =[]
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)

# Question 1:
# ours1 is a list which has 6 elements in and the element is string
# while ours2 is a list which has only 2 elements in and the element of ours2 is also list.

# Question 2:
yours[2] = 'Princeton'
print(ours1)
print(ours2)
# "+" just combine yours and mine into a new list named "ours",  it has the value of yours and mine;
# while when use .append(), ours2 just has the reference to yours and mine, so when we change any of them, ours2 would change
# That's why ours2 would change we alter yours
