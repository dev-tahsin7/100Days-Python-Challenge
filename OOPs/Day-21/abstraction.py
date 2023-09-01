class GSC: # Parent class / Abstract Class
    def section(self): # Abstract Method
        pass # Abstraction don't have any body

class Tahsin: # Child Class
    def section(self):
        print("Section B")

class Zisun: # Child Class
    def section(self):
        print("Section A")

t = Tahsin()
z = Zisun()

t.section()
z.section()