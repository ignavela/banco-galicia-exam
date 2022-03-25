import subprocess
import os

content = "galicia.html"

try: # should work on Windows
    os.startfile(content)
except AttributeError:
    try: # should work on MacOS and most linux versions
        subprocess.call(['open', content])
    except:
        print('Could not open URL')