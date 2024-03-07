def bank(operations):
    client = {}
    for operation in operations:
        operation = operation.split()
        if operation[0] == "DEPOSIT":
            client[operation[1]] = client.get(operation[1], 0) + int(operation[2])
        elif operation[0] == "WITHDRAW":
            client[operation[1]] = client.get(operation[1], 0) - int(operation[2])
        elif operation[0] == "BALANCE":
            print(client.get(operation[1], "ERROR"))
        elif operation[0] == "TRANSFER":
            client[operation[1]] = client.get(operation[1], 0) - int(operation[3])            
            client[operation[2]] = client.get(operation[2], 0) + int(operation[3])
        elif operation[0] == "INCOME":
            for name, money in client.items():
                if money > 0:
                    client[name] = int(money * (1 + int(operation[1]) / 100))
infile = open("input.txt")
bank(infile.readlines())
                
