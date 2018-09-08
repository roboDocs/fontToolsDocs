import os
from mojo.UI import HelpWindow

libFolder = os.path.dirname(__file__)
baseFolder = os.path.dirname(libFolder)
resourcesFolder = os.path.join(baseFolder, "resources")
htmlFolder = os.path.join(resourcesFolder, "htmlDocs")
htmlIndex  = os.path.join(htmlFolder, "index.html")

if os.path.exists(htmlIndex):
    H = HelpWindow(htmlIndex,
            title="FontTools Docs",
            developer="RoboDocs",
            developerURL="http://github.com/robodocs")

