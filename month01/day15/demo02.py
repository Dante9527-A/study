"""
    模块变量
"""
# 1. 存储的是模块文档字符串
# 适用性:在交互式python中,查看某个模块的使用方式
print(__doc__)

# 2. 存储的是模块名称
# 被导入时:真实模块名
# 作为主模块时:__main__
print(__name__)
import module01
