from desk import Desk
from datetime import datetime

desks = []
command = ""

print("It's task tracker")
print("-----------------", end="\n\n\n")
command = input()
while( command.lower() != "exit" and command.lower() != "quit" ):
    if( command.lower()=="adddesk" or command.lower()=="cleatedesk" ):
        desks.append(Desk.__init__(input("Name of desk: "), input("Information about desk: ")))

    elif( command.lower()=="removedesk" or command.lower()=="dropdesk" ):
        if(len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if(desk.is_this_desk(deskName)):
                    del desk
                    isThisDesk = True
                    break
            if(isThisDesk):
                print("Desk is deleted")
            else:
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif( command.lower()=="deskdata" ):
        if(len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if(desk.is_this_desk(deskName)):
                    print(desk.send_details())
                    break
            if (not isThisDesk):
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif( command.lower()=="addtask" ):
        if (len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if (desk.is_this_desk(deskName)):
                    desk.add_task()
                    break
            if (not isThisDesk):
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif( command.lower() == "removetask" or command.lower() == "droptask" ):
        if (len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if (desk.is_this_desk(deskName)):
                    desk.drop_task(input("Name of task: "))
                    break
            if (not isThisDesk):
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif(command.lower() == "changedeskname"):
        if (len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if (desk.is_this_desk(deskName)):
                    desk.change_name(input("New name: "))
                    break
            if (not isThisDesk):
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif(command.lower() == "changetaskname"):
        if (len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if (desk.is_this_desk(deskName)):
                    desk.change_task_name(input("Name of task: "), input("New name of task: "))
                    break
            if (not isThisDesk):
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif(command.lower() == "changetaskdata"):
        if (len(desks)):
            deskName = input("Name of needed desk: ")
            isThisDesk = False
            for desk in desks:
                if (desk.is_this_desk(deskName)):
                    desk.change_task_info(input("Name of task: "), input("New information: "))
                    break
            if (not isThisDesk):
                print("Desk is not found")
        else:
            print("List of desks is empty.")

    elif (command.lower() == "tasklist"):
        if (len(desks)):
            deskName = input("Name of needed desk: ")
            if(deskName != ""):
                isThisDesk = False
                for desk in desks:
                    if (desk.is_this_desk(deskName)):
                        for task in desk.tasks():
                            print(task)
                        break
                if (not isThisDesk):
                    print("Desk is not found")
            else:
                for desk in desks:
                    for task in desk.tasks():
                        print(task)
        else:
            print("List of desks is empty.")