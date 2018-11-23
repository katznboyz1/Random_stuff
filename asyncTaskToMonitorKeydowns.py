import msvcrt, _thread, sys, functools

def registerKeyDown(key):
    key = str(key)
    sys.stdout.flush()
    sys.stdout.write(('\r' + key))

def monitorKeyDowns():
    while (1):
        keydown = msvcrt.getch()
        if (keydown in [b'\x03', b'\x1b']):
            exit()
            quit()
            sys.exit()
            raise BaseException('Force quitted')
        registerKeyDown(keydown)

_thread.start_new_thread(monitorKeyDowns, ())

while (1):
    None