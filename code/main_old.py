














# 价值200块的升级版本，客户需要的时候再升级。






























#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from function import * 

# 全局变量
inputFile = "";			# (S)输入文件路径
outputFolder = "";		# (S)输出文件夹路径
commandReplace = False;	# (B)命令行带有替换参数
isReplace = False;		# (B)默认替换选项

# 处理参数
argLen = len(sys.argv);
if( argLen == 1 ):
	inputFile = input("Please enter input *.yml path:");
	outputFolder = input("Please enter the output folder:"); 
elif( argLen == 2 ):
	inputFile = sys.argv[1];
	checkoutInputFile( inputFile );
	outputFolder = input("Please enter the output folder:"); 
elif( argLen == 3 ):
	inputFile = sys.argv[1];
	checkoutInputFile( inputFile );
	outputFolder = sys.argv[2];
elif( argLen == 4 ):
	inputFile = sys.argv[1];
	checkoutInputFile( inputFile );
	outputFolder = sys.argv[2];
	if( sys.argv[3] == "Y" ):
		commandReplace = True;
		isReplace = True;
	else:
		commandReplace = True;
		isReplace = False;
else:
	exit("文件参数错误");
# 覆盖参数设置
outputFolderIsExits = checkoutOutputFolder( outputFolder );
if outputFolderIsExits and (not commandReplace):
	tempAsker = "";
	while( tempAsker != "Y" and tempAsker != "N" ):
		tempAsker = input("如果待解析的路径已存在文件，是否覆盖？（Y/N）");
	if tempAsker == "Y":
		isReplace = True;
	else:
		isReplace = False;

# 处理文件
iFile = open(inputFile, encoding='utf-8');
oFileName = "";
blockInfo = "";
oFile = False;
lastOFileName = "0";
for line in iFile:
	line=line.strip('\n');
	if( line[-1] == ":" ):
		oFileName = outputFolder + getRealFileName( line ) + ".html";
		blockType = getType( line );
		if oFile:
			oFile.close();
		if os.path.isfile( oFileName ):
			if oFileName != lastOFileName:
				print("打开文件%s："%(oFileName));
				lastOFileName = oFileName;
			oFile = open(oFileName,"a", encoding='utf-8');
		else:
			if oFileName != lastOFileName:
				print("初始化%s："%(oFileName));
				lastOFileName = oFileName;
			oFile = open(oFileName,"w", encoding='utf-8');
			generateTable( oFile );
	else:
		version = line.split(": ")[0];
		link	= line.split(": ")[1];
		urlInfo = getURLInfo( link );
		data = {
			"version":version,
			"link": link,
			"time": GMT2datetime(urlInfo["Last-Modified"]),
			"size": sizeConversion(urlInfo["Content-Length"]),
			"type": blockType,
		};
		insertLine( oFile, data );
		print("　->插入 %s %s "%(blockType, version));