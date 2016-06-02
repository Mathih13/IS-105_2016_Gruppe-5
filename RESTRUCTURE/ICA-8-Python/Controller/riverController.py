# Import data about canvas and it's objects as well as the frame
# for the program
from Display import *
from Server import clientController

# River and SM are the "model" of this
# design
from Tkinter import *


class riverController():
    
    def __init__(self, master, canvasData):
        self.master = master
        self.canvasData = canvasData
        self.setUpButtons()
        self.riverdb = self.getDB()
    
  
        
    def setUpButtons(self):
        a = Button(self.master, text="Get In", command=self.getIn)
        a.pack(side=LEFT)
        
        b= Button(self.master, text="Get out", command=self.getOut)
        b.pack(side=LEFT)
        
        c = Button(self.master, text="Chicken in", command=self.chickenIn)
        c.pack(side=LEFT)
        
        f= Button(self.master, text="Grain in", command=self.grainIn)
        f.pack(side=LEFT)        
        
        e= Button(self.master, text ="Fox in", command=self.foxIn)
        e.pack(side=LEFT)        
        
        d= Button(self.master, text="Drive boat right", command=self.moveBoatRight)
        d.pack(side=LEFT)
        
        
        h = Button(self.master, text="Drive boat left", command=self.moveBoatLeft)
        h.pack(side=LEFT)
        
        g= Button(self.master, text="chicken out", command=self.chickenOut)
        g.pack(side=LEFT)        
        
        j=Button(self.master, text="Fox Out", command=self.foxOut)
        j.pack(side=LEFT)
        
        i=Button(self.master, text="Grain Out", command=self.grainOut)
        i.pack(side = LEFT)
        
 
        
     
    
        
    def getOut(self):
        self.riverdb = self.getDB()
        if ('man isat boat' in self.riverdb):
            if ('boat isat left' in self.riverdb):
                self.canvasData.man.move(-100, 20)
                self.river.getout()
            elif ('boat isat right' in self.riverdb):
                self.canvasData.man.move(+100, 20)
                self.river.getout()
                
            
        else:
            print "Man is not in boat"
            return


        
    def getIn(self):
        self.riverdb = self.getDB()
        if ('man isat left' in self.riverdb and 'boat isat left' in self.riverdb):
            clientController.sendAndRecieve('getin')
            self.canvasData.man.move(100, -20)

            
        elif ('man isat right' in self.riverdb and 'boat isat right' in self.riverdb):
            self.river.getIn()
            self.canvasData.man.move(-100, -20)
        elif ('man isat boat' in self.riverdb):
            print "Man is already in boat"
            return

      
    def moveBoatRight(self):
        self.riverdb = self.getDB()
        
        
        if ('chicken isat boat' or 'fox isat boat' or 'grain isat boat' in self.riverdb and ('boat isat left' in self.riverdb)):
            
            if ('chicken isat boat' in self.riverdb):
                self.canvasData.chicken.move(390,1)
                self.canvasData.boat.move(390,1)
                self.canvasData.man.move(390,1)
                self.river.crossriver()

                
            if ('grain isat boat' in self.riverdb):
                self.canvasData.grain.move(390,1)
                self.canvasData.boat.move(390,1)
                self.canvasData.man.move(390,1)
                self.river.crossriver()
            
            if ('fox isat boat' in self.riverdb):
                self.canvasData.fox.move(390, 1)
                self.canvasData.boat.move(390, 1)
                self.canvasData.man.move(390,1)
                self.river.crossriver()
                

    def moveBoatLeft(self):
        self.riverdb = self.getDB()

        
        if ('chicken isat boat' or 'fox isat boat' or 'grain isat boat' in self.riverdb and 'boat isat right' in self.riverdb):
             
            if ('chicken isat boat' in self.riverdb):
                self.river.crossriver()
                self.canvasData.chicken.move(-390, -1)
                self.canvasData.boat.move(-390,-1)
                self.canvasData.man.move(-390,-1)
                
            else: 
                    self.canvasData.boat.move(-390,-1)
                    self.canvasData.man.move(-390,-1)
                    self.river.crossriver()  
                
        
    
        
            
    def chickenOut(self):
        self.riverdb = self.getDB()
        if (['chicken isat boat']  and 'boat isat right'in self.riverdb):
            self.river.takeOut("chicken")
            self.canvasData.chicken.move(220, 20) 
            
        if ('chicken isat boat' and 'boat isat left' in self.riverdb):
            self.river.takeOut("chicken")
            self.canvasData.chicken.move(-130, 20)
        
    
    
    def chickenIn(self):
        self.riverdb = self.getDB()
        
        if ('grain isat boat' in self.riverdb):
            print "boat is full"        
        
        elif ('fox isat boat'in self.riverdb):
            print "boat is full"
        
        elif ('chicken isat right' in self.riverdb):
            self.river.putIn("chicken")
            self.canvasData.chicken.move(-180,-20)
            
        
        elif (self.river.statusCheck == "s1" or "s14" or "s20"):
            self.river.putIn("chicken")
            self.canvasData.chicken.move(130,-20)
            

     

    def foxIn(self):
        self.riverdb = self.getDB()

        if ('chicken isat boat' in self.riverdb):
            print "boat is full"
            
        elif ('grain isat boat' in self.riverdb):
            print "boat is full"           
    
        elif (self.river.statusCheck == "s1" or "s6" or "s13" or "s14" ):
            self.river.putIn("fox")
            self.canvasData.fox.move(220, -20)   
        else:
            print"Noo noon noo"
            
    def foxOut(self):
        stat = self.river.statusCheck()
        if ('fox isat boat' and 'boat isat right' in self.riverdb):
            self.river.takeOut("fox")
            self.canvasData.fox.move(210, 20)
       
        
    def grainIn(self):
        self.riverdb = self.getDB()
        
        if ('chicken isat boat' in self.riverdb):
            print "boat is full"        
        
        elif ('fox isat boat'in self.riverdb):
            print "boat is full"        
        
        elif (['grain isat left'] and 'boat isat left' in self.riverdb):
            self.river.putIn("grain")
            self.canvasData.grain.move(180, -20)  
            
    def grainOut(self):
        self.riverdb = self.getDB()
        if ('grain isat boat' and 'boat isat right' in self.riverdb):
            self.river.takeOut("grain")
            self.canvasData.grain.move(+160, 20)
            
    def getDB(self):
        return clientController.sendAndRecieve('db')    
            