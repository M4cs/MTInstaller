# PyIcns
MacOS Theming Toolkit Using FileIcon

# Getting Started

**This program is still in active development. If you are reading this right now this software is still in pre-release.**

To start make sure you have Python 3.6+ installed and MacOS.

Clone this repository and run:
```
cd PyIcns
pip install -r requirements.txt
python3 setup.py
sudo python3 start.py
```

**You need to disable SIP on Pre-Catalina Versions. For Catalina you must root remount! Do so with this: `sudo mount -wu /`**

This should be pretty self-explainatory from there.

# Getting Started 4 Themers

Right now you should just include 1 512x512 png of whatever applications you want to theme. From there you will put them in any folder together and name them according to their application 1:1. Here is an example:

![Ex1](https://i.imgur.com/ZeHbaQR.png)

From here you simply package them in a zip or whatever and distrubte however you'd like. People will unzip and just enter the folder name containing all the icons. They will automatically map to installed applications and install.
