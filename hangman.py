from operator import truediv
from re import T


def hungman(word):
    wrong=0
    stages=["__________          ",
            "|                   ",
            "|         |         ",
            "|         O         ",
            "|        /|\        ",
            "|        / \        ",
            "|______________     "]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ")
    while not win:
        print(" ".join(board))
        iletter=input("アルファベット文字を入力してください")
        if iletter in rletters:
            i=rletters.index(iletter)
            board[i]=iletter
            rletters[i]=""
        else:
            for stage in stages[:wrong+1]:
                print(stage)
            wrong+=1
        if wrong >= len(stages):
            print("お前は負けたんだよ！正解は{}".format(" ".join(word)))
            break
        if rletters == [""]*len(word):
            print("おめでとう！正解です"," ".join(board))
            win=True
hungman("masaaki")
