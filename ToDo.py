import sys
filename = "Text.txt"

class ToDo(object):
    def print_usage_info(self):
        print(
            "Command Line Todo application\n"
            "=============================\n"
            "\nCommand line arguments:\n"
            "-l   Lists all the tasks\n" 
            "-a   Adds a new task\n"
            "-r   Removes a task\n"
            "-c   Completes a task\n")

    def open_Text(self):
        try:
            t_file = open(filename, "r")
            lines = t_file.readlines()
            t_file.close()
            counter = 0
            if len(lines) == 0:
                print("There are no todos for today")
                print_usage_info()
            else:
                for i in range(len(lines)):
                    counter += 1
                    print(str(counter) + " - " + lines[i].strip())
        except FileNotFoundError:
            print("Dod not find the file")

    def add_to_Text(self):
        try:
            t_file = open(filename, "a")
            user_input = sys.argv[2]
            t_file.write("\n[ ] " + user_input)
            t_file.close()
            print("Task has been added to your ToDos")
        except IOError:
            print("Unable to write file.")

    def remove_Text(self):
        try:
            t_file = open(filename, "r")
            lines = t_file.readlines()
            lines_for_write = open(filename, "w")
            if sys.argv[2] == 1:
                lines.pop(0)
                print("Task has been removed from your ToDos")
            else:
                index = int(sys.argv[2]) - 1
                lines.pop(index)
                for line in lines:
                    lines_for_write.write(line)
                print("Task has been removed from your ToDos")
            t_file.close()
        except IOError:
            print("Unable to write file.")

    def check(self):
        try:
            t_file = open(filename, "r")
            lines = t_file.readlines()
            t_file.close()
            lines_for_write = open(filename, "w")
            index = int(sys.argv[2]) - 1
            lines[index] = "[x]" + lines[index][3:]
            lines_for_write.writelines(lines)
            t_file.close()
            print("The task has been checked")
        except FileNotFoundError:
            print("Dod not find the file")

todo = ToDo()

if len(sys.argv) == 1:
    todo.print_usage_info()
elif len(sys.argv) == 2 or len(sys.argv) == 3:
    if sys.argv[1] == "-l":
        todo.open_Text()
    elif sys.argv[1] == "-a":
        todo.add_to_Text()
    elif sys.argv[1] == "-r":
        todo.remove_Text()
    elif sys.argv[1] == "-c":
        todo.check()
    else:
        print("Unsupported argument")