# SIP
###### **S**ustainable **I**rrigation **P**latform

SIP is a free Raspberry Pi based Python program for controlling irrigation systems ( sprinkler, drip, hydroponic, etc ). It uses web technology to provide an intuitive user interface (UI) in several languages. The UI can be accessed in your favorite browser on desktop, laptop, and mobile devices.
SIP has also been used to control pumps, lights, and other Irrigation related equipment.

The core program is very versatile and there is a growing number of available plugins for added functionality.

### Software support:
Starting with version 5, SIP runs under Python 3. Python 2.x support has been removed.\
Most of the required Python packages and modules such as web.py and Cheroot are included in SIP's GitHub repository.\
Installing SIP by cloning from GitHub enables easy upgrades via `git pull` on the command line or by using the included `System_Update` plugin.

To install, simply clone SIP into the /home/pi/ directory of your Raspberry Pi:\
`sudo git clone https://github.com/Dan-in-CA/SIP.git`\
Or use the install script described in the [documentation  wiki](https://github.com/Dan-in-CA/SIP/wiki/install_info).  

If you are running Raspberry Pi OS Lite you may need to install git first with:\
`sudo apt-get install git`.\
For complete setup and usage instructions see the SIP [documentation  wiki](https://github.com/Dan-in-CA/SIP/wiki).

### Hardware support:
SIP is developed and tested on [Raspberry Pi](https://www.raspberrypi.org/products) although there is limited support for Beagle Bone Black and Odroid-C2. It has been tested on most Raspberry Pi models including Pi Zero.

There are a number of options for connecting SIP to an irrigation system including [relay boards](https://www.sainsmart.com/products/8-channel-5v-relay-module) and [hats](https://www.seeedstudio.com/DockerPi-4-Channel-Relay-p-4096.html) connected directly to the Pi's GPIO pins as well as OpenSprinkler boards and a simple DIY [interface](https://github.com/Dan-in-CA/sip/wiki/Relay-interface) that can support a large number of stations while using only 4 GPIO pins.

### Communication with other systems
- SIP can be controlled and monitored using HTTP GET commands.
- With the addition of available plugins SIP can communicate with other systems via MQTT.
- there is a Node-RED plugin included with SIP that allows Node-RED flows to control SIP and receive status information from SIP.   
- SIP can also issue Linux shell commands when a station is turned on or off. This is useful for controlling wireless remote devices and for I2C relay hats and [boards](https://www.tindie.com/products/jap/8-channel-relay-board-for-raspberry-pi-and-arduino/).
- There is also a mobile_app plugin shipped with SIP that transmits and receives SIP settings and status information in json format.
- The [Blinker](https://pythonhosted.org/blinker/) package that is shipped with SIP sends messages to other Python modules such as plugins to report changes in status. See the signaling_examples.py file in SIP's plugins folder for examples.

### Get involved
The motivation for developing SIP is to enable a very low cost yet sophisticated solution for the efficient use of irrigation water, an increasingly scarce resource world wide.

SIP has been greatly improved by contributions, large and small, from the user community.\
For example all the UI language translations have been contributed by users. If you would like to contribute a language translation or update an existing one please see the [translation instructions](https://github.com/Dan-in-CA/SIP/wiki/Translation-doc) on the wiki. It is rather easy.

To report a bug or contribute to the SIP project open an issue or pull request.

To ask question, make suggestions and learn more about SIP please see the **Discussions** tab in this repository or visit the
 [SIP Forum](http://nosack.com/sipforum/index.php)

-----------------------------------------------------------------

GNU GPL License
