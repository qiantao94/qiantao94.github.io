# -*- coding: utf-8 -*-
"""blog config
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "qiantao94/qiantao94.github.io@main"
}

# 站点设置
site_name = "QianTao"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "qian.tao"
email = "qiantao94@gmail.com"
author_homepage = "https://www.imalan.cn"
description = "------------------"
key_words = ['Maverick', 'qiantao', 'Galileo', 'blog']
language = 'en-US'
external_links = [
    # {
    #     "name": "Maverick",
    #     "url": "https://github.com/AlanDecode/Maverick",
    #     "brief": "🏄‍ Go My Own Way."
    # },
    # {
    #     "name": "三無計劃",
    #     "url": "https://www.imalan.cn",
    #     "brief": "熊猫小A的主页。"
    # }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    # {
    #     "name": "Twitter",
    #     "url": "https://twitter.com/AlanDecode",
    #     "icon": "gi gi-twitter"
    # },
    {
        "name": "GitHub",
        "url": "https://github.com/qiantao94",
        "icon": "gi gi-github"
    },
    # {
    #     "name": "Weibo",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-weibo"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
