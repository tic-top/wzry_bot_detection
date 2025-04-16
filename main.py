import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='处理 battle.json 文件')
    parser.add_argument(
        '--path',
        type=str,
        default='data/battle.json',
        help='JSON 文件的路径（默认：data/battle.json）'
    )
    
    # 解析命令行参数
    args = parser.parse_args()
    path = args.path
    
    with open(path, encoding='utf-8', errors='replace') as json_file:
        battle_info = json.load(json_file)
    def simplify(info):
        return {
            "roleName": info['roleName'],
            "roleIcon": info['roleIcon'],
            # 'isGameAuth': info['isGameAuth'],
        }

    redroles = []
    blueroles = []
    for i in range(0, 5):
        redroles.append(battle_info['data']['redRoles'][i]['basicInfo'])
        blueroles.append(battle_info['data']['blueRoles'][i]['basicInfo'])
    redroles, blueroles = list(map(simplify, redroles)), list(map(simplify, blueroles))
    redrobot, bluerobot = 0, 0
    for role in redroles:
        # https://ogdb-cdn.intlgame.cn/draw/a/241901_524600421.png
        # http://i.gtimg.cn/club/item/face/img/5/14555_100.png
        # https://res.sgameglobal.com/Global/AI_Image/FakeAI_Image/
        if 'AI_Image/FakeAI_Image/' in role['roleIcon']:
            redrobot += 1
    for role in blueroles:
        if 'AI_Image/FakeAI_Image/' in role['roleIcon']:
            bluerobot += 1

    # print(redrobot, bluerobot)
    print("###################      redrole:     ################### ")
    for role in redroles:
        print(role)
    print("###################      bluerole:    ################### ")
    for role in blueroles:
        print(role)
