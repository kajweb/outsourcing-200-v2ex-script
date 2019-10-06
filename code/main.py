#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
from function import * 

# 全局变量
inputFile = "";				# (S)输入文件路径
outputFolder = "output/";	# (S)输出文件夹路径

# 处理参数
argLen = len(sys.argv);
if( argLen == 1 ):
	inputFile = input("Please enter input *.yml path:");
else:
	inputFile = sys.argv[1];
if not os.path.exists(outputFolder):
	os.mkdir( outputFolder );

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