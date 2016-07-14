# arduino-nano-ir-remote

This project is about infrared remote control with aruino (atmega328p). I don't use arduino library but standard avr libs with aruino bootloader only (i prefer that). 

C code is a copy from book "Język C dla mikrokontrolerów AVR" ("C language for AVR microcontrollers") by Tomasz Francuz. Python part is made by me. 
In order to control Linux system with remote control with Python code xdotol application is required:

sudo apt-get install xdotol.

Refer to man xdotol for reference.

Simplified connection diagram is attached in the project as diagram.jpg.
Infrared sensor is TSOP1736 and some random remote control I have from PC DVBT tuner (any other should work but detection of key codes is necessary)

http://dalincom.ru/datasheet/TSOP1736.pdf


