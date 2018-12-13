import winsound, _thread

def track1():
    winsound.Beep(600, 75)
    winsound.Beep(600, 75)
    winsound.Beep(1200, 125)
    winsound.Beep(900, 125)
    winsound.Beep(850, 125)
    winsound.Beep(800, 100)
    winsound.Beep(700, 100)
    winsound.Beep(600, 100)
    winsound.Beep(700, 100)
    winsound.Beep(800, 100)
    winsound.Beep(555, 75)
    winsound.Beep(555, 75)
    winsound.Beep(1200, 125)
    winsound.Beep(900, 125)
    winsound.Beep(850, 125)
    winsound.Beep(800, 100)
    winsound.Beep(700, 100)
    winsound.Beep(600, 100)
    winsound.Beep(700, 100)
    winsound.Beep(800, 100)
    winsound.Beep(520, 75)
    winsound.Beep(520, 75)
    winsound.Beep(1200, 125)
    winsound.Beep(900, 125)
    winsound.Beep(850, 125)
    winsound.Beep(800, 100)
    winsound.Beep(700, 100)
    winsound.Beep(600, 100)
    winsound.Beep(700, 100)
    winsound.Beep(800, 100)
    winsound.Beep(490, 75)
    winsound.Beep(490, 75)
    winsound.Beep(1200, 125)
    winsound.Beep(900, 125)
    winsound.Beep(850, 125)
    winsound.Beep(800, 100)
    winsound.Beep(700, 100)
    winsound.Beep(600, 100)
    winsound.Beep(700, 100)
    winsound.Beep(800, 100)

def bass():
    None

#work on bass track

track1()
basstrack1 = _thread.start_new_thread(bass, ()) #plays bass behind next track
track1()