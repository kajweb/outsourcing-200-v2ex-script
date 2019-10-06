import os
import urllib.request
import datetime

def checkoutInputFile( path ):
	# 判断文件是否存在
	if not os.path.isfile( path ):
		exit("输入文件不存在");

def checkoutOutputFolder( path ):
	# if os.path.exists(path):
	# 	return True;
	# elif os.path.isfile(path):
	# 	exit("输出文件夹与文件同名");
	# else:
	# 	return False;
	return True;

# 获得真实的文件名
def getRealFileName( Str ):
	return Str.split("_")[0].split(" ")[1].split(":")[0];

def getType( info ):
	if len(info) < 10:
		return "Release version";
	if info[-10] == "_beta_ver:":
		return "Beta version";
	elif info[-11] == "_alpha_ver:":
		return "Alpha version";
	else:
		return "Release version";

def getURLInfo( url ):
	req = urllib.request.Request(url,method='HEAD');
	return urllib.request.urlopen(req).info();

def insertLine( oFile, data ):
	line = "<tr><td>%s</td><td>%s</td><td>%s</td><td><a href='%s'>点击下载</a></td><td>%s</td></tr>\n"%(data["time"],data["version"],data["type"],data["link"],data["size"]);
	oFile.write(line);

def generateTable( oFile ):
	oFile.write('<meta charset="UTF-8">\n');
	oFile.write('<style>*{padding:0;margin:0;}table{margin-left:2%;}th{text-align:left;background:rgb(243,243,243);}td,th{padding:5px;border:1px solid rgb(214,214,214);}</style>\n');
	oFile.write('<table width="96%" border="0" cellspacing="0">\n');
	oFile.write("<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>\n"%("文件时间","软件版本","软件类型","文件下载","文件大小"));

def GMT2datetime( _GMT ):
	GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
	return (datetime.datetime.strptime(_GMT, GMT_FORMAT));

def sizeConversion( size ):
    _size = int(size);
    '''
    auth: wangshengke@kedacom.com ；科达柯大侠
    递归实现，精确为最大单位值 + 小数点后三位
    '''
    def strofsize(integer, remainder, level):
        if integer >= 1024:
            remainder = integer % 1024
            integer //= 1024
            level += 1
            return strofsize(integer, remainder, level)
        else:
            return integer, remainder, level

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    integer, remainder, level = strofsize(_size, 0, 0)
    if level+1 > len(units):
        level = -1
    return ( '{}.{:>03d} {}'.format(integer, remainder, units[level]) )