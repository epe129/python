def Todo():
    tasks = []

    while True:
        kysy = input("Haluatko lisätä tehtävän (kyllä/ei): ")
        if kysy == "kyllä":
            tehtänä = input("Anna tehtävä: ")
            tasks.append(tehtänä)
        elif kysy == "ei":
            print("näkemiin")
            print(tasks)
            break


    with open("tehtavat.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    

Todo()
