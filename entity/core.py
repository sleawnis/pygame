import pygame

import settings
from inventory import inventory
from job.helper import helper as jobhelper
from object.helper import helper as objecthelper
from engine.tick import tick
from util.tool import tool


#--------------------------------------------------
#  Factory Class
#--------------------------------------------------
class factory:
    @staticmethod
    def create(**args):
        # Generate random ID
        id = tool.genRandomString(16)

        # Initiate class
        result = (eval(args['uid']+'(**args, id=id)'))

        # Check for vehicle class
        if(result.type=='vehicle'):

            # Find suitable storage
            storage = objecthelper.getEmptyStorageAll('vehicle')[0]

            if(not storage):
                return False

            result.pos = [storage[0], storage[1]]

        settings.activeEntityDB[id] = result

        return id



#--------------------------------------------------
#  Base Class
#--------------------------------------------------
class base:
    def setVars(self, **kwargs):
        # Set common variables
        self.tickCount = 0
        self.status = 0
        self.firstMove = True
        pos = []
        self.claimed = False
        self.id = kwargs['id']
        self.tickID = settings.tick.register(5, 'settings.activeEntityDB["'+self.id+'"].doTick(0)')

    def assign(self, jobID):
        # Assign local variables based on provided job
        self.job = settings.activeJobDB[jobID]
        self.path = settings.pathDB[settings.activeJobDB[jobID].path]
        self.x = self.job.startPosition[1]*50
        self.y = self.job.startPosition[0]*50
        self.direction = 1
        self.jobID = jobID

    def unassign(self):
        # Reset local variables (upon job complete)
        self.job = 0
        self.path = 0
        self.x = 0
        self.y = 0
        self.direction = 0
        self.jobID = 0
        self.status = 0
        self.claimed = False


    def tick(self):
        if(self.tickListen!=False):
            # Call ticks and reset
            self.tickCount += 1
            for i in range(0, len(self.tickListen)):
                if (self.tickCount % self.tickListen[i] == 0):
                    self.doTick(i)
                    if(i==len(self.tickListen)):
                        self.tickCount = 0

    def doMove(self):
        # Move if status 1 only
        if (self.status == 1):
            # Iteratate path
            for i in range(0, len(self.path[1])):
                for o in range(0, len(self.path[1][i])):
                    # Find direction for current position
                    if (self.y / 50 == self.path[1][i][o][0] and self.x / 50 == self.path[1][i][o][1]):
                        if (self.direction == 4):
                            # Direction 4 means at destination
                            self.status = 3
                            jobhelper.complete(self.jobID)

                        # Change direction
                        self.direction = self.path[1][i][o][2]

            # update location tick
            if (self.direction == 0):
                self.y += -10
            elif (self.direction == 1):
                self.x += 10
            elif (self.direction == 2):
                self.y += 10
            elif (self.direction == 3):
                self.x += -10

    def place(self):
        # Blit at position
        settings.surface.blit(self.image, (self.x*50, self.y*50))

    def draw(self):
        # Transform and blit entity
        directionRotation = {
            0: 0,
            1: 270,
            2: 180,
            3: 90
        }
        base = pygame.transform.scale(self.image, (50, 50))
        base1 = base

        if(self.direction!=4):
            base1 = pygame.transform.rotate(base, directionRotation[self.direction])

        settings.surface.blit(base1, (self.x, self.y))

#===========================================================================
#  Subsidory Classes
#==============================================================
#  Car Entity
#--------------------------------------------------
class car(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(car, self).setVars(**args)
        self.image = pygame.image.load('sprites/car.png')
        self.tickListen = [5]
        self.inventory = inventory(5)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()

#--------------------------------------------------
#  Van Entity
#--------------------------------------------------
class van(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(van, self).setVars(**args)
        self.image = pygame.image.load('sprites/van.png')
        self.tickListen = [5]
        self.inventory = inventory(25)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()

#--------------------------------------------------
#  Lorry Entity
#--------------------------------------------------
class lorry(base):
    def __init__(self, **args):
        self.type = 'vehicle'
        super(lorry, self).setVars(**args)
        self.image = pygame.image.load('sprites/lorry.png')
        self.tickListen = [5]
        self.inventory = inventory(50)

    def doTick(self, tickID):
        if(tickID==0):
            self.doMove()