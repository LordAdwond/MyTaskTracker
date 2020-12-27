from datetime import datetime
from task import Task

class Desk:
    def __init__(self, name, info): # constructor
        self.date_of_creation = datetime.today()
        self.date_of_modification = datetime.today()
        self.name = name
        self.info = info
        self.task_list = []

    def change_name(self, new_name): # changing a name of desk
        self.name = new_name
        self.date_of_modification = datetime.today()

    def add_task(self): # adding new task
        self.task_list.append(Task.__init__(input("Name: "), input("Info: "), input("Status: "), len(self.task_list)))
        self.date_of_modification = datetime.today()

    def drop_task(self, name): # deleting task
        if( len(self.task_list) ):
            is_task_found = False
            i = 0
            for task in self.task_list:
                if( task.is_this_task(name) ):
                    is_task_found = True
                    break
                else:
                    i += 1
            if(is_task_found):
                del self.task_list[i:i+1]
                print("Task is deleted")
                self.date_of_modification = datetime.today()
            else:
                print("Task with this name is not found")
        else:
            print("List of tasks is empty")

    def change_task_name(self, old_name, new_name): # changing name of task
        if (len(self.task_list)):
            is_task_found = False
            for task in self.task_list:
                if(task.is_this_task(old_name)):
                    is_task_found = True
                    task.change_name(new_name)
                    self.date_of_modification = datetime.today()
                    break
            if(not is_task_found):
                print("Task with this name is not found")
        else:
            print("List of tasks is empty")

    def change_task_status(self, name, new_status): # changing status of task
        if (len(self.task_list)):
            is_task_found = False
            for task in self.task_list:
                if(task.is_this_task(name)):
                    is_task_found = True
                    task.change_status(new_status)
                    self.date_of_modification = datetime.today()
                    break
            if(not is_task_found):
                print("Task with this name is not found")
        else:
            print("List of tasks is empty")

    def change_task_info(self, name, new_info): # changing info of task
        if (len(self.task_list)):
            is_task_found = False
            for task in self.task_list:
                if(task.is_this_task(name)):
                    is_task_found = True
                    task.change_info(new_info)
                    self.date_of_modification = datetime.today()
                    break
            if(not is_task_found):
                print("Task with this name is not found")
        else:
            print("List of tasks is empty")

    def send_task_details(self, name): # sending task details
        if (len(self.task_list)):
            is_task_found = False
            for task in self.task_list:
                if(task.is_this_task(name)):
                    is_task_found = True
                    return task.send_details()
            if(not is_task_found):
                print("Task with this name is not found")
        else:
            print("List of tasks is empty")

    def send_details(self): # generating a string with details of desk
        details1 = "Name of desk: "+self.name+"\nDate of creation: "+str(self.date_of_creation)+'\n'
        details2 = "Date of last modification: "+str(self.date_of_modification)+"\nInformation: "+self.info+'\n'
        return details1+details2

    def is_this_desk(self, name):
        return self.name == name

    def tasks(self):
        return self.task_list