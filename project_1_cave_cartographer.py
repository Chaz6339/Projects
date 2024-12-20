'''
Project 1: Cave Cartographer

Legend for the Text file: 
-----------------------------------------------------------------------------------------------
Symbol    Meaning     Can you walk through it?     Console
-----------------------------------------------------------------------------------------------
R         Rock        No                           N/A                                           
_         Empty       Yes                          None                                          
S         Start       Yes                          "Entrance to the cave."                          
E         E           Yes                          End the game if the cave has been explored.
-----------------------------------------------------------------------------------------------

What you have to do:
    Any comment of the form 
    TODO: Here is a task for you to do 
    indicates that there is something you have to do there. Use Ctrl/Cmd+F to find all the tasks you have to do.
'''

# Classes
class Cave :
    """
    Cave Class
    This contains information about the entirety of the cave. Needs to be passed a text file.
    """
    def __init__(self, file) :
        self.cave_file = file           # (string) file name containing 
        self.layout = [["S"], ["E"]]    # (2D list of int) default cave
        self.width  = 1                 # (int) default width
        self.height = 2                 # (int) default height
        self.starting_spot = [0, 0]     # (list of int) default starting position

    def create_cave(self) :
        """
        Creates a cave from the input text file. 
        """
        fileR = open(self.cave_file, "r")
        x = fileR.readlines()
        fileR.close()
        y = []
        for string in x:
            string.replace("\n", "")
            row = string.split()
            y.append(row)
        self.layout = y
        #print (self.layout)

        self.height = len(y)
        self.width = len(y[0])
        sCount = 0
        eCount = 0
        #find starting point
        for rowIndex in range(self.height):
            for charIndex in range(self.width):
                c = self.layout[rowIndex][charIndex]

                if c == "S":
                    sCount +=1
                    self.starting_spot = [rowIndex, charIndex]
                    print("starting:", self.starting_spot)
                    #Finding only 1 exit point
                if c == "E":
                    eCount += 1


        if sCount != 1:
            raise Exception("Your starting point could not be located or you have more than 1 starting point.")
        if eCount !=1:
            raise Exception("Your exit could not be located or you have more than 1 exit point.")
        
 

#CHECKING THAT CAVE IS SURROUNDED BY ROCK
        #First column rock check
        for charIndex in range(self.width):
            c = self.layout[0][charIndex]
            if c != "R":
                raise Exception("Your 'left wall' is not made of rock")
        #Last column rock check
        for charIndex in range(self.width):
            c = self.layout[-1][charIndex]
            if c != "R":
                raise Exception("Your 'right wall' is not made of rock")
        #Ceiling rock check
        for rowIndex in range(self.height):
            c = self.layout[rowIndex][0]
            if c != "R":
                raise Exception("Your 'ceiling' is not made of rock")
        #Floor rock check
        for rowIndex in range(self.height):
            c = self.layout[rowIndex][-1]
            if c != "R":
                raise Exception("Your 'floor' is not made of rock")


        #Check rectangle
            
        for row in self.layout:
            if len(row) != self.width:
                raise Exception("Your cave is not a rectangle!")

        







        #Checks begin

        #Check if cave is a rectangle
        

        # TODO: Open cave file 

        # TODO: Read the cave file into a variable 

        # TODO: Close Cave file

        # TODO: Create the 2D list representing the cave 
        
        # TODO: Check the following things about the provided cave file:
        # 1. The cave is a rectangle.
        # 2. There is exactly one "S". (Hint: Assign the starting spot along the way!)
        # 3. There is exactly one "E".
        # 4. Check that the cave is surrounded by R.
        # Raise a generic Exception with a custom message if any of the checks fail. 

    def get_starting_spot(self) :
        """Returns starting spot in cave."""
        #print(self.starting_spot)
        return self.starting_spot
        

    def get_height(self) :
        """Returns height of underlying cave layout."""

        return self.height
    
    def get_width(self) :
        """Returns width of underlying cave layout."""

        return self.width

    def get_layout(self) :
        """Returns underlying cave layout."""

        return self.layout

    def __str__(self) :
        """
        Create full map of underlying cave layout and return as a string. 
        """

        #for row in self.layout:
            #for char in row:
                #string += char
            #string +="\n"
        string = str(('\n'.join(''.join(item) for item in self.layout)))
        return string
        
        
                

        
        
        

        

class Adventure :
    """
    Adventure Class
    This contains all of the information about the current state of the adventure. Needs to be passed a Cave object. Has a DEFAULT_CAVE constant pointing to a default cave file.
    """

    DEFAULT_CAVE = "default_cave.txt"

    def __init__(self, cave:Cave) -> None:
        self.cave = cave                # adventure's cave is cave passed
        self.visited = [[1], [1]]       # at start, only visited square is (1,1) by default (changed in start_adventure())
        self.current_spot = [0, 0]      # current_spot in default cave begins at (0,0) by default (changed in start_adventure)

    def start_adventure(self) :
        """
        Creates the adventure out of the cave passed to it in the init method.
        1. TODO It creates the adventure's cave object. If it encounters an Exception, it proceeds to start the adventure with the default cave (make sure you have a valid default_cave.txt in the folder).
        2. TODO It retrieves the starting coordinates for the given cave object.
        3. It initializes the visited portion of the cave by illuminating the immediate surroundings of starting spot.
        """
        
        # Create Cave
        ## TODO: Run create_cave() on the passed cave.

        ### Catches exceptions using a try-except statement. In the case of an exception,
        #creates the adventure from a valid default cave. (Not part of Part 2.)
        try:
            self.cave.create_cave()
        except:
           self.cave = Cave(self.DEFAULT_CAVE)
           self.cave.create_cave()
           #print(self.cave)

        

        self.current_spot = self.cave.get_starting_spot()

        visitedLO = []

        for x in range(self.cave.height): #creates as many new lists you need (as the height value)
            visitedLi = []
            for y in range(self.cave.width): #actually puts down the 0's in the rows
                visitedLi.append(0)
            visitedLO.append(visitedLi)
        #print(visitedLO)
        self.visited = visitedLO

        self.set_visited()

        


           


        
        
            
            
        ## TODO: Set current_spot to the starting coordinates from the cave object.

        # Initialize Visited (not part of Part 2)
        
        ## Use the set_visited method to set the visited area after indicating a starting position. (Not part of Part 2.)

    def get_current_map(self) :
        """
        Returns a map of the portion of the cave that has been visited so far.
        (Not part of Part 2.)
        """


        string = ""
        
        for y in range(self.cave.height):
            for x in range(self.cave.width):
                
                if self.visited[y][x] == 0:
                    string += " ?"
                if self.visited[y][x] == 1:
                    string += " " + self.cave.layout[y][x] 
            string +="\n"

        return string

    def get_current_spot(self) :
        """
        Returns the coordinates of the current spot the cartographer is inhabiting.
        (Not part of Part 2.)
        """
        return self.cave.layout[self.current_spot[0]][self.current_spot[1]]
    
    def set_visited(self) :
        """
        Updates the area that the cartographer has visited using the current spot.
        (Not part of Part 2.)
        """
        
        x = self.current_spot[1]
        y = self.current_spot[0]

        self.visited[y][x] = 1

        
        
        self.visited[y][x] = 1
        self.visited[y-1][x] = 1
        self.visited[y-1][x+1] = 1
        self.visited[y-1][x-1] = 1

        self.visited[y+1][x] = 1
        self.visited[y+1][x+1] = 1
        self.visited[y+1][x-1] = 1

        self.visited[y][x-1] = 1
        self.visited[y][x+1] = 1
        

        

        
    def can_move(self, direction) :
        """
        Returns True if cartographer can move in given direction and False otherwise.
        (Not part of Part 2.)
        """

        x,y = self.current_spot
        
        if direction == "up" and self.cave.layout[x-1][y] != "R" and x > 0:
            return True
        elif direction == "down" and self.cave.layout[x+1][y] != "R" and x < self.cave.height - 1:
            return True
        elif direction == "left" and self.cave.layout[x][y-1] != "R" and y > 0:
            return True
        elif direction == "right" and self.cave.layout[x][y+1] != "R" and y < self.cave.width - 1:
            return True

        else:
            return False
    
    def move(self, direction) :
        """
        Moves cartographer in given direction and updates the area visited.
        (Not part of Part 2.)
        """
        if direction == "up":
            self.current_spot[0] -= 1
            

        if direction == "down":
            self.current_spot[0] += 1

        if direction == "right":
            self.current_spot[1] += 1

        if direction == "left":
            self.current_spot[1] -= 1

        self.set_visited()


    def map_complete(self) :
        """
        Returns True if the map has been completely explored.
        (Not part of Part 2.)
        """


        for y in range(self.cave.height):
            for x in range(self.cave.width):
                if self.visited[y][x] == 0:
                    return False
        return True

# Other functions
def clear_screen() :
    """Clears the text in the console."""
    print("\n" * 1000)

def print_banner() :
    """Prints the welcome banner for the adventure."""

    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~ You are in a cave! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Explore the cave by typing in commands. You can only exit the cave if the entire
cave has been explored. Good luck!
          """)

# ~ MAIN ~ #
if __name__ == "__main__" :
    # Let's Go 
    ## Begin the Adventure
    print_banner()
    input("Press Enter to start.")


   

    ## TODO: Create the Adventure object and initialize it
    
    cave = Cave(input("is there a specific cave you would like to run? If so please type the file in the correct format (ex. 'Cave.txt')"))
    adv = Adventure(cave)
    adv.start_adventure()
    
    #print(adv.map_complete())

    ## GAME LOOP ##
    clear_screen()
    print_banner()
    print(adv.get_current_map())
        
    while True:
        
        
    
        empty = ""
        
        if adv.can_move("up") == True:
            empty = empty + "up "
        if adv.can_move("down")== True:
            empty = empty + "down "
        if adv.can_move("left") == True:
            empty = empty + "left "
        if adv.can_move("right") == True:
            empty = empty + "right"
        print("You can move ", empty)
            
        
        userInput = input("What direction would you like to move in? Type lowercase 'quit' if you would like to quit the game at any point")
        if userInput == "quit":
            quit()
        if userInput.lower() == "up" and adv.can_move("up") == True:
            adv.move("up")
         
        if userInput.lower() == "down" and adv.can_move("down") == True:
            adv.move("down")

        if userInput.lower() == "left" and adv.can_move("left") == True:
            adv.move("left")

        if userInput.lower() == "right" and adv.can_move("right") == True:
            adv.move("right")
        print(adv.get_current_map())
        if adv.map_complete() == True:
            print("map is complete!")

    
        
    # (Not part of Part 2)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
