"""simple python script tp demonstrate the concept of simple inheritence
we have a child class which inherits the from the parent class
PLAY AROUND ...."""


class Parent():
    def __init__(self,hobby,eye_colour):
        print("parent constructor in called")
        self.hobby=hobby
        self.eye_colour=eye_colour

class Child(Parent):
    def __init__(self,hobby,eye_colour,friend):
        print("Child constructor is called")            
        Parent.__init__(self,hobby,eye_colour)
        self.boy_friend=friend             
                 
                                
your_name=Child("hacking","black","none")
print(your_name.hobby)
print(your_name.boy_friend)                 
                 
