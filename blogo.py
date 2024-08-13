# Blogging isn't really my forte, but I can sure write one at something related to my forte! - VintellX

import json

def load_blogs():
    with open('static/assets/blogs/blogs.json') as json_file:
        data = json.load(json_file)
    return data

def tags_count():
    blogs = load_blogs()
    MyBigDic = {}
    for blog in blogs:
        for tagItem in blog['info']['tags']:
            if tagItem in MyBigDic:
                MyBigDic[tagItem] += 1
            else:
                MyBigDic[tagItem] = 1
    return MyBigDic
