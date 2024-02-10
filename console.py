#!/usr/bin/python3
import cmd

"""
console module
"""


class HBNBCommand(cmd.Cmd):
    """
    AirBnB command interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit program
        """
        return (True)

    def do_EOF(self, arg):
        """
        Exit prgram when EOF (Ctrl+D) is encountered
        """
        print("")
        return (True)

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
