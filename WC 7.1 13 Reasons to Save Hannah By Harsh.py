inputString = input("Please Enter The Input String : ")
count = 0
for i in inputString:
    if i == '0':
        count = count + 1
    elif i == '1':
        count = count + 1
    elif i == '2':
        count = count + 1
    elif i == '3':
        count = count + 1
    elif i == '4':
        count = count + 1
    elif i == '5':
        count = count + 1
    elif i == '6':
        count = count + 1
    elif i == '7':
        count = count + 1
    elif i == '8':
        count = count + 1
    elif i == '9':
        count = count + 1
print("The Sum Of 10 space-separated integers denoting the frequency of each digit from 0 to 9 Is :",count)
if count == 13:
    print("Hannah survived")
else:
    print("Hannah did not survive")