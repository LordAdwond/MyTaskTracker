class Task:
    def __init__(self, name, info, task_status, id_of_task):
        self.name = name
        self.info = info
        self.status = task_status
        self.taskId = id_of_task

    def send_details(self):
        return "Name of task: "+self.name+"\nStatus: "+self.status+"\nInformation: "+self.info+'\n'

    def change_name(self, new_name):
        self.name = new_name

    def change_status(self, new_status):
        self.status = new_status

    def change_info(self, new_info):
        self.info = new_info

    def is_this_task(self, name):
        return self.name == name
