import os
from mojo.UI import HelpWindow

baseFolder  = os.path.dirname(__file__)
htmlFolder = os.path.join(baseFolder, "htmlDocs")
htmlIndex  = os.path.join(htmlFolder, "index.html")

if os.path.exists(htmlIndex):
    H = HelpWindow(htmlIndex,
            title="FontTools Docs",
            developer="RoboDocs",
            developerURL="http://github.com/robodocs")

