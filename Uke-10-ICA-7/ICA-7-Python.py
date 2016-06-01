# Developer: Manish Raj (technoslab@gmail.com)
import shelve, time, sys

class File(object):

    # En typ constructor for class "File". 
    def __init__(self, name, type, parent=None, text=''):
        self.list = []
        self.name = name
        self.type = type
        self.time = int(time.time())
        self.parent = parent
        self.text = text


    # Metode for å sjekke om filen du søker etter eksisterer, returnerer true eller false.
    def is_file(self, name):
        for node in self.list:
            if node.name == name:
                return True
        return False

    # Metode for å sjekke om mappen du søker etter eksisterer, returnerer true eller false.
    def is_dir(self, name):
        if(self.is_file(name)) and self.get(name).type == 'dir':
            return True
        return False

    # Metode for å hente/finne en fil eller mappe. Returnerer funnet element
    def get(self, name):
        for node in self.list:
            if node.name == name:
                return node

    # Metode for å legge til en fil
    def add(self, name, type, text=''):
        self.list.append(File(name, type, self, text))

    # Metode for å slette en fil 
    def remove(self, name):
        self.list.remove(self.get(name))

    # Metode for gi et nytt navn til en fil
    def rename(self, name):
        self.name = name

    # Metode for kopiering av filer
    def copy(self, src, dest):
        src = self.get(src)
        self.add(dest, src.type, src.text)

    # For å liste opp f
    def stat(self):
        print 'Listing', self.name
        for node in self.list:
            print 'Name:', node.name, '; Created:', node.time, '; Type:', node.type

    # Metode for å lese en fil, printe ut filen 
    def read(self):
        print 'Reading file:', self.name
        print self.text

class FileSystem(object):

    # Dette er kommandoer som kan brukes.
    COMMANDS = ['ls', 'mkdir', 'chdir', 'cd', 'rmdir', 'create', 'read', 'rm', 'mv', 'cp', 'help', 'exit']

    # Start for klassen FileSystem
    def __init__(self):
        self.io = shelve.open('file.sys', writeback=True)
        if self.io.has_key('fs'):
            self.root = self.io['fs']
        else:
            self.root = File('/', 'dir')
        self.curr = self.root

    # Lager en ny directory, sjekker at navnet ikke er brukt fra før. dersom navnet er ledig blir det navnet på directoryen. 
    def mkdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'mkdir - make directory'
            print 'usage: mkdir <dir_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name) == False:
                self.curr.add(name, 'dir')
            else:
                print name, ' - already exists.'

    # Velger en ny directory for filen du er på.
    def chdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'chdir - change directory.'
            print 'usage: chdir <dir_name>'
        else:
            name = cmd[1]
            if name == '..':
                if self.curr.parent is not None:
                    self.curr = self.curr.parent
            elif self.curr.is_dir(name):
                self.curr = self.curr.get(name)
            else:
                print name, ' - invalid directory.'

    # Sletter et directory. 
    def rmdir(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'rmdir - remove directory'
            print 'usage: rmdir <dir_name>'
        else:
            name = cmd[1]
            if self.curr.is_dir(name):
                self.curr.remove(name)
                print 'Directory deleted.'
            else:
                print name, ' - invalid directory.'

    # Sletter en fil. 
    def rm(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'rm - remove file'
            print 'usage: rm <file_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name) and not self.curr.is_dir(name):
                self.curr.remove(name)
                print 'File deleted.'
            else:
                print name, ' - invalid file.'

    # Lister alle filer og Dir i en mappe (dir) 
    def ls(self, cmd):
        if(len(cmd) > 1):
            print 'ls - list stats'
            print 'usage: ls'
        self.curr.stat()

    # Lager en ny fil, legger til tekst i filen. 
    def create(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'create - create a file'
            print 'usage: create <file_name>'
        else:
            name = cmd[1]
            self.curr.add(name, 'file', raw_input('Enter file context: '))

    # Leser innholdet i en fil. 
    def read(self, cmd):
        if len(cmd) < 2 or cmd[1] == '':
            print 'read - read a file'
            print 'usage: read <file_name>'
        else:
            name = cmd[1]
            if self.curr.is_file(name):
                self.curr.get(name).read()
            else:
                print name, 'invalid file'
    
    # Bytter navn på en eksisterende fil 
    def mv(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            print 'mv - rename a file'
            print 'usage: mv <old_name> <new_name>'
        else:
            old_name = cmd[1]
            new_name = cmd[2]
            if self.curr.is_file(old_name):
                self.curr.get(old_name).rename(new_name)
            else:
                print old_name, 'invalid file'

    # kopierer en fil. 
    def cp(self, cmd):
        if len(cmd) < 3 or cmd[1] == '':
            print 'cp - copy a file'
            print 'usage: cp <src> <dest>'
        else:
            src = cmd[1]
            dest = cmd[2]
            if self.curr.is_file(src):
                self.curr.copy(src, dest)
            else:
                print src, 'invalid file'
    # Brukes i "Main". Lagrer alt når du exiter. 
    def save(self):
        self.io['fs'] = self.root
        self.io.sync()

    # Skriver ut mulige kommandoer.        
    def help(self, cmd):
        print 'COMMANDS: mkdir, ls, chdir, rmdir, create, read, mv, cp, rm, exit'

    def exit(self, cmd):
        sys.exit(0)

# Start av FileSystem og hovedloop for input og kommandoer til filsystemet.
#Inneholder også exit og save funksjonen. 
def main():
    fs = FileSystem()
    while True:
        cmd = raw_input('> ').split(' ');
        method = None
        try:
            method = getattr(fs, cmd[0])
        except AttributeError:
            print 'Invalid command. Type "help".'
        if method is not None and cmd[0] in FileSystem.COMMANDS and callable(method):
            method(cmd)
            fs.save()
        else:
            print 'Invalid command. Type "help".'
main()