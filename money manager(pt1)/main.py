from os import system
from time import sleep

global list
list = []

def delete(item):
    list.remove(item)

def add(item):
    list.append(item)



def main():
    while True:
        system("cls")
        print(list)
        print("add[a]")        
        print("delete[d]")
        inp = input(">> ")
        if inp in ["a", "A"]:
            system("cls")
            print("add")
            inp2 = input(">> ")
            add(inp2)
        elif inp in ["d", "D"]:
            while True:
                system("cls")
                print(list)
                print("delete")
                inp3 =  input(">> ")
                if inp3 in list:
                    delete(inp3)
                    break
                else:
                    system("cls")
                    print("havent deleted")
                    print("please enter the name correctly")
                    sleep(5)



if __name__ == "__main__":
    main()