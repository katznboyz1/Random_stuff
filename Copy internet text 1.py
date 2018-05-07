import urllib.request, os, time

data = (urllib.request.urlopen(('https://' + str(input('https://')))))
data = data.read()

file = open('website_retrived.html', 'w')
file.write(str(data))
file.close()
    
os.startfile('website_retrived.html')

time.sleep(1)

os.remove('website_retrived.html')
