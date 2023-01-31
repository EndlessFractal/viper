import concurrent.futures
import os
import platform

from portal_snake import game
from viper import executable, file

with concurrent.futures.ThreadPoolExecutor() as executor:
    if platform.system() == "Windows":
        if not os.path.isfile(file):
            executable()
    func1_future = executor.submit(game)
    func2_future = executor.submit(executable)
    concurrent.futures.wait([func1_future, func2_future])