from os import path, listdir, mkdir, walk
from shutil import rmtree, move
from sys import exit

class Classifier:
    def __init__(self, abs_path, dest_path, traverse=False):
        self.abs_path = abs_path
        self.dest_path = dest_path
        self.traverse = traverse

        if not path.isdir(self.abs_path) or not path.exists(self.abs_path):
            print('Invalid absolute path. Check it again')
            exit()
        if not path.isdir(self.dest_path) or not path.exists(self.dest_path):
            print('Invalid destination path. Check it again')
            exit()
                
        if self.traverse:
            for curr_path, _, files in walk(self.abs_path, topdown=True):
                self.__run(files, curr_path)
        else:
            self.__run(listdir(self.abs_path), self.abs_path)
            
        rmtree(self.abs_path)

    def __run(self, files, curr_path):
        for file in files:
            _, ext = path.splitext(file)
            dest_path = None

            if ext:
                dest_path = self.dest_path + "\\" + ext[1:].upper() + " Files"
            else:
                dest_path = self.dest_path + "\\Unknown Files"

            if not path.exists(dest_path):
                mkdir(dest_path)

            source = path.join(curr_path, file)
            destination = path.join(dest_path, file)

            move(source, destination)

abs_path = input('Enter the absolute path of the directory to be scanned: ').strip()
dest_path = input('Enter the destination path to put classified files: ').strip()
should_traverse = True if input('Do you want to traverse within every subdirectory (Y/N): ').strip().upper() == "Y" else False

Classifier(abs_path, dest_path, should_traverse)
