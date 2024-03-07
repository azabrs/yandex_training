tcom, tcon = map(int,input().split())
mode = input() 

match mode:
    case "freeze":
        if tcon > tcom:
            print(str(tcom))
        else:
            print(str(tcon))
    case "heat":
        if tcon < tcom:
            print(str(tcom))
        else:
            print(str(tcon))
    case "auto":
        print(str(tcon))
    case "fan":
        print(str(tcom))
