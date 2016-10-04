from random import randint
import settings

from engine.ui.uis.popup import popup

class userInteract:
    def __init__(self, **kwargs):
        self.activeOutput = []
        self.activeInput = []
        print('init')


        self.ui = eval(kwargs['type']+'(**kwargs)')

        self.register()


    def register(self):
        for each in self.ui.activeOutput:
            settings.activeOutputDB.append(each)


    '''
    def createPopup(self, popupid):
        result = popup.active(popupid)

        self.activeOutput.append(result[0])
        self.activeInput.append(result[1])

        #return ((len(self.activeOutput)-1), results)

    def bufferOutput(self):
        return self.activeOutput

    def bufferInput(self):
        return self.activeInput

    '''