from random import randint
from datetime import datetime
from time import sleep

def color_generator(n_colors, n_repetitions): # Generate palette of colors.
    for r in range(n_repetitions): # Repeat several times.
        colors_list = []
        while len(colors_list) != n_colors: # How many colors are needed?
            color = ""
            for char in range(6): # Hex color code has 6 characters.
                color += f"{randint(0, 15):x}"
            if color not in colors_list:
                colors_list.append(color)
        yield colors_list
        
def file_dir(): # Get the file directory to save the log file and backup file.
    full_path = __file__
    indx = full_path[-1::-1].find("\\")
    fdir = full_path[0:1].upper() + full_path[1:-indx]
    return fdir

# Check function 1
def check_nrepetitions(number_rep):
    try:
        number_rep = int(number_rep)
    except:
        return 100
    return number_rep

# Check function 2
def check_name(fil_name):
    if "/" in fil_name or "\\" in fil_name or "<" in fil_name \
        or ">" in fil_name or "?" in fil_name or "|" in fil_name \
            or "*" in fil_name or ":" in fil_name or '"' in fil_name:
        return "backup.css"
    if fil_name == ".css":
        return "backup.css"
    return fil_name

# Check function 3
def check_mode(mode):
    if (mode.lower()[0] == "t") and (mode[1].isdigit()) and (len(mode) == 2) and (int(mode[1]) >= 1):
        return (int(mode[1]) * 5)
    else:
        return "p"

def log_writer(log):
    with open(file_dir() + "Color_Injector_log_file.log", "a") as logfile:
        logfile.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {log}\n")

def search_into_css_file(all_lines_of_file): # Finding the right lines from the CSS file to inject color codes.
    global all_indexes_list, background_index_list, color_index_list
    inline = 1
    background_index_list = []
    color_index_list = []
    print("Searching result:")
    for line in all_lines_of_file:
        if "background-color" in line.strip():
            background_index_list.append(inline-1)
            print(f"{inline}: {line.strip()}")
        elif "color" in line.strip():
            color_index_list.append(inline-1)
            print(f"{inline}: {line.strip()}")
        inline += 1
    all_indexes_list = color_index_list + background_index_list
    
def getting_backup(all_lines_for_backup, backup_fname):
    with open(file_dir() + backup_fname, "a") as bfile:
        bfile.writelines(all_lines_for_backup)
        log_writer(f"A backup of the CSS file has been created. Path: {file_dir() + backup_fname}")    

def user_choices(): # Getting user choices list.
    global choices_list
    while True:
        choices_list = input("Enter the number of lines to inject color and split them with ',' (ex: 'all' or 'abc' or 'ac' or '23, 36, 39'): ").strip().split(",")
        if choices_list[0].lower() == "all":
            choices_list = list(map(lambda x: (x+1), all_indexes_list))
        elif choices_list[0].lower() == "abc":
            choices_list = list(map(lambda x: (x+1), background_index_list))
        elif choices_list[0].lower() == "ac":
            choices_list = list(map(lambda x: (x+1), color_index_list))
        else:
            try:
                choices_list = list(map(lambda x: int(x.strip()), choices_list))
            except:
                print("You have entered an invalid value! Please try again or enter '0' to cancel.")
                continue
        flag = 0
        for num in choices_list:
            if (num-1) not in all_indexes_list:
                flag = 1
                break
        if flag == 0:
            log_writer(f"Selected lines: {choices_list}")
            break
        elif choices_list == [0]:
            log_writer("Selection canceled! Color injection was stopped.")
            break
        else:
            print("You have entered an invalid value! Please try again or enter '0' to cancel.")
          
def css_file_manager(css_file_path, backup_file_name, number_of_repetitions, injection_mode): # Main function
    with open(css_file_path, "r") as cfile:
        all_lines = cfile.readlines()
    
    # Preparing for color injection.
    getting_backup(all_lines, backup_file_name)
    search_into_css_file(all_lines)
    user_choices()

    # Cancel color injection.
    if choices_list == [0]:
        return
    
    counter = 1
    for clr_list in color_generator(len(choices_list), number_of_repetitions):
        log_writer(f"|N{counter}| List of colors: {clr_list}")
        clr_indx = 0
        for num in choices_list:
            if (num-1) in background_index_list:
                all_lines.insert((num-1), f"    background-color: #{clr_list[clr_indx]};\n")
                all_lines.pop(num)
            elif (num-1) in color_index_list:
                all_lines.insert((num-1), f"    color: #{clr_list[clr_indx]};\n")
                all_lines.pop(num)
            clr_indx += 1
        with open(css_file_path, "w") as cfile:
            cfile.writelines(all_lines)
        if injection_mode == "p":
            stopinjection = input(f"[List number: {counter}] Press enter for change color or enter 'e' or 'q' to exit: ").strip()
            if (stopinjection.lower() == "e") or (stopinjection.lower() == "q"):
                break
        else:
            print(f"[List number: {counter}] If you want to stop the injection, press 'Ctrl + C'.")
            try:
                sleep(injection_mode)
            except:
                break
        counter += 1

while True:
    print("-----------------------------------------------\
    \nWelcome to Color Injector program. \
    \n[0] Help \
    \n[1] Color Injector \
    \n[2] Exit \
    \n-----------------------------------------------")
    choose = input("Enter your choice: ")
    print("-----------------------------------------------")
    if choose == "0": # Help
        print(f"""###############################################
Help Content:
- Why was this tool created? 
--- To change colors more easily and find good color combinations for web pages.
Don't worry about mistakes in inputs, all inputs will be checked.

- How can I use it?
--- Step 1: Open the program.
--- Step 2: Enter '1'.
--- Step 3: Enter number of repetitions, like 80, then you can change colors for 80 times.
--- Step 4: Enter path of CSS file for color injection.
--- Step 5: Enter an appropriate name (without these characters: \/:*?"<>|) for the new backup file.
You don't need to end the name with '.css'.
--- Step 6: Enter mode. If you want to change colors every 10 seconds, enter 't2' (t1=5s, t2=10s, t3=15s, tn=n*5s).
If you want to change colors with pressing 'Enter', enter 'p'.
--- Step 8: Select lines for color injection like '8, 12, 21',
or enter 'all' to select all lines,
or enter 'abc' to select all background-colors,
or enter 'ac' to select all colors.
--- Step 7: Open HTML file on 'Live Server' (it is a 'VS Code' extension).
--- Step 8: After selecting color, if you enter 'p' mode, enter 'e' or 'q' to stop injection,
or if you enter 't' mode, press 'Ctrl + C' to stop injection.
--- Step 9: Enter 'q' or 'e' or '2' to exit the program.

- Where is the log file?
--- It will be saved in the program directory. Right here: {file_dir()}

- What information will be in the log file?
--- Here is the test log:
[14-10-2022 17:30:02] ********** Color Injector launched. **********
[14-10-2022 17:30:05] Number of repetitions: 30
[14-10-2022 17:30:14] Path of CSS file: E:\PYTHON_Projects\Menu1\Menu1.css
[14-10-2022 17:30:19] Backup name: 'mytest.css'
[14-10-2022 17:30:25] A backup of the CSS file has been created. Path: E:\PYTHON_Projects\Color_Injector\mytest.css
[14-10-2022 17:30:29] Selected lines: [16, 26, 6, 17, 25]
[14-10-2022 17:30:29] |N1| List of colors: ['aecea9', '250aeb', '7ac26b', '6ab6a0', '4084bf']
[14-10-2022 17:30:34] |N2| List of colors: ['38bdfd', '618657', 'c0ae40', '868861', '4f7314']
[14-10-2022 17:30:39] |N3| List of colors: ['1c005c', '037d41', 'c8f41e', 'ae5f8a', '5176ff']
[14-10-2022 17:30:44] |N4| List of colors: ['cb1029', '5181dd', 'e421c1', 'd9d198', 'd13ad3']
[14-10-2022 17:30:49] |N5| List of colors: ['76c085', '5a7c58', '969ad9', '44d824', '75dbc8']



About Me:
- My GitHub Link: https://github.com/PAIREN1383
- Author: MohammadAli
###############################################""")
    elif choose == "1": # Color Injector
        # All inputs will be checked.
        log_writer("********** Color Injector launched. **********")
        nrepetitions = input("Enter number of repetitions (ex: '50'): ")
        correct_nrepetitions = check_nrepetitions(nrepetitions)
        log_writer(f"Number of repetitions: {nrepetitions}")

        cssfilepath = input("Enter path of CSS file: ")
        try:
            with open(cssfilepath, "r") as existfile:
                pass
        except:
            print("You have entered an invalid path! Please try again.")
            continue
        log_writer(f"Path of CSS file: {cssfilepath}")

        backup_name = input("Enter a name for a backup CSS file (to avoid potential problems): ").strip() + ".css"
        correct_backup_name = check_name(backup_name)
        log_writer(f"Backup name: '{correct_backup_name}'")

        choosemode = input("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \
            \nModes: \
            \n't1': Change color automatically every 5 seconds. \
            \n't2': Change color automatically every 10 seconds. \
            \n't3': Change color automatically every 15 seconds. \
            \n'tn': Change color automatically every (n*5; (0<n<10)) seconds. \
            \n'p': Press 'Enter' to change color. \
            \nEnter mode: ").strip()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        correct_mode = check_mode(choosemode)

        css_file_manager(cssfilepath, correct_backup_name, correct_nrepetitions, correct_mode)
        print(f"Your log file path: {file_dir() + 'Color_Injector_log_file.log'}")
    elif (choose == "2") or (choose.lower() == "e") or (choose.lower() == "q"): # Exit
        break
    else:
        print("You have entered an invalid value!")
