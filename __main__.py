from src.wayterm import Wayterm

if __name__ == "__main__":
    wayterm = Wayterm()
    wayterm._init_print()
    while True:
        try:
            command = raw_input('wayterm > ')
            if len(command) == 0:
                pass
            if command.lower() == 'exit':
                print 'exiting...'
                exit()
            else:
                wayterm.call(command.split('\\'))
        except RuntimeError:
            print 'Error, exiting...'
            exit()
