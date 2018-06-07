import random
class a():
    a = 0
    def update(): a.a += random.randint(-1, 1)

for _ in range(int(input('range: '))):
    a.update()
    if a.a > 0 and a.a < 200: print (a.a * '\u2588', _, a.a)
    elif a.a > 100: print (200 * '\u2588', _, a.a)
    else: print ('\u2588', _, a.a)
input('')
