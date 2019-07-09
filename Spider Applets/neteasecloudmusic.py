import requests
from lxml import etree
import re
from bson import json_util

import mongoengine
# from mongoengine import connect

class PlaylistModel(mongoengine.Document):
    playlist_id = mongoengine.IntField(default=None)                # 歌单id
    playlist_name = mongoengine.StringField(default=None)           # 歌单名称
    playlist_coverImgUrl = mongoengine.URLField(default=None)       # 歌单图片url
    playlist_createTime = mongoengine.IntField(default=None)        # 歌单创建时间
    playlist_tags = mongoengine.ListField(default=None)             # 歌单标签
    playlist_description = mongoengine.StringField(default=None)    # 歌单简介
    playlist_shareCount = mongoengine.IntField(default=None)        # 歌单分享次数
    playlist_commentCount = mongoengine.IntField(default=None)      # 歌单评论次数
    playlist_subscribedCount = mongoengine.IntField(default=None)   # 歌单收藏次数
    playlist_playCount = mongoengine.IntField(default=None)         # 歌单播放次数
    creator_avatarUrl = mongoengine.URLField(default=None)          # 歌单创建者头像url
    creator_userId = mongoengine.IntField(default=None)             # 歌单创建者id
    creator_nickname = mongoengine.StringField(default=None)        # 歌单创建者昵称
    playlist_trackCount = mongoengine.IntField(default=None)        # 歌曲数
    playlist_songId = mongoengine.ListField(default=None)           # 获取歌单歌曲id

class SongModel(mongoengine.Document):
    song_id = mongoengine.IntField(default=None)                    # 歌曲id
    song_name = mongoengine.StringField(default=None)               # 歌曲名
    song_singer = mongoengine.ListField(default=None)               # 歌手
    song_album = mongoengine.DictField(default=None)                # 专辑
    song_publishTime = mongoengine.IntField(default=None)           # 上传时间
    song_hquality = mongoengine.DictField(default=None)             # 320k音质
    song_mquality = mongoengine.DictField(default=None)             # 192k音质
    song_lquality = mongoengine.DictField(default=None)             # 128k音质
    song_url = mongoengine.URLField(default=None)                   # 歌曲文件url
    song_lyric = mongoengine.DictField(default=None)                # 歌词lrc
    song_klyric = mongoengine.DictField(default=None)               # 歌词klyric
    song_tlyric = mongoengine.DictField(default=None)               # 歌词tlyric
    song_comments = mongoengine.ListField(default=None)             # 歌曲评论id
    
class neteasecloudSpider(object):
    def __init__(self):
        self.playlist_url = 'https://api.imjad.cn/cloudmusic/?type=playlist&id='
        self.detail_url = 'https://api.imjad.cn/cloudmusic/?type=detail&id='
        self.song_url = 'https://api.imjad.cn/cloudmusic/?type=song&id='
        self.comments_url = 'https://api.imjad.cn/cloudmusic/?type=comments&id='
        self.lyric_url = 'https://api.imjad.cn/cloudmusic/?type=lyric&id='

    # 发送请求
    def get_response(self, url):
        response = requests.get(url)
        data = response.content.decode()
        return data

    # 解析歌单数据
    def playlist_parse_data(self,data):
        # 把str格式的data转为dic
        '''
        dic:{
            "playlist":{},
            "code": 200,
            "privileges":{}
        }
        playlist 存放歌单信息
        privileges 存放歌曲id，bit
        '''
        # 直接对playlist处理，获取数据
        dic = json_util.loads(data)['playlist']

        # 获取歌单id
        playlist_id = dic['id']

        # 获取歌单名称
        playlist_name = dic['name']

        # 获取歌单图片url
        playlist_coverImgUrl = dic['coverImgUrl']

        # 歌单创建时间
        playlist_createTime = dic['createTime']

        # 歌单标签, 格式：["",""]
        playlist_tags = dic['tags']

        # 歌单简介
        playlist_description = dic['description']

        # 歌曲数
        playlist_trackCount = dic['trackCount']

        # 歌单分享次数
        playlist_shareCount = dic['shareCount']

        # 歌单评论次数
        playlist_commentCount = dic['commentCount']

        # 歌单收藏次数
        playlist_subscribedCount = dic['subscribedCount']

        # 歌单播放次数
        playlist_playCount = dic['playCount']

        # 获取歌单创建者信息
        playlist_creator = dic['creator']

        # 歌单创建者头像url
        creator_avatarUrl = playlist_creator['avatarUrl']

        # 创建者id和昵称
        creator_userId = playlist_creator['userId']
        creator_nickname = playlist_creator['nickname']
        
        # 获取歌单歌曲id，按["","",""]存放
        playlist_songId = []
        for num in dic['trackIds']:
            playlist_songId.append(num['id'])
        
        playlist_dic = {
            "playlist_id" : playlist_id,                            # 歌单id
            "playlist_name" : playlist_name,                        # 歌单名称
            "playlist_coverImgUrl" : playlist_coverImgUrl,          # 歌单图片url
            "playlist_createTime" : playlist_createTime,            # 歌单创建时间
            "playlist_tags" : playlist_tags,                        # 歌单标签
            "playlist_description" : playlist_description,          # 歌单简介
            "playlist_shareCount" : playlist_shareCount,            # 歌单分享次数
            "playlist_commentCount" : playlist_commentCount,        # 歌单评论次数
            "playlist_subscribedCount" : playlist_subscribedCount,  # 歌单收藏次数
            "playlist_playCount" : playlist_playCount,              # 歌单播放次数
            "creator_avatarUrl" : creator_avatarUrl,                # 歌单创建者头像url
            "creator_userId" : creator_userId,                      # 歌单创建者id
            "creator_nickname" : creator_nickname,                  # 歌单创建者昵称
            "playlist_trackCount" : playlist_trackCount,            # 歌曲数
            "playlist_songId" : playlist_songId                     # 获取歌单歌曲id
        }
        return playlist_dic

    # 解析歌曲数据
    def detail_parse_data(self, data):
        # 把str格式的data转为dic
        '''
        dic:{
            "songs":[],
            "code": 200,
            "privileges":[]
        }
        songs 存放歌曲信息
        privileges 存放歌曲id等什么不知道的东西
        '''
        # 将str转为dic，提取歌曲信息list
        #print(json_util.loads(data))
        dic = json_util.loads(data)['songs'][0]

        # 歌曲名字
        song_name = dic['name']

        # 歌曲id
        song_id = dic['id']

        # 歌手, [{}{}{}]
        song_singer = []
        singer_lambda = lambda li: {'id':li['id'],'name':li['name']}
        for num in dic['ar']:
            song_singer.append(singer_lambda(num))

        # 专辑
        song_album = dic['al']

        # 上传时间
        song_publishTime = dic['publishTime']

        quality_lambda = lambda li: {'br':li['br'],'size':li['size']}
        # 320k音质
        if dic['h'] == None:
            song_hquality = None
        else:
            song_hquality = quality_lambda(dic['h'])

        # 192k音质
        if dic['m'] == None:
            song_mquality = None
        else:
            song_mquality = quality_lambda(dic['m'])

        # 128k音质
        if dic['l'] == None:
            song_lquality = None
        else:
            song_lquality = quality_lambda(dic['l'])

        song_lyric, song_klyric, song_tlyric = self.lyric_parse_data(self.get_response(self.lyric_url + str(song_id)))

        song_dic = {
            "song_id" :song_id,                         # 歌曲id
            "song_name" : song_name,                    # 歌曲名
            "song_singer" : song_singer,                # 歌手
            "song_album" : song_album,                  # 专辑
            "song_publishTime" :song_publishTime,       # 上传时间
            "song_hquality" : song_hquality,            # 320k音质
            "song_mquality" : song_mquality,            # 192k音质
            "song_lquality" : song_lquality,            # 128k音质
            "song_lyric" : song_lyric,                  # 歌词lrc
            "song_klyric" : song_klyric,                # 歌词klyric
            "song_tlyric" : song_tlyric                 # 歌词tlyric
            #"song_url" : song_url                      # 歌曲文件url
        }
        #print(song_dic)
        return song_dic

    # 解析歌词数据
    def lyric_parse_data(self, data):
        lyric_dic = json_util.loads(data)

        if ('nolyric' in lyric_dic and lyric_dic['nolyric'] == True) or ('uncollected' in lyric_dic and lyric_dic['uncollected'] == True):
            song_lyric = None
            song_klyric = None
            song_tlyric = None
        else:
            # 歌词lrc
            song_lyric = lyric_dic['lrc']

            # 歌词klyric
            song_klyric = lyric_dic['klyric']

            # 歌词tlyric
            song_tlyric = lyric_dic['tlyric']

        song_lrc_dic ={
            "song_lyric":song_lyric,
            "song_klyric":song_klyric,
            "song_tlyric":song_tlyric
        }
        return song_lyric, song_klyric, song_tlyric

    # 解析评论
    def comments_parse_data(self, data):
        # 把str格式的data转为dic
        '''
        dic:{
            "songs":[],
            "code": 200,
            "privileges":[]
        }
        songs 存放歌曲信息
        privileges 存放歌曲id等什么不知道的东西
        '''
        # 将str转为dic，提取评论
        #print(json_util.loads(data))
        dic = json_util.loads(data)
        hot_dic = dic['hotComments']
        new_dic = dic['comments']

        # 热门评论
        song_name = hot_dic['name']

        # 歌曲id
        song_id = dic['id']

        # 歌手, [{}{}{}]
        song_singer = []
        singer_lambda = lambda li: {'id':li['id'],'name':li['name']}
        for num in dic['ar']:
            song_singer.append(singer_lambda(num))

        # 专辑
        song_album = dic['al']

        # 上传时间
        song_publishTime = dic['publishTime']

        quality_lambda = lambda li: {'br':li['br'],'size':li['size']}
        # 320k音质
        if dic['h'] == None:
            song_hquality = None
        else:
            song_hquality = quality_lambda(dic['h'])

        # 192k音质
        if dic['m'] == None:
            song_mquality = None
        else:
            song_mquality = quality_lambda(dic['m'])

        # 128k音质
        if dic['l'] == None:
            song_lquality = None
        else:
            song_lquality = quality_lambda(dic['l'])

        song_lyric, song_klyric, song_tlyric = self.lyric_parse_data(self.get_response(self.lyric_url + str(song_id)))

        song_dic = {
            "song_id" :song_id,                         # 歌曲id
            "song_name" : song_name,                    # 歌曲名
            "song_singer" : song_singer,                # 歌手
            "song_album" : song_album,                  # 专辑
            "song_publishTime" :song_publishTime,       # 上传时间
            "song_hquality" : song_hquality,            # 320k音质
            "song_mquality" : song_mquality,            # 192k音质
            "song_lquality" : song_lquality,            # 128k音质
            "song_lyric" : song_lyric,                  # 歌词lrc
            "song_klyric" : song_klyric,                # 歌词klyric
            "song_tlyric" : song_tlyric                 # 歌词tlyric
            #"song_url" : song_url                      # 歌曲文件url
        }
        print(song_dic)
        return song_dic

    def save_mongodb(self, dic, type):
        # 连接数据库 mongodb
        mongoengine.connect('missChating', host='127.0.0.1')

        # 创建Model
        if type == 'playlist':
            mongo_data = PlaylistModel(
            playlist_id = dic['playlist_id'],
            playlist_name = dic['playlist_name'],
            playlist_coverImgUrl = dic['playlist_coverImgUrl'],
            playlist_createTime = dic['playlist_createTime'],
            playlist_tags = dic['playlist_tags'],
            playlist_description = dic['playlist_description'],
            playlist_shareCount = dic['playlist_shareCount'],
            playlist_commentCount = dic['playlist_commentCount'],
            playlist_subscribedCount = dic['playlist_subscribedCount'],
            playlist_playCount = dic['playlist_playCount'],
            creator_avatarUrl = dic['creator_avatarUrl'],
            creator_userId = dic['creator_userId'],
            creator_nickname = dic['creator_nickname'],
            playlist_trackCount = dic['playlist_trackCount'],
            playlist_songId = dic['playlist_songId']
        )
        elif type == 'detail':
            mongo_data = SongModel(
                song_id = dic['song_id'],
                song_name = dic['song_name'],
                song_singer = dic['song_singer'],
                song_album = dic['song_album'],
                song_hquality = dic['song_hquality'],
                song_mquality = dic['song_mquality'],
                song_lquality = dic['song_lquality'],
                song_url = self.song_url + str(dic['song_id']),
                song_lyric = dic['song_lyric'],
                song_klyric = dic['song_klyric'],
                song_tlyric = dic['song_tlyric']
            )

        elif type == 'lyric':
            mongo_data = SongModel(
                song_lyric = dic['song_lyric'],
                song_klyric = dic['song_klyric'],
                song_tlyric = dic['song_tlyric']
            )
        elif type == 'comments':
            pass
        else:
            print("error")
        

        # 存入数据库
        mongo_data.save()

    

    def run(self, type, id):
        if type == 'playlist':
            # 拼接url
            run_url = self.playlist_url + id
            # 发送请求
            run_data = self.get_response(run_url)
            # 解析数据
            run_data_dic = self.playlist_parse_data(run_data)
            # 保存数据至数据库
            self.save_mongodb(run_data_dic, type)

        elif type == 'detail':
            # 拼接url
            run_url = self.detail_url + id
            # 发送请求
            run_data = self.get_response(run_url)
            # 解析数据
            run_data_dic = self.detail_parse_data(run_data)
            # 保存数据至数据库
            self.save_mongodb(run_data_dic, type)

        elif type == 'comments':
            pass

        elif type == 'lyric':
            pa# 拼接url
            run_url = self.lyric_url + id
            # 发送请求
            run_data = self.get_response(run_url)
            # 解析数据
            run_data_dic = self.lyric_parse_data(run_data)
            # 保存数据至数据库
            self.save_mongodb(run_data_dic, type)

        else:
            print("error")
        


if __name__ == '__main__':
    #type = input("输入type：")
    #id = input("输入id：")
    mongoengine.connect('missChating', host='127.0.0.1')

    songdetail = PlaylistModel.objects()
    if len(songdetail) == 0:
        print("查询结果为空，error")
    datali = []
    asd = 1
    asds = 1
    #neteasecloudSpider().run("detail", str(481169047))
    
    for das in songdetail[7:]:
        ds = das._data['playlist_songId']
        for n in ds:
            neteasecloudSpider().run("detail", str(n))
            print("id:{}, 第{}首歌曲写入完成".format(str(n),asds))
            asds += 1
        print("############################################################")
        print("第{}个歌单写入完成".format(asd))
        asd += 1

    '''
    songdetail = SongModel.objects()
    asd = 1
    for das in songdetail:
        n = das._data['playlist_songId']
        neteasecloudSpider().run("detail", str(n))
        print("id:{}, 第{}首歌歌词写入数据库完成".format(str(n),asd))
        asd += 1
    '''