#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import imghdr
import os
import urllib
import shutil
import threading

q = threading.Lock()
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []
        self.basePath = os.path.dirname(__file__) + '/images'
        self.x = 1

    def collect_data(self,new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        file = open('output.html','w')
        file.write('<html>')
        file.write('<body>')
        for data in self.datas:
            file.write(data['url'])
            file.write(data['title'].encode('utf-8'))
            file.writelines(data['lists'])
            file.write("<br>")

        file.write('</body>')
        file.write('</html>')
        file.close()


    def _downloadImage(self,imgurls):
        if imgurls is None or len(imgurls) == 0:
            return
        for url in imgurls:
            if self.x > 100:
                print 'done'
                return
            path = self.basePath + '/%s.png' % self.x
            urllib.urlretrieve(url,path)
            if imghdr.what(path):
                q.acquire()
                print '正在下载第%d张图片' % self.x
                self.x += 1
                q.release()
            else:
                os.remove(path)
        print 'done'


    def downloadImages(self):
        shutil.rmtree(self.basePath,True)
        os.mkdir(self.basePath)
        tempSet = set()
        for data in self.datas:
            tempSet = tempSet | data['lists']

        self._downloadImage(tempSet)
        os.system('open %s' % self.basePath)

