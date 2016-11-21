import settings

class inputbuffer:
    @staticmethod
    def getTitleType(title):
        # private function
        # 0 Type = Click Buffer
        # 1 Type = Key button Buffer
        titleType = {
            0: ['setObject'],
            1: ['getKeyInput']
        }
        for key, value in titleType.items():
            for each in value:
                if(each == title):
                    return key

        return False
    @staticmethod
    def get():
        return settings.inputBuffer

    @staticmethod
    def exists():
        if('type' in settings.inputBuffer):
            return True
        return False

    @staticmethod
    def create(title, args = None):
        if(title == 'setObject'):
            settings.inputBuffer['click'] = 1


        settings.inputBuffer['type'] = inputbuffer.getTitleType(title)
        settings.inputBuffer['title'] = title
        settings.inputBuffer['args'] = args

    @staticmethod
    def isClick():
        if(inputbuffer.exists()):
            if(settings.inputBuffer['type'] == 0):
                return True
            return False

    @staticmethod
    def isKey():
        if(settings.inputBuffer['type'] == 1):
            return True
        return False

    @staticmethod
    def clear():
        settings.inputBuffer = {}

    @staticmethod
    def getArgs():
        return settings.inputBuffer['args']

    @staticmethod
    def getClick():
        return settings.inputBuffer['click']