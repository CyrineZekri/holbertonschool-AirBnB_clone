 #!/usr/bin/python3
"""the console module"""
import cmd
class HBNBCommand(cmd.Cmd):
    """Class of HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exiting the file"""
        return True

    def do_EOF(self, arg):
        """Exiting the file"""
        return True

    def emptyline(self):
        """When empty line, do nthg"""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()