import settings
from job.factory import factory as job
from jobset.base import base
from object.helper import helper as objecthelper
from entity.helper import helper as entityhelper
from pathfind import pathFind
from entity.factory import factory as entity

'''
'   Required Params:
'   position, item(id)
'''

class waitForItems(base):
    def __init__(self, **kwargs):
        self.tickListen = [10]
        super(waitForItems, self).__init__(**kwargs)
        self.pos = kwargs['position']
        self.items = kwargs['items']

    def task(self):
        print('waiting for items')
        print(self.items)

    def needsItem(self, itemID):
        print(self.items)
        for id, qty in self.items.items():
            if(id==itemID):
                return True
        return False