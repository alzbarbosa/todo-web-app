import time

FILEPATH = "todos.txt"
FILEPATH2 = "completetodos.txt"

def get_todos(filepath=FILEPATH):
    """
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_new:
        file_new.writelines(todos_arg)


def write_complete_todos(todos_arg, filepath=FILEPATH2):
    with open(filepath, 'a') as file_new:
        todos_arg_split = todos_arg.split("\n")
        todos_arg_split = time.strftime("%b %d, %Y") + " " + "-" + " " + str(todos_arg_split[0]) + "\n"
        file_new.writelines(todos_arg_split)


def get_complete_todos(filepath=FILEPATH2):
    with open(filepath, "r") as file_local:
        completed_todos_local = file_local.readlines()
    return completed_todos_local


if __name__ == "__main__":
    print(get_todos())