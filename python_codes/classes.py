class Parrot():
    
    species = "hello"
    
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
    def sing(self, song):
        
        return "best, i sing {}".format(str(song))
    
myparrot = Parrot('samake', 12)

print(myparrot.sing('oulala'), myparrot.name)
    