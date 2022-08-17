import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    FRIENDS = [ 'Jonathan', 'Adam', 'Barbara', 'Bob' ]

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print('hi')
    
    def help_greet(self):
        print('\n'.join(['greet [person]', 'greet named person']))

    def complete_greet(self, text, line, begidix, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f for f in self.FRIENDS if f.startswith(text) ]
        return completions
        
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()