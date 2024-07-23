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
