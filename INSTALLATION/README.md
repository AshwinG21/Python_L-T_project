Here we must install raspberry pi software in a monitor by downloading raspbian OS and burning it to the SD card.

After initial configuration of RPi is done, the RPi board is connected to Wi-Fi. An IP address is programmed and setup is linked to the RPi. The video captured by the RPi camera is sent over the Wi-Fi modem. This video can be viewed in your smartphone by connecting to the same Wi-Fi connection and IP address of the RPi.

The RPi is powered up using a 5V, 10000mAh power bank (Xiaomi). Then an SD card with the Raspbian software is inserted into the slot provided in the RPi board. The board is connected to a monitor for further configuration. The RPi configuration tool in Raspbian allows you to easily enable features and change your specific settings like keyboard layout. The procedure for the initial setting up is as follows:

1. Access the Terminal window on the Mac (or equivalent on another machine)
2. Run wirelessly with a static IP for each SD card
3. Automatically startup
4. Set the time zone
5. Skip the GUI of the RPi


Then we must install apache web server. 

Apache is used in this project to configure RPi as server. Apache is a popular web server application that you can install on the RPi to allow it to serve web pages. Apache can serve HTML files over HTTP, and with additional modules it can serve dynamic web pages using scripting languages such as PHP. First install the Apache package by typing the following command in the Terminal:

# ***Sudo apt-get install apache2 -y***

By default, Apache puts a test HTML file in the web folder. This default web page is served when you browse http://192.168.1.98 from another computer on the network. Browse the default web page either on the RPi or from another computer on the network; you would see the default page. Next, install PHP5 by giving the following command in the Terminal:

# ***Sudo apt-get install php5***
