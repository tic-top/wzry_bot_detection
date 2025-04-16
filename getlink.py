import requests

def get_battle_detail(gameSeq, gameSvr, relaySvr, battleType):
    # 构造URL
    url = f"https://camp.honorofkings.com/h5/app/index.html?gameSeq={gameSeq}&gameSvr={gameSvr}&relaySvr={relaySvr}&battleType={battleType}"
    
    # 发送HTTP GET请求
    response = requests.get(url)
    
    # 检查响应状态码是否为200（成功）
    if response.status_code == 200:
        try:
            # 将响应内容解析为JSON格式
            json_data = response.json()
            return json_data
        except ValueError:
            return "Response is not in JSON format"
    else:
        return f"Failed to get data, status code: {response.status_code}"

# 使用函数，传入适当的参数
gameSeq = 1729661697
gameSvr = 102813
relaySvr = 1779893784
battleType = 16

data = get_battle_detail(gameSeq, gameSvr, relaySvr, battleType)
print(data)
