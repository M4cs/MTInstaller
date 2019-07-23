from pyicns import compiler
import os
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

This is an easy to use manager for installing and compiling
macOS themes. All you need to do is feed a folder with images
in a hierarchy depicted on the GitHub documentation. If you need
a link simply type "github" and press enter. This will open up
a new tab with the github documentation!

If you have any questions please contact me on twitter:
@maxbridgIand <- that is an I yes. Not an L!

1/ Install Theme Pkg

2/ Download Themes (Coming Soon)

3/ Documentation

4/ Exit
"""


terminal = "pyicns$ "
print(menu)
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
  elif answer == "3":
    webbrowser.open_new_tab('https://github.com/M4cs/PyIcns/')
  elif answer == "2":
    print('\nComing Soon!\n')
  elif answer == "4" or "exit":
    os._exit(0)
  main()
try:
  main()
except KeyboardInterrupt:
  print('\nGoodbye!')

