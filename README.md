# Color_Injector
To change colors more easily and find good color combinations for web pages.

![image from Color_Injector user interface](https://github.com/PAIREN1383/Color_Injector/blob/main/Color_Injector_img.PNG)
![image from Color_Injector user interface](https://github.com/PAIREN1383/Color_Injector/blob/main/Color_Injector_img2.PNG)


## Help Content:
### Why was this tool created?
To change colors more easily and find good color combinations for web pages. Don't worry about mistakes in inputs, all inputs will be checked.

### How can I use it?
- Step 1: Open the program.
- Step 2: Enter '1'.
- Step 3: Enter number of repetitions, like 80, then you can change colors for 80 times.
- Step 4: Enter path of CSS file for color injection.
- Step 5: Enter an appropriate name (without these characters: \/:*?"<>|) for the new backup file. You don't need to end the name with '.css'.
- Step 6: Enter mode. If you want to change colors every 10 seconds, enter 't2' (t1=5s, t2=10s, t3=15s, tn=n*5s). If you want to change colors with pressing 'Enter', enter 'p'.
- Step 8: Select lines for color injection like '8, 12, 21'or enter 'all' to select all lines or enter 'abc' to select all background-colors or enter 'ac' to select all colors.
- Step 7: Open HTML file on 'Live Server' (it is a 'VS Code' extension).
- Step 8: After selecting color, if you enter 'p' mode, enter 'e' or 'q' to stop injection or if you enter 't' mode, press 'Ctrl + C' to stop injection.
- Step 9: Enter 'q' or 'e' or '2' to exit the program.

### Where is the log file?
It will be saved in the program directory. Right here: E:\PYTHON.VSC\Color_Injector\

### What information will be in the log file?
Here is the test log:
```
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
```
