from engine.userinteract.model.base import base
from engine.userinteract.model.menuproducerbuy import menuproducerbuy
from engine.userinteract.helper import helper as uihelper

import settings

class defaultoverlay(base):
    def __init__(self, **kwargs):
        self.basePriority = 60
        super(defaultoverlay, self).__init__(**kwargs)

    def openBuyMenu(self):
        print('BUY TOGGLE')
        uihelper.toggleModel('menuproducerbuy')

    def addInputs(self):
        self.addInput(type='mouseAction', priority=self.basePriority, title='base', attribute={
            'click': 1,
            'pos': [settings.yMax*50, 0],
            'dim': [50, settings.xMax*50],
            'event': 'none',
        })

        self.addInput(type='mouseAction', priority=self.basePriority+5, title='openBuyMenu', attribute={
            'click': 1,
            'pos': [settings.yMax*50, 0],
            'dim': [50, settings.xMax*50],
            'event': 'openBuyMenu',
        })

    def addOutputs(self):
        self.addOutput(pos=[settings.yMax*50, 0], type='shape', priority=self.basePriority ,
                       title='overlayBackground', attribute={
                'shape': 'rectangle',
                'dim': [50, settings.xMax*50],
                'color': (51, 51, 51)
            })

        self.addOutput(pos=[(settings.yMax*50) +10, 10], type='text', priority= self.basePriority + 2, title='menustoragebuytext', attribute={
            'font': 'primaryFont',
            'size': 20,
            'value': 'Balance: {0}',
            'variables': ['settings.player.balance'],
            'color': (255, 255, 255)
        })