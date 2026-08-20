# Touch-ID
A 1 key macropad. Macbooks don't allow for touch ID on external keyboards, so I will make a 1 key macropad  that just types out my password. PCB will be made in KiCAD, code is VS code, and case in Fusion 360.

## Assembly:
Take the pcb and use the through hole components to solder the seeeduino and the switch
<br></br>
Use double sided tape (if wanted) to secure the pcb to the bottom case
<br></br>
Take the top part of the case and screw it in
<br></br>
Put the keycap on
<br></br>

## Flashing:
To flash the firmware, press the bott button and while holding it press the reset button
<br></br>
You should see a drive called RP1-RP2
<br></br>
Drag the uf2 file into the drive
<br></br>
Now you should see a drive called CIRCUITPY
<br></br>
Delete everything in there and replace it with everything in the code folder so it looks like this:
<img width="723" height="140" alt="Screenshot 2026-08-20 at 4 50 57 PM" src="https://github.com/user-attachments/assets/f9543655-7d8b-4031-8fe4-b8eadf1f626f" />

## Updating Code:
Update the code in the place where it says YOURPASSWORD, replace it with your actual password

## Images:
<img width="1244" height="914" alt="Screenshot 2026-08-20 at 4 15 45 PM" src="https://github.com/user-attachments/assets/febde1c3-9af6-4b2a-88c8-8a07fe4488c5" />
<img width="667" height="473" alt="Screenshot 2026-08-20 at 4 32 59 PM" src="https://github.com/user-attachments/assets/eb03d850-40e1-4d49-a3ee-557617bd18c1" />
