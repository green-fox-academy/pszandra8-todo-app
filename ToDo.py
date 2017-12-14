import sys
filename = "Text.txt"

def print_usage_info():
    print(
        "Command Line Todo application\n"
        "=============================\n"
        "\nCommand line arguments:\n"
        "-l   Lists all the tasks\n" 
        "-a   Adds a new task\n"
        "-r   Removes a task\n"
        "-c   Completes a task\n")

if len(sys.argv) == 1:
    print_usage_info()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-l":
        print("Lists all tasks")
    elif sys.argv[1] == "-a":
        print("Adds a new task")
    elif sys.argv[1] == "-r":
        print("Reomves a task")
    elif sys.argv[1] == "-c":
        print("Completes a task")
    else:
        print("Unsupported argument")

def open_Text():
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        counter = 0
        for i in lines:
            counter += 1
            return str(counter) + ". " + i
    except FileNotFoundError:
        return 0

print(open_Text())