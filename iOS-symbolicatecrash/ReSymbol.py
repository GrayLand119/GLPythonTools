import sys
import os

appName = "AppDefaultName"

def runCmd(cmd, cmd2=None):
    try:
        os.system(cmd)
    except Exception as e:
        print(e)
        print("Please run > export DEVELOPER_DIR=\"/Applications/XCode.app/Contents/Developer\" \n and then retry")

    if cmd2 is not None:
        os.system(cmd2)
        pass
    pass

if __name__ == "__main__":
    print(sys.argv)
    fileName = ""
    version = ""
    for index in range(1, len(sys.argv)):
        param = str(sys.argv[index])
        if param.startswith("-"):
            if param == '-c':
                fileName = sys.argv[index + 1]
            elif param == '-v' or param == '-version':
                version = sys.argv[index + 1]
            elif param == '-a':
                appName = sys.argv[index + 1]

    print('fileName=', fileName)
    print('version=', version)
    print('appName=', appName)
    
    if len(fileName) == 0:
        print("No fileName")
        exit(0)

    cmd = './symbolicatecrash ' + fileName + ".crash " + appName
    cmd = cmd + version + ".app"
    cmd = cmd + " > " + fileName + ".log"

    # print("cmd = ", cmd)
    print("正在解析...")
    # os.system(cmd)
    runCmd(cmd)
    print("解析完成!!!")
