'''
'
'   Tick class handles registering, and calling ticking
'
'''
from util.tool import tool

class tick:
    def __init__(self):
        self.tick = {}

    def register(self, tick, action, identifier=0):
        #Identifier is optional, allows all ticks to be removed
        tickID = tool.genRandomString()
        self.tick[tickID] = [identifier, tick, action]

    def getTicks(self):
        return self.tick

    def remove(self, **kwargs):
        if('identifier' in kwargs):
            removeBuffer = []
            for key, each in self.tick.items():
                if(each[0]==kwargs['identifier']):
                    removeBuffer.append(key)

            for each in removeBuffer:
                del self.tick[each]