# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['getsubtitle']

package_data = \
{'': ['*']}

install_requires = \
['archi>=0.1.1,<0.2.0',
 'beautifulsoup4>=4.4.0',
 'guessit==3.1.0',
 'requests>=2.0']

entry_points = \
{'console_scripts': ['getsubtitle = getsubtitle.main: main']}

setup_kwargs = {
    'name': 'getsubtitle',
    'version': '2019.12.5',
    'description': 'download subtitles easily',
    'long_description': '# getsubtitle\n\n## 下载\n\n`pip install getsubtitle`\n\n## 使用\n\n## 说明\n\n### 搜索规则\n\n`getsubtitle`会抽取视频名中包含的一下信息进行多次组合搜索，直到候选字幕包数达到设定值（默认为 10 条，可以通过 `-n` 参数设定）。\n\n- 美剧名（电影名）\n- 剧集信息（美剧）\n- 年份（电影）\n- 分辨率\n- 视频格式\n- 音频编码格式\n- 压制组信息\n\n如视频名为 `Game.of.Thrones.s07e01.1080p.web.h264-tbs.mkv`， 所有组合如下，按搜索顺序先后排列：\n\n```\nGame of Thrones s07 e01 1080p WEB-DL tbs\nGame of Thrones s07 e01 1080p WEB-DL\nGame of Thrones s07 e01 1080p\nGame of Thrones s07 e01\nGame of Thrones s07\nGame of Thrones\n```\n\n如视频名为 `The.Notebook.2004.720p.BluRay.x264.AC3.3Audio-HDWinG.mkv`， 所有组合如下，按搜索顺序先后排列：\n\n```\nThe Notebook 2004 720p BluRay 3Audio-HDWinG\nThe Notebook 2004 720p BluRay\nThe Notebook 2004 720p\nThe Notebook 2004\nThe NoteBook\n```\n\n**标准视频名**：\n\n全英文组成，包含美剧名（电影名）， 分辨率， 视频格式， 音频编码格式， 压制组等信息。\n\n如： `Game.of.Thrones.s07e01.1080p.web.h264-tbs.mkv` ， `T2_ Trainspotting (1080p HD).mp4`\n\n**其余视频名**：\n\n其余一般为包含了中文的视频名。\n\n对于包含中文的视频名：\n\n- 若视频名的美剧名（电影名）中中文字数大于英文字数，选取中文作为视频的 title\n- 若视频名的美剧名（电影名）中英文字数大于等于中文字数，选取英文作为视频的 title\n\n其中若名称中英混合，只能作简单过滤中文（英文）字符。\n\n若视频名为 `[SPS辛普森一家字幕组].[丑陋的美国人.第一季].Ugly.Amricans.S01E01.rmvb` 这类， 无法抽取准确的名称。\n\n### 下载来源\n\n关于下载来源，现在首选是从[subhd](http://subhd.com)下载字幕，若搜索结果数太少，会继续搜索[zimuzu](http://www.zimuzu.tv/)、[zimuku](https://www.zimuku.la/)的字幕。\n\n关于下载频率，zimuzu 与 zimuku 目前都没有明显的下载频率限制，拖入一个视频文件夹下载一般不会报错。~~而 subhd 有下载频率限制，一般每次只能下载一两个视频的字幕，之后需要滑动验证码验证。~~\n\n~~若下载出现 unknown error，可能就是下载频率过高，可以等一段时间再试。~~\n',
    'author': 'Wu Haotian',
    'author_email': 'whtsky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/whtsky/getsubtitle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
