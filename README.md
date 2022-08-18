# GLPythonTools

## iOS
### ReSymbol

Auto recursive iOS Symbol in Crash Logs. iOS奔溃日志自动解析(符号化).

[Usage用法](./iOS-symbolicatecrash/README.md)

## Python
### Auto Download MIT-Arrhythmia Data

Can auto download MIT-Arrhythmia Data (.hea|.dat|.atr) for DNN.

[Usage用法](./AutoDownloadMITArrhythmiaData/README.md)

## Scripts

### [sparse-clone.sh](Scripts/sparse-clone.sh)

Only Clone Specified Directories and Files with Sparsecheckout.

Usage:
`sh ./sparse-clone.sh <TargetFolder> <remote-git> <branch> <Sub-Directory1> <Sub-Directory2> ...`

e.g.:

`sh ./sparse-clone.sh ToMyFolder xxxx.git master examples/ sources/xxx.png`

It will only clone examples directory and sources/xxx.png to ToMyFolder from xxxx.git master branch.

