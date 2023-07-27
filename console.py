 #!/usr/bin/python3
"""the console module"""
import cmd
class HBNBCommand(cmd.Cmd):
    prompt="(hbnb)"
    def do_quit(self,arg):
        """Exit the command interpreter"""
        return True
    def do_EOF(self,arg):
        """Exit the Command interpreter"""
        return True
    def emptyline(self):
        """when empty line, do nthg"""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()