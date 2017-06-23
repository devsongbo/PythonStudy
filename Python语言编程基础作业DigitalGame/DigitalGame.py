

# 1.在设定的范围内生成随机数
# 2.用户猜数字
# 3.进行比对及处理




minNum = 0
maxNum = 100
randomNum = 0

inputNum = 0

def generateRandom():
    randomNum = random.randint(minNum, maxNum)
    print(randomNum)



generateRandom()



def userGuessNum():
    inputNumber = input('请随意输入一个整数整数')
    compareNum(inputNumber)

userGuessNum()



def compareNum(inputNum):

    intInputNum = int(inputNum)

    if intInputNum == randomNum:
        print('恭喜你才对了')
    elif intInputNum < randomNum:
        print('你猜小了')
    elif intInputNum > randomNum:
        print('你猜大了')

