# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:06:17 2017

@author: Meidi
"""

import urllib2
import urllib
import time
import json
http_url = 'https://api-us.faceplusplus.com/facepp/v3/compare'
key = "5XBmEnCpmdb0NfzDMTfaP6zxUXaGcnte"
secret = "QsXI8xpdyNapNAqwh3PxLhMepMMm0oGw"

def compare(filepath1, filepath2):
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
    data.append(key)
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
    data.append(secret)
    data.append('--%s' % boundary)
    fr=open(filepath1,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="first.jpg"' % 'image_file1')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s' % boundary)
    
    fr=open(filepath2,'rb')
    data.append('Content-Disposition: form-data; name="%s"; filename="second.jpg"' % 'image_file2')
    data.append('Content-Type: %s\r\n' % 'application/octet-stream')
    data.append(fr.read())
    fr.close()
    data.append('--%s--\r\n' % boundary)
    
    http_body='\r\n'.join(data)
    #buld http request
    req=urllib2.Request(http_url)
    #header
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_data(http_body)
    try:
        #post data to server
        resp = urllib2.urlopen(req, timeout=5)
        #get response
        qrcont=resp.read()
        resultDict = json.loads(qrcont)
        if 'error_message' in resultDict:
            print resultDict['error_message']
            return
        elif 'confidence' in resultDict:
            return resultDict['confidence']
        else:
            return
    
    except urllib2.HTTPError as e:
        print e.read()