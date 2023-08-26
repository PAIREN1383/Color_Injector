from random import randint
from datetime import datetime
from time import sleep
from webbrowser import open_new_tab
from keyboard import add_hotkey, remove_hotkey


def color_generator(n_colors):  # Generate palette of colors.
    while True:  # Repeat several times.
        colors_list = []
        while len(colors_list) != n_colors:  # How many colors are required?
            color = ""
            for char in range(6):  # Hex color code has 6 characters.
                color += f"{randint(0, 15):x}"
            if color not in colors_list:
                colors_list.append(color)
        yield colors_list


# Get the file directory to save the log file and backup file.
def file_dir(full_path):
    indx = full_path[-1::-1].find("\\")
    fdir = full_path[0:1].upper() + full_path[1:-indx]
    return fdir


# Check function 1
def check_live_direct(live_direct_input):
    if live_direct_input == "1":
        return "1"
    else:
        return "2"


# Check function 2
def check_name(fil_name):
    if "/" in fil_name or "\\" in fil_name or "<" in fil_name \
        or ">" in fil_name or "?" in fil_name or "|" in fil_name \
            or "*" in fil_name or ":" in fil_name or '"' in fil_name:
        return "Ibackup.css"
    if fil_name == ".css":
        return "Ibackup.css"
    return fil_name


# Check function 3
def check_mode(mode):
    if mode == "":
        return "p"
    elif (mode.lower()[0] == "t") and (mode[1].isdigit()) and (len(mode) == 2) and (int(mode[1]) >= 1):
        return mode.lower()
    else:
        return "p"


def log_writer(log):
    global cf_path
    with open(cf_path + "Color_Injector_log_file.log", "a") as logfile:
        logfile.write(
            f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {log}\n")


def br_loop():
    global break_loop
    break_loop = True


# Detecting the exact lines from the CSS file to inject color codes.
def search_into_css_file(all_lines_of_file):
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
    global cf_path
    with open(cf_path + backup_fname, "a") as bfile:
        bfile.writelines(all_lines_for_backup)
        log_writer(
            f"A backup of the CSS file has been created. Path: {cf_path + backup_fname}")


def user_choices():  # Getting user choices list.
    global choices_list
    while True:
        choices_list = input(
            "Enter the number of lines to inject color and split them with ',' (ex: 'all' or 'abc' or 'ac' or '23, 36, 39'): ").strip().split(",")
        if choices_list[0].lower() == "all":
            choices_list = list(map(lambda x: (x+1), all_indexes_list))
        elif choices_list[0].lower() == "abc":
            choices_list = list(map(lambda x: (x+1), background_index_list))
        elif choices_list[0].lower() == "ac":
            choices_list = list(map(lambda x: (x+1), color_index_list))
        else:
            try:
                choices_list = list(
                    map(lambda x: int(x.strip()), choices_list))
            except:
                print(
                    "You have entered an invalid value! Please try again or enter '0' to cancel.")
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
            print(
                "You have entered an invalid value! Please try again or enter '0' to cancel.")


# Main function
def css_file_manager(css_file_path, html_file_path, backup_file_name, injection_mode, live_direct_mode):
    global break_loop

    with open(css_file_path, "r") as cfile:
        all_lines = cfile.readlines()

    # Preparing for color injection.
    getting_backup(all_lines, backup_file_name)
    search_into_css_file(all_lines)
    user_choices()

    # Cancel color injection.
    if choices_list == [0]:
        return

    if len(injection_mode) == 2:
        sleep_time = int(injection_mode[1]) * 5
        print(f"***************************************** \
            \nAmount of sleep: {sleep_time}s \
            \n*****************************************")

    counter = 1
    break_loop = False
    add_hotkey("ctrl+alt+z", br_loop)  # Breaker of loop in tn mode
    for clr_list in color_generator(len(choices_list)):
        log_writer(f"|N{counter}| List of colors: {clr_list}")
        clr_indx = 0
        for num in choices_list:
            if (num-1) in background_index_list:
                all_lines.insert(
                    (num-1), f"    background-color: #{clr_list[clr_indx]};\n")
                all_lines.pop(num)
            elif (num-1) in color_index_list:
                all_lines.insert(
                    (num-1), f"    color: #{clr_list[clr_indx]};\n")
                all_lines.pop(num)
            clr_indx += 1
        with open(css_file_path, "w") as cfile:
            cfile.writelines(all_lines)
        if injection_mode == "p":
            if live_direct_mode == "2":
                open_new_tab("file:///" + htmlfilepath.replace(" ", "%20"))
            stopinjection = input(
                f"[List number: {counter}] Press 'Enter' for changing color or enter 'e' or 'q' to exit: ").strip()
            if (stopinjection.lower() == "e") or (stopinjection.lower() == "q"):
                break
        else:
            print(
                f"[List number: {counter}] If you want to stop the injection, press 'Ctrl + Alt + Z'.")
            if live_direct_mode == "2":
                open_new_tab("file:///" + html_file_path.replace(" ", "%20"))

            # Check breaker
            for i in range(sleep_time):
                sleep(1)
                if break_loop == True:
                    break
            if break_loop == True:
                break

            if counter % 10 == 0:
                wait_for_user = input(
                    f"You change the color(s) {counter} time(s). press 'Enter' to continue or enter 'q' or 'e' to exit: ").strip()
                if (wait_for_user.lower() == "e") or (wait_for_user.lower() == "q"):
                    break
        counter += 1
    remove_hotkey("ctrl+alt+z")


while True:
    print("-----------------------------------------------\
    \nWelcome to Color Injector program. \
    \n[0] Help \
    \n[1] Color Injector \
    \n[2] Exit \
    \n-----------------------------------------------")
    choose = input("Enter your choice: ").strip()
    print("-----------------------------------------------")
    if choose == "0":  # Help
        print(f"""###############################################
Help Content:
- Why was this tool created? 
--- To change colors more easily and find good color combinations for web pages.
---\ Don't worry about mistakes in inputs, all inputs will be checked.

- How can I use it?
--- Step 1: Open the program.
--- Step 2: Enter '1'.
--- Step 3: Enter '1' if you have a live server (it is a 'VS Code' extension) or 
---\ enter '2' if you are running the application from terminal.
--- Step 4: Enter path of CSS file for color injection.
--- Step 5: Enter path of HTML file for color injection.
--- Step 6: Enter an appropriate name (without these characters: \/:*?"<>|) for the new backup file.
---\ You don't need to end the name with '.css'.
--- Step 7: Enter mode. If you want to change colors every 10 seconds, enter 't2' (t1=5s, t2=10s, t3=15s, tn=n*5s).
---\ If you want to change colors with pressing 'Enter', enter 'p'.
--- Step 8: If everything is correct, enter 'y'.
--- Step 9: Select lines for color injection like '8, 12, 21',
---\ or enter 'all' to select all lines,
---\ or enter 'abc' to select all background-colors,
---\ or enter 'ac' to select all colors.
--- Step 10: If you are entering live server mode, open the HTML file in Live Server.
--- Step 11: After selecting color, if you enter 'p' mode, enter 'e' or 'q' to stop injection,
---\ or if you enter 't' mode, press 'Ctrl + Alt + Z' to stop injection.
--- Step 12: Enter 'q' or 'e' or '2' to exit the program.

- Where is the log file?
--- It will be saved in the CSS file directory.

- What information will be in the log file?
--- Here is the test log:
**** Color Injector launched. **********
[31-07-2023 17:22:21] Path of CSS file: F:\python projects\Mini-Project-Menu1\Menu1\Menu1.css
[31-07-2023 17:22:29] Backup name: 'mytest.css'
[31-07-2023 17:22:39] A backup of the CSS file has been created. Path: F:\python projects\Mini-Project-Menu1\Menu1\mytest.css
[31-07-2023 17:22:47] Selected lines: [16, 26, 71, 81]
[31-07-2023 17:22:47] |N1| List of colors: ['6e602c', 'ae8096', '018e9d', '3083cd']
[31-07-2023 17:22:50] |N2| List of colors: ['e449bd', '774f10', 'cd0c90', '4c109b']
[31-07-2023 17:22:50] |N3| List of colors: ['cf72d7', 'e61b57', 'fd88d6', 'b6170e']
[31-07-2023 17:22:51] |N4| List of colors: ['c36e48', '31cb16', 'fd5799', '411e25']
[31-07-2023 17:22:51] |N5| List of colors: ['b9fd74', 'deb908', 'b567ea', '6b45e4']

About Me:
- My GitHub Link: https://github.com/PAIREN1383
- Author: MohammadAli
###############################################""")
    elif choose == "1":  # Color Injector
        # All inputs will be checked.
        live_direct = input("[1] I use VS Code live server \
                            \n[2] I use terminal \
                            \nEnter usage mode: ").strip()
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        correct_live_direct = check_live_direct(live_direct)
        cssfilepath = input("Enter path of CSS file: ").strip()
        htmlfilepath = input("Enter path of HTML file: ").strip()
        try:
            with open(cssfilepath, "r") as existfile:
                pass
            with open(htmlfilepath, "r") as existfile:
                pass
        except:
            print("You have entered an invalid path! Please try again.")
            continue
        cf_path = file_dir(cssfilepath)

        backup_name = input(
            "Enter a name for a backup of CSS file (to prevent potential problems): ").strip() + ".css"
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

        ok = input(f"Your choices: \
                \nUsage mode: {correct_live_direct} \
                \nCSS file path: {cssfilepath} \
                \nHTML file path: {htmlfilepath} \
                \nBackup file name: {correct_backup_name} \
                \nMode: {correct_mode} \
                \nEvery thing is ok? y/n: ").strip()
        if (ok.lower() == "y") or (ok.lower() == "yes"):
            print(
                "============================== The program started ==============================")
        else:
            continue

        log_writer("********** Color Injector launched. **********")
        log_writer(f"Path of CSS file: {cssfilepath}")

        css_file_manager(cssfilepath, htmlfilepath, correct_backup_name, correct_mode, correct_live_direct)
        print(f"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \
            \nYour log file path: {cf_path + 'Color_Injector_log_file.log'}")
    elif (choose == "2") or (choose.lower() == "e") or (choose.lower() == "q"):  # Exit
        break
    else:
        print("You have entered an invalid value!")
