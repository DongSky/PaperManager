# encoding:utf-8
from .TagTree import TagTree
from .ArxivScrapy import paperDown
from .PaperNode import PaperNode
import os


def AddPaper(userid, title, author, time, tags, source, filePath):
    pass


def initializeTagTree(userid, filePath):
    rootTag = TagTree("root", userid, None)
    with open(filePath, "w") as f:
        f.write(str(rootTag.toDict()))
        f.close()
    return rootTag


"""
function AddTag(userid, tag, parentTag)
    str userid: the symbol of TagTree
    str tag: tag needs to be added
    list parentTag: parent tags, from root to direct parent of new tag
"""


def AddTag(userid, tag, parentTag):
    pass


def getTagList(userid, currentPath):
    result = {}
    rootDir = "./resource/tags/" + userid + "/"
    rootDir += "/".join(currentPath.split("."))
    print('rootDir: ' + rootDir)
    try:
        sonDir = os.listdir(rootDir)
        sonDir = [item for item in sonDir if item[-5:] != '.json']
        print(sonDir)
    except FileNotFoundError:
        result['error_num'] = 2
        result['msg'] = "fail, no such directory"
        result['tagList'] = []
        return result
    try:
        sonDir.remove('.DS_Store')
    except:
        pass
    len_sonDir = len(sonDir)
    if len_sonDir <= 0:
        result['error_num'] = 1
        result['msg'] = "fail, no son directory exists"
        result['tagList'] = []
    else:
        result['error_num'] = 0
        result['msg'] = "success"
        result['tagList'] = sonDir
    return result


def getFileList(userid, currentPath):
    result = {}
    rootDir = "./resource/tags/" + userid + "/"
    rootDir += "/".join(currentPath.split("."))
    try:
        sonDir = os.listdir(rootDir)
    except FileNotFoundError:
        result['error_num'] = 2
        result['msg'] = "fail, no such directory"
        result['fileList'] = []
        return result
    try:
        sonDir.remove('.DS_Store')
    except:
        pass
    sonFile = []
    for son in sonDir:
        if os.path.isfile(rootDir + "/" + son):
            sonFile.append(son.split(".")[0])
    len_sonFile = len(sonFile)
    if len_sonFile <= 0:
        result['error_num'] = 1
        result['msg'] = "fail, no paper in this tag"
        result['fileList'] = []
    else:
        result['error_num'] = 0
        result['msg'] = "success"
        result['fileList'] = sonFile
    return result

if __name__ == "__main__":
    #print(getTagList("10010", "manga.lovelive"))
    #print(getTagList("10010", "manga.ddlc"))
    #print(getTagList("10010", "manga.white_album"))
    print(getTagList("10032","cs.ai"))
    print(getTagList("10032", "cs.se"))
    print(getTagList("10032", "cs"))
    print(getTagList("10033", "cs"))

