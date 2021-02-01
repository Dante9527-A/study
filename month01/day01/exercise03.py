"""
    汇率转换器
"""
# 1.获取数据
usd = input("请输入美元：")
# 2.逻辑处理
cny = float(usd) * 7.0733
# 3.显示结果
print(usd + "美元=" + str(cny) + "人民币")
