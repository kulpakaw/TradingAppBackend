from flask import Blueprint, request
from tasks.TaskService import TaskService
from utils.json_msg import json_msg

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/create_task', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        TaskService.create_task(data)
        return json_msg("Utworzono nowego taska", "success", 201)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))


@tasks_bp.route('/delete_task', methods=['DELETE'])
def delete_task():
    try:
        data = request.get_json()
        TaskService.delete_task(data)
        return json_msg("Task usunięty", "success", 200)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))
   
@tasks_bp.route('/display_tasks', methods=['GET'])
def display_tasks():
    try:
        data = request.get_json()
        TaskService.display_tasks(data)
        return json_msg("Wyświetlono taski", "success", 200)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))