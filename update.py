import os
import shutil
from mojo.extensions import ExtensionBundle

baseFolder = os.path.dirname(__file__)
libFolder = os.path.join(baseFolder, 'lib')
extensionFile = "fontTools.roboFontExt"
extensionPath = os.path.join(baseFolder, extensionFile)
htmlFolder = os.path.join(baseFolder, 'html')

#-------------
# update docs
#-------------

# update fontTools
# > git pull fontTools

# build docs
# > cd Doc
# > make html

# hardwired to the local path on my machine
fontToolsHtml = '/_code/fonttools/Doc/build/html/'

if os.path.exists(htmlFolder):
    print("\tremoving old HTML files...")
    shutil.rmtree(htmlFolder)

shutil.copytree(fontToolsHtml, htmlFolder)

#-----------------
# build extension
#-----------------

print("building FontTools Docs extension...\n")

if os.path.exists(extensionPath):
    print("\tremoving old RoboFont extension...")
    shutil.rmtree(extensionPath)

print("\trebuilding the RoboFont extension...")
B = ExtensionBundle()
B.name = "FontTools Docs"
B.developer = "RoboDocs"
B.developerURL = "http://github.com/robodocs"
B.version = "0.1"
B.mainScript = ""
B.launchAtStartUp = 0
B.addToMenu = [{
    "path" : "docs.py",
    "preferredName" : "FontTools Docs",
    "shortKey" : "",
}]
B.requiresVersionMajor = "1"
B.requiresVersionMinor = "5"
B.infoDictionary["html"] = 0
B.save(extensionPath, libPath=libFolder, resourcesPath=None, pycOnly=False)

print()
print('...done.\n')
