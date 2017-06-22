
string = "sdfs   dfsf   11 s"




strNum = 0
spaceNum = 0
digitNum = 0


for x in string:
    print (x)

    print(x.isalpha())

    print(x.isspace())

    print(x.isdigit())


    if x.isalpha() == True:
        strNum += 1


    if x.isspace() == True:
        spaceNum += 1

    if x.isdigit() == True:
        digitNum += 1



print(strNum)

print(spaceNum)

print(digitNum)



print("字符串中有  %d 个字母  %d 个空格  %d 个数字 " % (strNum ,spaceNum ,digitNum))



