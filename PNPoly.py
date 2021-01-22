from typing import List

# PNPoly算法


def if_points_in_polygon(x: float, y: float, cdump: float, verts: List[tuple]) -> float:
    # 检验xy是否为浮点数
    try:
        x, y = float(x), float(y)
    except:
        return 'input error!!!'
    vertx = [xyvert[0] for xyvert in verts]
    verty = [xyvert[1] for xyvert in verts]

    # 此部分移至预处理，仅选择外包四边形范围内点进行判断
    # # 如果点位不在横纵坐标最大值规定的四边形内，则直接返回False
    # if not verts or not min(vertx) <= x <= max(vertx) or not min(verty) <= y <= max(verty):
    #     return 0

    # 核心算法部分
    num_verts = len(verts)
    if_in = False

    for i in range(num_verts):
        j = num_verts - 1 if i == 0 else i-1
        if ((verty[i] > y)) != ((verty[j]) > y) and (x < (vertx[j]-vertx[i])*(y-verty[i])/(verty[j]-verty[i])+vertx[i]):
            if_in = not if_in

    if if_in == True:
        return cdump
    else:
        return 0


if __name__ == "__main__":
    boundary = [(1, 1), (1, 3), (2, 4), (5, 1)]
    x = 1.1
    y = 2
    cdump = 777
    print(if_points_in_polygon(x, y, cdump, boundary))
