#all python codes
#python code on upper and lower case letters 
str="geeksforgeeks"
b=len(str)
str1=str[0:int(b/2)]
str2= str[int(b/2):int(b)]
print(str1 ,str2.upper())
-------------------------------------------->
#python code for detecting aplhanumerics
str="teja  has 2 books"
flag_1=False
flag_2=False
for i in str:
    if i.isalpha():
        flag_1=True
    if i.isdigit():
        flag_2=True
print(flag_1 and flag_2)
------------------------------------------->
#python code to check whether all vowels are present 
str="aeio"

vowels=set("aeiou")  
s=set()  #creates an empty set

for i in str:
    if i in vowels:
        s.add(i)
if len(s)==len(vowels):
    print("accepted")
else:
    print("not accepted")
  ---------------------------------------->
#python program to make first and last letter capital
str="hello world"
b=str[0].upper()+str[1:-1]+str[-1].upper()
print(b)
--------------------------------------------->
#python program to count similar characters in  two strings 
str1="teja"
str2="i am a human god in this universe"
count=0
s=set()
c=min(len(str1),len(str2))

for i in range (0 ,len(str1)):
    for j in range (0,len(str2)):
        if str1[i] not in s:
            if(str1[i]==str2[j]):
                 count=count+1
                 s.add(str1[i]) 
print(count)
------------------------------------------------>


