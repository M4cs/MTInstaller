# MTInstaller
MacOS Theming Toolkit

# Getting Started

You might as well go through [Help](https://github.com/M4cs/PyIcns/blob/master/README.md#help) and follow those steps as well.

Head to the [Releases Page](https://github.com/M4cs/MTInstaller/releases) and get yourself the most recent release of `mti-cli-gui` and `mti-cli`. These two packages will allow

# Getting Started From Source

**This program is still in active development. If you are reading this right now this software is still in pre-release.**

To start make sure you have Python 3.6+ installed and MacOS.

You might as well go through [Help](https://github.com/M4cs/PyIcns/blob/master/README.md#help) and follow those steps as well.

Clone this repository into /System and run:
```
cd PyIcns
pip install -r requirements.txt
sudo python3 setup.py
sudo python3 start.py
```

If you can't write to system refer to [Help](https://github.com/M4cs/PyIcns/blob/master/README.md#help).

This should be pretty self-explainatory from there.

# Getting Started 4 Themers

Right now you should just include 1 512x512 png of whatever applications you want to theme. From there you will put them in any folder together and name them according to their application 1:1. Here is an example:

![Ex1](https://i.imgur.com/ZeHbaQR.png)

From here you simply package them in a zip or whatever and distrubte however you'd like. People will unzip and just enter the folder name containing all the icons. They will automatically map to installed applications and install.

# Help

If you can't write to root or are on Catalina you may have to follow the steps below.

**You need to disable SIP on Post-Cap Versions.**

1. First run `sudo mount -uw /`. Even if it errors that's fine.

2. Run `mount -uw /System/Volumes/Data`. Even if it errors that's fine.

3. Run `cd /System && mkdir AppleInternal`

4. You can also add `AppleInternal` to root.

# Credit

Shoutout to the dev behind FileIcon this tool makes this whole toolkit possible!

https://github.com/mklement0/fileicon
