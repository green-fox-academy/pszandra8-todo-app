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
        if len(lines) == 0:
            print("There are no todos for today")
        else:
            for i in range(len(lines)):
                counter += 1
                print(str(counter) + " - " + lines[i].strip())
    except FileNotFoundError:
        return 0

def add_to_Text():
    try:
        t_file = open(filename, "a")
        user_input = sys.argv[2]
        t_file.write("\n[ ] " + user_input)
        t_file.close()
    except IOError:
        print("Unable to write file.")

def remove_Text():
    try:
        t_file = open(filename, "r")
        lines = t_file.readlines()
        lines_for_write = open(filename, "w")
        if sys.argv[2] == 1:
            lines.pop(0)
        else:
            index = int(sys.argv[2]) - 1
            lines.pop(index)
            for line in lines:
                lines_for_write.write(line)
        t_file.close()
    except IOError:
        print("Unable to write file.")

def check():
    try:
        t_file = open(filename, "r")
        lines = t_file.readlines()
        t_file.close()
        lines_for_write = open(filename, "a")
        for line in lines:
            if sys.argv[2] == 1:
                lines[0] = "[x] " + lines[0]
            else:
                index = int(sys.argv[2]) - 1
                lines[index] = "[x] " + lines[index]
        lines_for_write.writelines(lines)
        t_file.close()
            
    except FileNotFoundError:
        return 0
    
if len(sys.argv) == 1:
    print_usage_info()
elif len(sys.argv) == 2 or len(sys.argv) == 3:
    if sys.argv[1] == "-l":
        open_Text()
    elif sys.argv[1] == "-a":
        add_to_Text()
    elif sys.argv[1] == "-r":
        remove_Text()
    elif sys.argv[1] == "-c":
        check()
    else:
        print("Unsupported argument")