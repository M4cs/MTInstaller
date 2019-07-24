from pyicns import Compiler, __changelog__, __version__
import os
import requests
import time
import progressbar
import webbrowser
import readline

readline.parse_and_bind("tab: complete")

menu = f"""\

     _____ ______   _________  ___     
    |\   _ \  _   \|\___   ___\\  \    
    \ \  \\\__\ \  \|___ \  \_\ \  \   
     \ \  \\|__| \  \   \ \  \ \ \  \  
      \ \  \    \ \  \   \ \  \ \ \  \ 
       \ \__\    \ \__\   \ \__\ \ \__\
        \|__|     \|__|    \|__|  \|__|
                                       

Welcome to MTInstaller!

Current Version: {__version__}

This is an easy to use manager for installing macOS themes. 
All you need to do is feed a folder with images in a hierarchy
depicted on the GitHub documentation. 

If you need a link simply type "github" and press enter.

This will open up a new tab with the github documentation!

If you have any questions please contact me on twitter:
@maxbridgIand <- that is an I yes. Not an L!

Type 'menu' to display this menu

1 or 'install'/ Install Theme Pkg

2 or 'download'/ Download Themes (Coming Soon)

3 or 'github'/ Documentation

4 or 'changelog'/ View Changelog

5 or 'exit'/ Exit
"""

def check_updoots():
  response = requests.get('https://raw.githubusercontent.com/M4cs/MTInstaller/master/version').text
  if response != __version__:
    print('Current Version: %s' % __version__)
    print('Most Recent Version: %s' % response)
    print('Would you like to update?')
    ans1 = input('[y\\n]').lower()
    if ans1 == "y":
      print('Did you clone this from GitHub?')
      ans2 = input('[y\\n]').lower()
      if ans2 == "y":
        print('Updating')
        os.system('git fetch && git pull')
      else:
        count = 3
        while count != 0:
          print('Please Download The Latest Release In ' + str(count) + '\r')
          time.sleep(1)
          count = count - 1
        webbrowser.open_new_tab('https://github.com/M4cs/MTInstaller/releases')
        exit()
    else:
      pass
  else:
    pass

def main():
  while True:
    answer = input(terminal).lower()
    if answer == "1" or answer == "install":
      while True:
        print('Would you like to edit a specific folder? [Y\\n]')
        folder_ans = input(terminal).lower()
        if folder_ans == "y":
          print('Please Enter The Folder Location or Type Cancel To Go Back:')
          to_be = input(terminal)
          if to_be.lower() == "cancel":
            break
          while True:
            if os.path.exists(os.path.realpath(to_be)):
              print('Please Enter The Folder Where Your Theme Is Located:')
              from_here = input(terminal)
              while True:
                if os.path.exists(os.path.realpath(from_here)):
                  print('Please Enter The Image File Name You Would Like To Use:')
                  image = input(terminal)
                  while True:
                    if os.path.exists(os.path.realpath(from_here.replace('/', '') + '/' + image)):
                      print('Theming Folder...')
                      print('bins/fileicon set "{}" "{}"'.format(to_be, os.path.realpath(from_here.replace('/', '') + '/')))
                      os.system('bins/fileicon set "{}" "{}"'.format(os.path.realpath(to_be), os.path.realpath(from_here.replace('/', '') + '/' + image)))
                      os.system('killall Dock && killall Finder')
                      break
                    else:
                      print('File Does Not Exist!')
                break
            else:
              print('File Does Not Exist!')
            break
        print('Please Enter A Folder Location Of Your Theme Bundle or Type Cancel To Go Back:')
        ans1 = input(terminal)
        if ans1.lower() == "cancel":
          print(menu)
          break
        if os.path.exists(ans1):
          comp = Compiler(ans1)
          file_count = comp.file_count()
          print('Found %s Icons For The Applications In This Folder. Is This Correct? [Y\\n]' % file_count)
          response = input(terminal).lower()
          if response == 'y':
            print('Setting Theme...')
            count = 0
            with progressbar.ProgressBar(max_value=file_count) as bar:
              while count <= file_count - 1:
                comp.grab_new_app()
                comp.set_icon()
                bar.update(1)
                count = count + 1
              os.system('killall Dock && killall Finder')
              break
          elif response == 'n':
            break
          else:
            print('Choose Y or N Only')
        else:
          print('Error! The File Does Not Exist!')
    elif answer[0:1] == "2" or answer == "download":
      print('\nComing Soon!\n')
    elif answer == "3" or answer[0:5] == "github":
      webbrowser.open_new_tab('https://github.com/M4cs/PyIcns')
    elif answer == "4" or answer == "changelog":
      print(__changelog__)
    elif answer == "5" or answer[0:4] == "exit":
      break
    elif answer == "menu":
      print(menu)
    else:
      print('Unknown Option!')

terminal = "pyicns$ "

if __name__ == "__main__":
  os.system('clear')
  print('Checking For Updates...')
  check_updoots()
  print('Up To Date!')
  print(menu)
  main()
  exit()
