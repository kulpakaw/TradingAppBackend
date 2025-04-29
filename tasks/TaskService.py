from tasks.TaskModel import TaskModel
from extensions import mongodb

class TaskService:

    @staticmethod
    def get_task():
        return mongodb.get_collection("tasks")

    @staticmethod
    def create_task(data):
        if TaskService.task_exists(data["name"]):
            raise Exception("Task o podanej nazwie już istnieje")

        model = TaskModel().load(data)
        print(model)

        TaskService.get_task().insert_one(model)

    @staticmethod
    def delete_task(data):
        print(data)
        task = TaskService.task_exists(data["name"])
        if not task:
            raise Exception("Nie znaleziono taska")
        return True

    @staticmethod
    def display_tasks(data):
        print(data)
        task = TaskService.task_exists(data["name"])
        if not task:
            raise Exception("Nie znaleziono użytkownika")
        return True

    @staticmethod
    def task_exists(name):
        task = TaskService.get_task().find_one({"name": name})
        return task