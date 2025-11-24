import cmd

class Hello(cmd.Cmd):
    def do_hello(self, arg):
        print(f"Hello, {arg}!")
    
    def do_exit(self, arg):
        print("Goodbye!")
        return True  # exit the prompt

if __name__ == '__main__':
    h = Hello()
    h.cmdloop()  # Starts the interactive command prompt
