import os
import shutil
from mojo.extensions import ExtensionBundle

baseFolder = os.path.dirname(__file__)
libPath = os.path.join(baseFolder, 'lib')
extensionFile = "fontTools.roboFontExt"
extensionPath = os.path.join(baseFolder, extensionFile)
fontToolsHtml = '/_code/fonttools/Doc/build/html'

print(baseFolder)
print(extensionPath)

print("building FontTools Docs extension...\n")

# remove existing extension
if os.path.exists(extensionPath):
    print("\tremoving old RoboFont extension...")
    shutil.rmtree(extensionPath)

# build new extension
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
B.save(extensionPath, libPath=libPath, resourcesPath=None, pycOnly=False)

# # # remove git repository from extension
# # extensionLibPath = os.path.join(extensionPath, 'lib')
# # if os.path.exists(extensionLibPath):
# #     # remove git repository
# #     gitPath = os.path.join(extensionLibPath, '.git')
# #     if os.path.exists(gitPath):
# #         print '\tremoving git repository from extension...'
# #         shutil.rmtree(gitPath)
# #     # remove gitignore file
# #     gitignorePath = os.path.join(extensionLibPath, '.gitignore')
# #     if os.path.exists(gitignorePath):
# #         print '\tremoving .gitignore file from extension...'
# #         os.remove(gitignorePath)

# # # remove extension from extension (!!)
# # if os.path.exists(extensionLibPath):
# #     duplicateExtensionPath = os.path.join(extensionLibPath, 'extension')
# #     if os.path.exists(duplicateExtensionPath):
# #         print '\tremoving extension folder from extension...'
# #         shutil.rmtree(duplicateExtensionPath)

# # # removing .pyc files from extension
# # if os.path.exists(extensionLibPath):
# #     allFiles = os.listdir(extensionLibPath)
# #     print '\tremoving .pyc files from extension...'
# #     for file_ in allFiles:
# #         if os.path.splitext(file_)[1] == '.pyc':
# #             filePath = os.path.join(extensionLibPath, file_)
# #             os.remove(filePath)

# # print
# # print '...done.\n'
