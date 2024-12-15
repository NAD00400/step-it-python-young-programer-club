import turtle 
t = turtle.Turtle()


def turtleMove():
    print("các lệnh khả dụng ")
    print("fd: ")
    print("bk: ")
    print("rt: ")
    print("lt: ")
    while True:
        command = input(">>>").lower()
        if command == "exit":
            break
        parts = command.split()
        if len(parts)!=2 :
            print("lệnh khônng hợp lệ !!")
            continue
        try:
            action ,value =parts
            value = int(value)
            if value <= 0 :
                print(" giá trị phải là 1 số nguyên dương ")
                continue
            elif action =="fd":
                t.fd(value)
            elif action == "bk":
                t.bk(value)
            elif action =="lt":
                t.lt(value)
            elif action =="rt":
                t.rt(value)
            else :
                print("lệnh không hợp lệ")
        except ValueError:
            print ('giá trị khôn hợp lệ vui lòng nhập số nguyên ')
turtleMove()
turtle.done()