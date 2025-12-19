'''
Email Id’s of  customers of an online shop are stored into a CSV file.
File is read and the data is stored into a string.
Write a Python program to count the email id’s with the particular domain name.
Hint: Use String functions like strip,split etc and Use Dictionary and List.
Example:
email = “raj@gmail.com,ravi@yahoo.com,sam.joseph@hotmail.com,yash@yahoo.com,giri@mycon.com,kaviya@gmail.com,kriti@hotmail.com”

Expected Output:
Gmail.com : [2 , ‘raj@gmail.com’, ‘kaviya@gmail.com’]
Hotmail.com: [ 2, ‘sam.joseph@hotmail.com’,’ kriti@hotmail.com’]
Yahoo.com: [2,’ ravi@yahoo.com’,’ yash@yahoo.com’]
Mycon.com:[1, giri@mycon.com]
'''

email = "raj@gmail.com,ravi@yahoo.com,sam.joseph@hotmail.com,yash@yahoo.com,giri@mycon.com,kaviya@gmail.com,kriti@hotmail.com"
lis = email.split(",")
print(lis)

dic = {}
print(dic.keys())

for l in lis:
    s = l.split("@")[1]
    if s in dic.keys():
        dic[s].append(l)
        dic[s][0] = len(dic[s])-1
    else:
        dic[s]=[1, l]

print(dic)
