from xes.ext import xes,tts
'''
名 称: play_mp3
功 能: 播放mp3音乐文件
参数1: mp3文件名称, 类型:string
返回值：无
'''
play_mp3 = xes.play_mp3


'''
名 称: air_temp
功 能: 获取某地某天的气温
参数1: 地点名称, 类型:string
参数2: 某天的索引，默认是0, 类型:int
      （0：表示当天，1：表示明天，2：表示后天，-1：表示昨天）
返回值：温度值（摄氏度），类型:int
'''
air_temp = xes.get_weather_t


'''
名 称: air_speed
功 能: 获取某地某天的风速
参数1: 地点名称, 类型:string
参数2: 某天的索引，默认是0, 类型:int
      （0：表示当天，1：表示明天，2：表示后天，-1：表示昨天）
返回值：风速值（m/s），类型:int
'''
air_speed = xes.get_weather_s


'''
名 称: send_msg
功 能: 发送短信
参数1: 电话号码, 类型:int
参数2: 要发送的信息, 类型:string
返回值：发送状态（成功，失败），类型:string
'''
send_msg = xes.send_message


'''
名 称: shengpizi
功 能: 获取一个生僻字
参数1: 无
返回值：一个生僻字，类型:string
'''
shengpizi = xes.rand_shengpizi
shengpici = xes.rand_shengpici

'''
名 称: pinyin1
功 能: 获取一个汉字的拼音
参数1: 汉字, 类型:string
返回值：汉字的拼音，类型:string
'''
pinyin1 = xes.pinyin_one

'''
名 称: pinyin
功 能: 获取一串汉字的拼音
参数1: 一串汉字, 类型:string
返回值：每一个汉字的拼音，类型:list（list中的元素是string)
'''
pinyin = xes.pinyin

'''
名 称: pinyin2
功 能: 获取多个汉子的拼音
参数1: 汉字, 类型:string
返回值：汉字的拼音，类型:string
'''
pinyin2 = xes.pinyin2


'''
名 称: chengyu
功 能: 获取一个成语，成语的首字和传入成语的最后一个字保持一致
参数1: 一个成语，默认无
返回值：成语，类型:string
'''
idiom = xes.next_chengyu


'''
名 称: is_chengyu
功 能: 判断一个词语是不是成语
参数1: 一个词语，类型:string
返回值：是成语返回'y'，不是成语返回'n'，类型:string
'''
is_idiom = xes.is_chengyu


'''
名 称: junk_info
功 能: 获取一个垃圾信息关键字列表
参数1: 无
返回值：垃圾信息关键字列表，类型:list（list中的元素是string)
'''
junk_info = xes.junk_information


'''
名 称: public_trans
功 能: 公共交通查询
参数1: 城市名称，类型:string
参数2: 起点，类型:string
参数3: 终点，类型:string
返回值：公共交通路线，类型:list（list中的元素是string)
'''
public_trans = xes.public_transport

date_diff=xes.date_diff


'''
名 称: speak
功 能: tts文字转语音
参数1: 文字内容, 类型:string
返回值：无
'''
speak = tts.speak

'''
名 称: setmode
功 能: tts设置男声boy还是女声girl
参数1: boy或者girl, 类型:string
返回值：无
'''
setmode = tts.setmode

'''
名 称: setspeed
功 能: tts设置朗读语速
参数1: 0-2, 类型:float
返回值：无
'''
setspeed = tts.setspeed

'''
名 称: sethigh
功 能: tts设置音高
无参数
返回值：无
'''
sethigh = tts.sethigh

'''
名 称: translate
功 能: tts翻译，中文翻译为英文，英文翻译为中文
参数1：待翻译的文本，类型:string
返回值：翻译后的文本，类型：string
'''
translate=tts.translate

'''
名 称: date_diff
功 能: 计算两个日期相差的天数
参数1：日期1，格式"%Y-%m-%d"，类型:string
参数2：日期2，格式"%Y-%m-%d"，类型:string
返回值：相差的天数，类型：int
'''
date_diff=xes.date_diff