def message(inputMessage):
    inputMessage = inputMessage + " is the message."
    return inputMessage

def myFun():

    subject = "It will rain tomorrow"
    print(subject)

    # subjectを値として渡します。
    # subjectの中のデータは messageの仮パラメータにコピーされます。
    # 出力はnewMessageに格納されます
    newMessage = message(subject)

    print(subject)
    print(newMessage)


myFun()




