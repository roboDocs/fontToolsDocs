import os
import shutil

# update fontTools
# > git pull fontTools

# build fontTools docs
# > cd Doc
# > make html

baseFolder = os.path.dirname(__file__)
extensionFile = "fontToolsDocs.roboFontExt"
extensionPath = os.path.join(baseFolder, extensionFile)
resourcesFolder = os.path.join(extensionPath, 'resources')
htmlFolder = os.path.join(resourcesFolder, 'htmlDocs')

# hardwired to the local path on my machine
fontToolsHtml = '/_code/fonttools/Doc/build/html/'

print('updating FontTools documentation...\n')

if os.path.exists(htmlFolder):
    print("\tremoving old files...")
    shutil.rmtree(htmlFolder)

print("\tfetching the latest version...")
shutil.copytree(fontToolsHtml, htmlFolder)

print('\n...done.\n')

