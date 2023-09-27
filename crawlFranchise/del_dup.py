lst = []
clear_lst = []
f2 = open("service.txt", 'r')
f3 = open("service_choijong.txt", 'w')
while True:
    line = f2.readline()
    if not line:
        break
    lst.append(line.strip('\n'))

print(lst)
for i in range(1, len(lst)):
    if lst[i] == lst[i-1]:
        continue
    clear_lst.append(lst[i])
print("\n\n\n\n\n\n\n\n\n\n")
print(clear_lst)

for i in clear_lst:
    f3.write(i + '\n')

f2.close()
f3.close()
