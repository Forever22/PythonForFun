import urllib2
import re

def downURL(url,filename):
	print url
	print filename
        fp=urllib2.urlopen(url)
	op=open(filename,"wb")
#	print 'ok'
	while 1:
		s=fp.read()
		print 's len is: ', len(s)
		if not s:
			break
		op.write(s)
	
#	print len(s)
	fp.close()
	op.close()
	return 1

def getURL(url):
	try:
		fp=urllib2.urlopen(url)
	except:
		print 'get url exception'
		return []
	pattern=re.compile("http://sports.sina.com.cn/[^\>]+.shtml")
	while 1:
		s=fp.read()
		if not s:
			break
		urls=pattern.findall(s)
	fp.close()
	return urls

def spider(startURL,times):
	urls=[]
	urls.append(startURL)
	i=1
	while 1:
		if i>times:
			break
		if len(urls)>0:
			url=urls.pop(0)
			print url,len(urls)
			downURL(url,str(i)+'.htm')
			i=i+1
			if len(urls)<times:
				urllist=getURL(url)
				for url in urllist:
					if urls.count(url)==0:
						urls.append(url)
		else:
			break
	return urls

urls=spider('http://www.baidu.com',10)
print urls
