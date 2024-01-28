from os import path, listdir, mkdir, walk
from platform import system
import shutil
import sys

class FileClassifier:
    def __init__(self, abs_path, des_path, enter_sub):
        self.abs_path = abs_path
        self.enter_sub = enter_sub.upper()
        self.os = system()
        self.rootdir = None
        
        if des_path != '':
            self.rootdir = des_path
            self.__run()
        else:
            self.__wrapper()

    def __wrapper(self):
        if self.os == 'Windows':
            self.rootdir = 'C:\\Categorization\\'
        elif self.os == 'Darwin':
            # Mac root directroy
            print('Does not support Mac yet')
            sys.exit()
        else:
            # Linux root directroy
            print('Does not support Linux yet')
            sys.exit()

        self.__run()

    def __creator(self):
        if path.isdir(self.abs_path) and path.exists(self.abs_path):
            if len(listdir(self.abs_path)) != 0:
                if path.isdir(self.rootdir):
                    if not path.exists(self.rootdir):
                        mkdir(self.rootdir)

                    self.__walk_or_not()
                else:
                    raise Exception('Please enter a valid directroy!')
            else:
                raise Exception('Target directory is empty!')
        else:
            raise Exception('Check the path again!')

    def __walk_or_not(self):
        if self.enter_sub == 'Y':
            for current_path, _, files in walk(self.abs_path, topdown=True):
                self.__categorizer(files, current_path)
        elif self.enter_sub == 'N' or self.enter_sub == '':
            self.__categorizer(listdir(self.abs_path), None)
        else:
            raise SyntaxError('Please enter valid char or nothing!')

        shutil.rmtree(self.abs_path)
        print('\nAll files classified')
        sys.exit()

    def __categorizer(self, data_list, current_path):
        for data in data_list:
            _, tail = path.splitext(data)
            if tail != '':
                my_path = self.rootdir + tail[1:].upper() + ' Files'
            else:
                my_path = self.rootdir + 'Unknown Files'

            if not path.exists(my_path):
                mkdir(my_path)

            self.__transporter(data, my_path, current_path)

    def __transporter(self, source, destination, current_path):
        adj_source = path.join(
            self.abs_path if current_path is None else current_path, source)
        adj_destination = path.join(destination, source)

        shutil.move(adj_source, adj_destination)

    def __run(self):
        self.__creator()

path_inp = input('Enter a absolute path of directroy: ').strip(' ')
dest_path = input('Enter the destination path of new directory: (Default root directory) ').strip(' ')
walk_inp = input('Enter to every subdirectory: (Y/N) (Default N) ').strip(' ')

FileClassifier(path_inp, dest_path, walk_inp)
