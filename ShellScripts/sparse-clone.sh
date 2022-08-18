#!/bin/bash

# echo "file name: $0"
# echo "base file name: $(basename $0)"
if [[ $# -lt 4 ]]; then
	echo "++++++++++++++++++++++++++++++++++++"
	echo "Script description: "
	echo "Only Clone Specified Directories and Files with Sparsecheckout."
	echo "Usage:"
	echo "<TargetFolder> <remote-git> <branch> <Sub-Directory1> <Sub-Directory2> ..."
	echo "++++++++++++++++++++++++++++++++++++"
	exit
fi

targetDir=$1
echo "targetDir: $targetDir"
rootGit=$2
echo "rootGit: $rootGit"
branch=$3

pNum=$#
# echo "param num: $pNum"
subDirs=$?
pArr=($*)
echo "pArr: ${pArr[*]}"
sudDirsLength=$(($pNum-3))
subDirs=(${pArr[*]:3:$sudDirsLength})
# echo subDirs: ${subDirs[@]} $sudDirsLength
# echo subDirs Length : ${#subDirs[@]}

git init $targetDir
cd $targetDir
git remote add origin $rootGit
git config core.sparsecheckout true

for (( i = 0; i <= sudDirsLength; i++ )); do
	# echo "${subDirs[$i]}"
	echo "${subDirs[$i]}" >> .git/info/sparse-checkout
done

git pull --depth=1 origin $branch

# cloneDirs=$3

# ./demo.sh -s xxx.git -d example

# git init <repo>
# cd <repo>
# git remote add origin <url>
# git config core.sparsecheckout true
# echo "<path you want to clone>/*" >> .git/info/sparse-checkout
# git pull --depth=1 origin <branch you want to fetch>