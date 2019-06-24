# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:37:30 2019

@author: 张伟英
"""

#__author__ == 'rourou'

import UtilDat

import HeaderInfo

class PropertyInfo: 
    
    '''
    def search_info(self, *kword)#获取搜索数据
        
    def host_massage(self, url, headers)#获取首页有效字段的公共字段
    
    def properties(self, headers)#获取首页有效字段
    
    def comment_u(self)#获取评论链接
    
    def comment_info(self, headers)#获取评论信息
    
    def author_info(self, url)#获取发布者信息
    
    '''    
    
    comment_url = 'https://api.huoshan.com/hotsoon/item/{}/comments/?offset=0&count=20&req_from=normal&sort_type&live_sdk_version=600&iid=75669734468&device_id=68314386864&ac=wifi&channel=pcandroid&aid=1112&app_name=live_stream&version_code=600&version_name=6.0.0&device_platform=android&ssmix=a&device_type=sm-j200g&device_brand=samsung&language=zh&os_api=22&os_version=5.1.1&uuid=865166022069994&openudid=19b6f476238193e5&manifest_version_code=600&resolution=720*1280&dpi=240&update_version_code=6003&_rticket=1560844930906&ab_version=938059%2C951618%2C839333%2C712302%2C914029%2C936962%2C689928%2C705072%2C842000%2C928648%2C692223%2C953571%2C901581%2C850765%2C830474%2C662293%2C943434%2C557631%2C927653%2C944952%2C956299%2C919434%2C914334%2C947986%2C661947%2C819012%2C956109%2C949507%2C935981%2C938386%2C957250%2C929430%2C911475%2C501249%2C933043%2C478014%2C665355%2C922855%2C949017%2C957639%2C920238%2C927642%2C848690%2C643980%2C457535%2C950310%2C768603%2C797936%2C682009%2C946396&mcc_mnc=46000&ts=1560844930&as=a2b5f9f012f87d0a386455&cp=9988d45b25820aa7e2Ycag&mas=00df32d723ef1b2e8c29ff4b64a6f0ac284eacd8a5e2666eb0'    
    
    utildat = UtilDat#实例化工具类  
    
    header_info = HeaderInfo
    
    def search_info(self, *kword):
        
        
        date = self.utildat.UtilDat.dat2(self, *kword)

        datel = date['data'].pop()['item_result']['items']
        
        datels = [datel[i]['item'] for i in range(0, len(datel))]
        
        info = []
        
        for dat in datels:
        
            search_info = {
                    
                'video_urls' : dat['video']['url_list'][0],#视频链接
                
                'title' : dat['title'],#主题
                
                'nicknames' : dat['author']['nickname'],#别名
                
                'avatar_jpg' : dat['author']['avatar_jpg']['url_list'][0],#头像
               
                'digg_count' : dat['stats']['digg_count'],#点击喜欢
            }
            
            info.append(search_info)
        
        return dict(zip(range(0, len(info)), info))
        
        

    #获取首页有效字段的公共字段
    def host_massage(self, url, headers):
        
        date = self.utildat.UtilDat.dat1(url, headers)
        
        publ_dat = [date['data'][i]['data'] for i in range(0,len(date['data']))]
        
        return publ_dat
    
    #获取首页有效字段信息
    def properties(self,url, headers):
        
        publ_dat = self.host_massage(url, headers)#调用公有字段
        
        for publdat in publ_dat:
            
            if 'stats' in publdat:
            
                info = {
            
                    'id' : publdat['id'],#视频id，评论链接所包含的参数
                    
                    'author_city' : publdat['author']['city'],#所在城市 
                    
                    'author_nickname' : publdat['author']['nickname'],#别名
                                    
                    
                    'author_hotsoon_verified_reason' : publdat['author']['hotsoon_verified_reason'],#作者标志
                    
                    'author_fan_ticket_count' : publdat['author']['fan_ticket_count'],#火力值
                    
                    'author_birthday_description' : publdat['author']['birthday_description'],#生日描述
                    
                    'author_gender' : publdat['author']['gender'],#性别
                    
                    'author_short_id' : publdat['author']['short_id'],#用户ID
                    
        #            'description' :  publdat['description'],#视频描述
                    
                    'share_description' : publdat['share_description'],#分享介绍
                    
                    'share_title' : publdat['share_title'],#分享主题
                    
                    'share_url' : publdat['share_url'],#分享链接
                    
                    'stats_comment_count' : publdat['stats']['comment_count'],#评论数
                    
                    'stats_digg_count' : publdat['stats']['digg_count'],#喜欢人数
                    
                    'stats_play_count' : publdat['stats']['play_count'],#播放次数
                    
                    'stats_share_count' : publdat['stats']['share_count'],#转发次数
                    
                    'video_cover' : publdat['video']['cover']['url_list'][0],#封面
                    
                    'video_download_url' : publdat['video']['download_url'][0],#视频url
                    
                    'video_duration' : publdat['video']['duration'],#播放时长
                    
                    'video_h265_url' : publdat['video']['h265_url'][0]#音频url
                    
                    }
            
        return dict(info)
    
    #获取所有评论链接
    def comment_u(self, url ,headers):
        
        info = self.properties(url, headers)

        comment_ur = info['id']
        
        comment_urls = self.comment_url.format(comment_ur)
            
        return comment_urls
    
    #获取所有的评论信息
    def comment_info(self,url, headers, headers1):
        
        comment_urls = self.comment_u(url, headers)#获取所有评论url列表
        
        comment_text = []

        date = self.utildat.UtilDat.dat1(comment_urls, headers1)#调取dat方法，获得date数据
        
        count = len(date['data']['comments'])#获取每页的评论条数
 
        for i in range(0, count):
            
            comment_text.append(date['data']['comments'][i]['text'])#把获取的评论内容添加到comment中
             
        return comment_text
    
    #获取发布者信息
    def author_info(self, url,headers):
        
        date = self.utildat.UtilDat.dat1(url,headers)
        
        pre_date = [date['data'][i]['data'] for i in range(0,len(date['data']))]
        
        predat = [pre_date[i] for i in range(0, len(pre_date))]
        
        info = []
        
        for pd in predat:
            
            if 'hashtag' in pd:
        
                un_info = {
                        
                    'download_url' : pd['video']['download_url'][0],#视频连接
        
                    'face_url' : pd['author']['avatar_jpg']['url_list'][0],#头像
                    
                    'description': pd['description'],#作品描述
                    
                    'birthday_description' : pd['author']['birthday_description'],#生日描述
                    
                    'status' : pd['status'],#火山粉丝数量（万）
                    
                    'fan_ticket_count' : pd['author']['fan_ticket_count'],#火力值
                    
                    #'following_count' : tads['data']['stats']['following_count'],#关注人数
                    
                    'level_str' : pd['author']['pay_grade']['grade_icon_list'][1]['level_str'],#等级
                    
                    'icon_url' : pd['author']['pay_grade']['grade_icon_list'][1]['icon']['url_list'][0],#等级图标链接
                    
                    'signature' : pd['author']['signature'],#签名
                    
                    'nickname' : pd['author']['nickname'],#火山名
                                   
                    'entrance_desc':pd['hashtag']['entrance_desc'],#播放次数

                    
                    }
                    
                info.append(un_info)
                
        return dict(zip(range(0,len(info)), info))

#if __name__ == '__main__':
#    
#    header_info = HeaderInfo
#    
#    url = header_info.url
#    
#    comment_url = header_info.comment_url
#    
#    author_url = header_info.author_url
#    
#    headers = header_info.headers
#    
#    headers1 = header_info.comment_headers
#    
#    headers2 = header_info.author_headers
#    
#    pf = PropertyInfo()
#  
#    hre = pf.host_massage(url,headers)
#    
#    info = pf.properties(url, headers)
#      
#    comment_u = pf.comment_u(url, headers)
#    
#    comment_info = pf.comment_info(url, headers, headers1)
#    
#    author_info = pf.author_info(author_url, headers2)
#    
#    search_info = pf.search_info('喵星人')

