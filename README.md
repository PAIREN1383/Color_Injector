# Color_Injector
To change colors more easily and find good color combinations for web pages.

![image from Color_Injector user interface](https://github.com/PAIREN1383/Color_Injector/blob/main/Color_Injector_img.PNG)


## Help Content:
### Why was this tool created?
To change colors more easily and find good color combinations for web pages. Don't worry about mistakes in inputs, all inputs will be checked.

### How can I use it?
- Step 1: Open the program.
- Step 2: Enter '1'.
- Step 3: Enter '1' if you have a live server (it is a 'VS Code' extension) or enter '2' if you are running the application from terminal.
- Step 4: Enter path of CSS file for color injection.
- Step 5: Enter path of HTML file for color injection.
- Step 6: Enter an appropriate name (without these characters: \/:*?"<>|) for the new backup file. You don't need to end the name with '.css'.
- Step 7: Enter mode. If you want to change colors every 10 seconds, enter 't2' (t1=5s, t2=10s, t3=15s, tn=n*5s). If you want to change colors with pressing 'Enter', enter 'p'.
- Step 8: If everything is correct, enter 'y'.
- Step 9: Select lines for color injection like '8, 12, 21',
-- or enter 'all' to select all lines,
-- or enter 'abc' to select all background-colors,
-- or enter 'ac' to select all colors.
- Step 10: If you are entering live server mode, open the HTML file in Live Server.
- Step 11: After selecting color, if you enter 'p' mode, enter 'e' or 'q' to stop injection, or if you enter 't' mode, press 'Ctrl + Alt + Z' to stop injection.
- Step 12: Enter 'q' or 'e' or '2' to exit the program.


### Where is the log file?
It will be saved in the CSS file directory.

### What information will be in the log file?
Here is the test log:
```
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
```
### HINT
After using the program, clear the log file.

Don't forget to give a star. ;)
