class Wayterm_color:
    PLAIN = '\033[0m'
    NAME = '\033[94m'
    LABEL = '\033[95m'
    VALUE = '\033[96m'
    AT_NAME = '\033[92m'
    TIME = '\033[93m'
    DARK = '\033[90m'

    def disable(self):
        self.PLAIN = ''
        self.NAME = ''
        self.LABEL = ''
        self.VALUE = ''
        self.AT_NAME = ''
        self.TIME = ''
