import sys

sent = ' '
for iteration in sys.argv[1:]:
    sent += str(iteration) + ' '

print ('''
 {}
<{}>
 {}
        \\   ^__^
         \\  (oo)\_______
            (__)\       )\\/\\
                ||----w |
                ||     ||
'''.format(('_' * len(sent)), sent, ('-' * len(sent))))