from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper
from webinteract.market import market

import settings

class menumarketstatus(base):
    def __init__(self, **kwargs):
        self.basePriority = 80
        self.title = 'factory'
        super(menumarketstatus, self).__init__(**kwargs)

    def selectPart(self, part):
        settings.grid[self.objectPosition[0]][self.objectPosition[1]].part = part
        print('part selected')
        uihelper.toggleModel('factorypartsselectpart')

    def addInputs(self):
        self.addCommon(uid='close', pos=[0, 512])


    def addOutputs(self):
        self.addOutput(pos=[10, 10], type='text', priority= 2, title='factoryparttitle',
            attribute={
               'font': 'primaryFont',
               'size': 50,
               'value': 'Global Market',
               'color': (255, 255, 255)
           }
        )

        self.addOutput(pos=[0,0], type='shape', priority=0, title='factoryPartBackground',
            attribute={
                'shape': 'rectangle',
                'dim': [512, 512],
                'color': (0, 0, 0)
            }
        )

        marketResponse = market()
        basey = 50
        limit = 10
        current = 0

        for each in marketResponse.get():
            if(current <= limit):
                settings.marketCache[each['itemid']] = each['current_demand']

                self.addOutput(pos=[basey, 10], type='text', priority=2, title='factoryparttitle',
                   attribute={
                       'font': 'primaryFont',
                       'size': 30,
                       'value': str(each['itemid']) + ' : ' + str(each['current_demand']),
                       'color': (255, 255, 255)
                   }
                )
                current += 1
                basey += 30
            else:
                break



    def load(self, pos):
        self.objectPosition = pos

        self.refresh()