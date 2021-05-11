## How to do the set up for Adafruit Circuit Playground Express (CPX) Simulator


The official set up documentation can be visited in their official
[website](https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress)

______

### Installations (see installations.md)
 
- Install python 3.7+ or check that you are using this version or up of python. 
  [warning tip]: If you have installed `python2` in your system make sure it
  is not active as your default `python` command.

- Install Visual Studio Code. 

- Install the Device Simulator Express (Extension from the marketplace).
  Once it is installed, you will need to reload VScode. 

In some cases it is necessary to close it and open again (sometimes a couple of times).
______

### Set up:

- Click on the green button **Install** for Device Simulator Express, 
  after that it will pop-up a message asking if you want to open
  Visual Studio code. 

- *Click* **Open Visual Studio Code** 


<img align="middle" width="600px" src="images/vs_1.png" >

- Click on the button **Open Visual Studio Code**,
  your VSCode should be opened automatically.

At that point, a screen will appear with the Device Simulator Express Installation. 

- *Click* **Install**

<img  align="middle" width="600px" src="images/vs_2.png" >

If all goes OK, you would be able to don´t see any special screen. 

Go to :

  - `View` > `Command Palette` 
  - or use for Mac `cmd + shift + p` or for Windows/Linux `cntl + shift + p`

<img  align="middle" width="600px" src="images/vs_3.png" >


After *click* **Device Simulator Express**, you will need to wait some seconds
until three options of simulators appear. 

- In our case will work with "CircuitPlayground Express". 
If nothing happens wait a bit more, after a while retry to click again,
if not go to the "problems section".


[Extra info]On these images the purple arrows are indicating different python working version. 

Once the different options of simulators appear, we will select the
CircuitPlayground Express and the simulator will appear.

<img  align="middle" width="600px"  src="images/vs_5.png" >

In this case, it was running `python 3.9.1`, and since that fulfil the
rule of `python 3.7+` it will work good. 
After all these steps, we will arrive to the final screen divided in two. 
On the left, we have some information about a tutorial from the official
documentation about CircuitPython and the coding area.
On the right, on top we should see a microcontroller (CPX) image.

<img  align="middle" width="600px"  src="images/vs_6.png" >


## Possible problems and how to solve them:

The first arrow shows that `python2` is running, while on the bottom
it looks like it is `python 3.7+`.
Since the running version was `python2.7` it was not working. 

<img  align="middle" width="600px"  src="images/vs_4.png" >