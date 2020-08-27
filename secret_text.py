text = input("Enter your text : ")

check = True
etext = ""
for chars in text:
    if(ord(chars)) <= 90 and ord(chars) <= 65:
        if((ord(chars) + 13) > 90):
            x = 64 + ((ord(chars) + 13) - 90)
        else:
            x = ord(chars) + 13
    elif(ord(chars) <= 122 and ord(chars) >= 97):
        if (ord(chars) + 13 > 122):
            x = 96 + ((ord(chars) + 13) - 122)
        else:
            x = ord(chars) + 13
    elif(ord(chars) == 32):
        x = 32
    else:
        check = False
        break
    etext = str(etext) + chr(x)
if(check == False):
    print("Invalid Characters found")
else:
    print(etext)
