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

def open_Text():
    try:
        t_file = open(filename, "r")
        lines = t_file.readlines()
        t_file.close()
        counter = 0
        for i in range(len(lines)):
            if len(lines) == 0:
                print("There are no todos for today")
            else:
                counter += 1
                print(str(counter) + " - " + lines[i].strip())
    except FileNotFoundError:
        return 0

def add_to_Text():
    try:
        t_file = open(filename, "a")
        user_input = input("Please add a new task: ")
        t_file.write("\n" + user_input)
        t_file.close()
    except IOError:
        print("Unable to write file.")


if len(sys.argv) == 1:
    print_usage_info()
elif len(sys.argv) == 2 or len(sys.argv) == 3:
    if sys.argv[1] == "-l":
        open_Text()
    elif sys.argv[1] == "-a":
        add_to_Text()
    elif sys.argv[1] == "-r":
        print("Reomves a task")
    elif sys.argv[1] == "-c":
        print("Completes a task")
    else:
        print("Unsupported argument")