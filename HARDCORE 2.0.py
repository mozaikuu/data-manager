listofchamps = []
with open ( "champs.txt" , "r", encoding="utf-8") as reader:
    listofchamps = list(dict.fromkeys(listofchamps))

print(listofchamps)
print(len(listofchamps))
function=("")
    

def addchamp():
    addchamp = input("enter the champ name " + "(press enter to skip) :")
    if addchamp in listofchamps:
        print("already in list")
        main()
    elif addchamp not in listofchamps:
        listofchamps.append(addchamp)
        print(addchamp + " has been added")
        main()

    elif addchamp==("no" , "quit" , "" , "exit"):
        main()
    else:
        print("invalid input")
        addchamp()




def removechamp():
    removechamp = input("enter the champ name: ")
    if removechamp in listofchamps:
        listofchamps.remove(removechamp)
        print(removechamp + " has been removed")
        main()
    else:
        print("not found")
        removechamp()



def searchchamp():
    print("enter the champ name " + "(press enter to end) :")
    champion = input()
    if champion == ("" , "no" , "quit" , "exit" , "end"):
        main()

    elif champion in listofchamps:
        print(champion + " is in the list")
        searchchamp()
    else:
        print(champion + " is not in the list")
        searchchamp()




def listchamps():
    print(listofchamps)
    main()



def end():
    print("press enter to close <3. goodbye")
    with open("champs.txt", "w", encoding="utf-8") as file:
        for name in listofchamps:
            file.write(name)


def main():
    print("main = 1 /" , "add champ = 2 /" , "remove champ = 3 /" , "search champ = 4 /" , "list champs = 5 /" , "end = 6")
    print("what would you like to do?: ")
    function = input()


    # TODO: Sdadsd
    if function=="1":
        main()
    elif function=="2":
        addchamp()
    elif function=="3":
        removechamp()
    elif function=="4":
        searchchamp()
    elif function=="5":
        listchamps()
    elif function=="6":
        end()
    else:
        print("invalid input")
        main()

        
main()