# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 08:10:48 2019

@author: 张伟英
"""

import requests

import urllib.request as br

import json

import HeaderInfo

class UtilDat:
    
    header_info = HeaderInfo
    
    #获取date数据
    def dat1(u, headers):
        
        req = requests.get(u, headers = headers, verify = False)
        
        req.encoding = 'utf-8'
        
        tad = req.text

        date = json.loads(tad)
        
        return date
    
    def dat2(self, keyword):
        
        kword = br.quote(keyword, encoding = 'utf-8')
        
        url = self.header_info.search_url
        
        headers = self.header_info.search_headers
        
        while True:
            
            req = requests.get(url.format(kword), headers = headers, verify = False)
            
            req.encoding = 'utf-8'
            
            date = json.loads(req.text)
            
            if date['status_code'] == 0:
                
                return date
            
            print('加载失败')
        
        
    
    
    
    
    