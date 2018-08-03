import sys
import os

appName = "YourAppName"

if __name__ == "__main__":
    print(sys.argv)
    fileName = sys.argv[1]
    print(fileName)

    if len(fileName) == 0:
        print("No fileName, Please Input a FileName")
        exit(0)

    cmd = './symbolicatecrash ' + fileName + ".crash " + appName

    version = ""
    if len(sys.argv) > 2:
        version = str(sys.argv[2])
    cmd = cmd + version + ".app"

    cmd = cmd + " > " + fileName + ".log"
    # print("cmd = ", cmd)
    print("正在解析...")
    os.system(cmd)
    print("解析完成!!!")

