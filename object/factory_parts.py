from object.base import base
from inventory import inventory
from jobset.factory import factory as jobset
import settings


class factory_parts(base):
    def __init__(self, **kwargs):
        self.title = 'factory_parts'
        self.type = 'producer'

        super(factory_parts, self).setVars(image=self.title, **kwargs)
        self.passable = []
        self.inventory = inventory(30+settings.mod)
        self.status = 0
        self.used = False
        settings.mod = -20

    def doTick(self, tickID):

        if(tickID==0):
            #chance grow increase
            if(not self.inventory.isFull()):
                self.image = self.load(self.title)


        if (tickID == 1):
            if(settings.itemDB[self.part]['required']=={}):

                if(self.inventory.addItem('body',8)=='INVFULL') & (self.used==False):

                    self.image = self.load(self.title+'_full')

                    jobset.create(typ='collectFromObjectAndStore', startPosition=[self.y, self.x, self.direction])
                    self.used = True

            else:
                #Assume has to check inventory for parts
                data = settings.itemDB[self.part]

                hasItems = 0

                for name, quantity in data['required'].items():
                    if(self.inventory.has(name, quantity)):
                        hasItems += 1


                print('dbg')
                print(data['required'])

                print(len(data['required']))
                print(hasItems)

                if((len(data['required'])) == hasItems):
                    print('CAN CONSTRUCT')
                    if (self.inventory.buildItem('plane') == 'INVFULL') & (self.used == False):
                        print('FULL INVENTORYY')
                        pass


                print('inv')
                print(self.inventory.inventory)
                print(len(self.inventory.inventory))


