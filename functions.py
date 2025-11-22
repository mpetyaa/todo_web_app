FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of todos """
    with open(filepath, 'r') as f:  # w = write r = read
        t = f.readlines()
    return t

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in a text file """
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)

#print(__name__) #if you run functions directly __name__ will be equal to __main__ if you run main name will be functions
if __name__ == "__main__":
    print(get_todos())