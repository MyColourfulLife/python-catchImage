#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import urllib2
class HtmlDownLoader(object):
    def download(self, new_url):
        if new_url is None:
            return
        request = urllib2.Request(new_url)
        request.add_header('User-Agent',"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()