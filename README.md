# MTInstaller
MacOS Theming Toolkit

# Getting Started

**If you are on a version above El Capitan you MUST disable SIP. Do so by entering Recovery Mode. Heading to `Utilities > Terminal` and running `csrutil disable`.**

Start by running:
```
curl -o- https://macthemes.co/mti-setup.sh | bash +x
```

This will install the `easy_mount` command to your system along with necessary things for MTInstaller to work. Next you will need to run `sudo easy_mount`. This will remount your system for the current uptime. **You need to run `easy_mount` after every reboot if you want to change the theme again. Themes DO persist through reboots however**.



# Credit

Shoutout to the dev behind FileIcon this tool makes this whole toolkit possible!

https://github.com/mklement0/fileicon
