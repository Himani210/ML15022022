#Q2
print(5**9)
print(3//2)
7//3
7/3
6 == 6

### Q3

s1='Nice to have it '
s2='here'
print(s1+s2)

#Q4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a1=a[3]
a2=a1[1]
a3=a2[2]
a4=a3[0]
print(a4)

#Q5
a.append(s2)
print(a)
a.insert(0,s1)
print(a)


#Q6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
list=[]
for i in numbers:
    if i%2==0 and i<237:
        list.append(i)
print(list)


#Q7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)


##
###Q9
##n=int(input("Enter your number :"))
##for i in range(n):
##    print()

#Q11
z=input().split(',')
print(z)
z.sort()
print(z)


##
##
###Q12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
h=d['Marks']
#print(max(h))
topper=h.index(max(h))
a=d['Student']
print(a[topper])

#Q13
l='hello world!123'
w=[]
for i in l:
    w.append(i)
print(w)
y=['0','1','2','3','4','5','6','7','8','9']
countn=0
counta=0
for j in w:
    if j.isalpha():
        counta=counta+1
    elif j in y:
        countn=countn+1
    else:
        print(' ')

print("Number of alphabets :",counta)
print("Number of digits :",countn)
    


