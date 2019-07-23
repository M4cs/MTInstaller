from pyicns import compiler
import os
import requests
import time
import progressbar
import webbrowser

menu = """\

   ▄███████▄ ▄██   ▄    ▄█   ▄████████ ███▄▄▄▄      ▄████████ 
  ███    ███ ███   ██▄ ███  ███    ███ ███▀▀▀██▄   ███    ███ 
  ███    ███ ███▄▄▄███ ███▌ ███    █▀  ███   ███   ███    █▀  
  ███    ███ ▀▀▀▀▀▀███ ███▌ ███        ███   ███   ███        
▀█████████▀  ▄██   ███ ███▌ ███        ███   ███ ▀███████████ 
  ███        ███   ███ ███  ███    █▄  ███   ███          ███ 
  ███        ███   ███ ███  ███    ███ ███   ███    ▄█    ███ 
 ▄████▀       ▀█████▀  █▀   ████████▀   ▀█   █▀   ▄████████▀  
                                                              

Welcome to Pyicns!

This is an easy to use manager for installing macOS themes. 
All you need to do is feed a folder with images in a hierarchy
depicted on the GitHub documentation. 

If you need a link simply type "github" and press enter.

This will open up a new tab with the github documentation!

If you have any questions please contact me on twitter:
@maxbridgIand <- that is an I yes. Not an L!

1/ Install Theme Pkg

2/ Download Themes (Coming Soon)

3/ Documentation

4/ Exit
"""

__version__ = "1.0.1"

def check_updoots():
  response = requests.get('https://raw.githubusercontent.com/M4cs/PyIcns/master/version').text
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
          print('Please Clone From The Browser Opening In ' + str(count) + '\r')
          time.sleep(1)
          count = count - 1
        webbrowser.open_new_tab('https://github.com/M4cs/PyIcns')
        exit()
    else:
      pass
  else:
    pass

terminal = "pyicns$ "
def main():
  answer = input(terminal).lower()
  if answer == "1":
    while True:
      print('Please Enter A Folder Location Of Your Theme Bundle:')
      ans1 = input(terminal)
      if os.path.exists(ans1):
        comp = compiler.Compiler(ans1)
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
            break
      else:
        print('Error! The File Does Not Exist!')
    main()
  elif answer[0:1] == "2":
    print('\nComing Soon!\n')
    main()
  elif answer[0:1] == "3" or answer[0:5] == "github":
    webbrowser.open_new_tab('https://github.com/M4cs/PyIcns')
    main()
  elif answer[0:1] == "4" or answer[0:4] == "exit":
    exit()
  else:
    print('Unknown Option!')
    main()

if __name__ == "__main__":
  check_updoots()
  print(menu)
  main()