import os
from pathlib import PurePath

class Compiler:
    
    def __init__(self, folder_path):
        self.folder_path = os.path.realpath(folder_path)
        self.current_app = ""
        self.temp_used_packages = []

    def grab_new_app(self):
        for path, subdirs, files in os.walk(self.folder_path):
            for name in files:
                new_path = str(PurePath(path, name))
                if '.png' in new_path:
                    path_split = new_path.split('/')
                    for i in path_split:
                        if '.png' in i:
                            if i not in self.temp_used_packages:
                                self.current_app = i.replace('.png', '')
                                self.temp_used_packages.append(i)
                                return
    def set_icon(self):
        if os.path.exists('/System/Applications/{}.app'.format(self.current_app)):
            # print('bins/fileicon "/System/Applications/{}.app" "{}"'.format(self.current_app, os.path.realpath(self.folder_path + '/' + self.current_app + '.png')))
            os.system('bins/fileicon set "/System/Applications/{}.app" "{}"'.format(self.current_app, os.path.realpath(self.folder_path + '/' + self.current_app + '.png')))
        elif os.path.exists('/Applications/{}.app'.format(self.current_app)):
            os.system('bins/fileicon set "/Applications/{}.app" "{}"'.format(self.current_app, os.path.realpath(self.folder_path + '/' + self.current_app + '.png')))
        else:
            print('User Missing Application: %s' % self.current_app)

                        

    def file_count(self):
        path, dirs, files = next(os.walk(self.folder_path))
        new_files = []
        for i in files:
            if '.DS_Store' not in i:
                print('Found Application: %s' % i.replace('.png', ''))
                new_files.append(i)
        return len(new_files)