import os
from mojo.UI import HelpWindow

libFolder  = os.path.dirname(__file__)
baseFolder = os.path.dirname(libFolder)
htmlFolder = os.path.join(baseFolder, "html")
htmlIndex  = os.path.join(htmlFolder, "index.html")

if os.path.exists(htmlIndex):
    HelpWindow(htmlIndex,
            title="FontTools Docs",
            developer="RoboDocs",
            developerURL="http://github.com/robodocs")
