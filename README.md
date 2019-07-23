# PyIcns
MacOS Theming Toolkit Using FileIcon

# Getting Started

**This program is still in active development. If you are reading this right now this software is still in pre-release.**

To start make sure you have Python 3.6+ installed and MacOS.

**You need to disable SIP on Pre-Catalina Versions.**

1. Shut down your Mac

2. Boot into the Recovery Mode

3. When shut, start pressing CMD + R and while still pressing power up your machine and keep pressing the button combination until the Apple logo appears so that your Mac boots into the Recovery Mode.

4. Click Utilites and choose Terminal

5. Type diskutil list and identify the id of your disk named Macintosh HD
it should be something like `/dev/disk2s2`

6. Now we need to mount it: type `diskutil mount /dev/[YOUR_DISK_ID]`. If successful, keep going with the next step. If not, you probably got a message regarding APFS that the disk needs to be unlocked, so type `diskutil apfs unlockVolume /dev/[YOUR_DISK_ID]`

7. Finally you can create the required folder to enable writing: type `mkdir /Volumes/Macintosh\ HD/AppleInternal $$ mkdir /AppleInternal`

**For Catalina you must root remount! Do so with this: `sudo mount -wu /`**


Clone this repository and run:
```
cd PyIcns
pip install -r requirements.txt
python3 setup.py
sudo python3 start.py
```

This should be pretty self-explainatory from there.

# Getting Started 4 Themers

Right now you should just include 1 512x512 png of whatever applications you want to theme. From there you will put them in any folder together and name them according to their application 1:1. Here is an example:

![Ex1](https://i.imgur.com/ZeHbaQR.png)

From here you simply package them in a zip or whatever and distrubte however you'd like. People will unzip and just enter the folder name containing all the icons. They will automatically map to installed applications and install.

# Credit

Shoutout to the dev behind FileIcon this tool makes this whole toolkit possible!

https://github.com/mklement0/fileicon
