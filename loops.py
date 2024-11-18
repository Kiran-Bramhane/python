# while loop 
i=1
while i <= 10:
    print("Check ",i)
    i += 1


for i in range(10):
    print("Check for ",i+1)

sum = 0
i = 1
num = int(input("Enter a number: "))
while i<=num:
    sum+=i
    i +=1
print("Sum ",sum)


s1=0
s="12345"
for i in s:
    s1 += int(i)
print("Sum of digits ",s1)


name = input("Name: ")
processed = set()
for i in name.lower():
    if i not in processed:
        print(f"{i} : {name.lower().count(i)}")
        processed.add(i)



s_name = "Tarant"
i=0
temp = ""
while i < len(s_name):
    if s_name[i] not in temp:
        temp += s_name[i]
        print(f"{s_name[i]} : {s_name.count(s_name[i])}")
    i += 1