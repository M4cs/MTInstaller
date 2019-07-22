import os, requests

os.system('mkdir bins')
res = requests.get('https://raw.githubusercontent.com/mklement0/fileicon/stable/bin/fileicon').text
with open('bins/fileicon', 'w') as filecon:
    filecon.write(res)
    filecon.close()
os.system('chmod +x bins/fileicon')