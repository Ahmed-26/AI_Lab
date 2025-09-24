no_list=[0,1]
target=52
while True:
    last=no_list[-1]
    last2nd=no_list[-2]
    next=last+last2nd
    if next > target:
        break
    no_list.append(next)

print(no_list)

no_list=[0,1]
for i in range(2,10):
    no_list.append(no_list[-1] + no_list[-2])
print(no_list)

