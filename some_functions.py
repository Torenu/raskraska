BORDER1 = [[-5, 0.15, -5, 3.5],
           [-5, 3.5, -0.5, 3.5],
           [-0.5, 3.5, -0.5, 0.15],
           [-0.5, 0.15, -5, 0.15]]

BORDER2 = [[-5, -3.5, -5, -0.15],
           [-5, -0.15, -0.5, -0.15],
           [-0.5, -0.15, -0.5, -3.5],
           [-0.5, -3.5, -5, -3.5]]

BORDER3 = [[0.5, -1.675, 0.5, 1.675],
           [0.5, 1.675, 5, 1.675],
           [5, 1.675, 5, -1.675],
           [5, -1.675, 0.5, -1.675]]

BORDER4 = [[-5, -1.675, -5, 1.675],
           [-5, 1.675, -0.5, 1.675],
           [-0.5, 1.675, -0.5, -1.675],
           [-0.5, -1.675, -5, -1.675]]

BORDER5 = [[-5, -3.6, -5, 2.4],
           [-5, 2.4, 5, 2.4],
           [5, 2.4, 5, -3.6],
           [5, -3.6, -5, -3.6]]

LC = [[-5, 0.5, -0.5, 3],
      [-3, -3.5, -2, -0.15],
      [-5, -2, -0.5, -1],
      [1.3, -1.675, 2.3, 1.675],
      [0.5, -1.2, 5, 0.2],
      [0.5, 1.4, 5, -0.8],
      [-3, -1.675, -2, 1.675],
      [-5, -0.175, -0.5, 0.825],
      [0.5, 0, 2.75, 1.675],
      [2.75, -1.675, 5, 0],
      [-5, 1.825, -2.75, 3.5],
      [-5, 0.15, -0.5, 3.5],
      [-2.75, 0.15, -0.5, 1.825],
      [-5, -1.825, -2.4, -0.15],
      [-3, -3.5, -0.5, -1.825],
      [-3.7, -0.15, -1.9, -3.5],
      [2.7, 1.675, 2.8, -1.675],
      [0.5, 0.8, 5, -0.8],
      [0.5, -1.3, 5, 1.3],
      [-2.4, 2.4, 2.7, -3.6],
      [-5, 2.1, 5, -0.8],
      [-5, -3.5, 5, 0.3],
      [-5, -0.5, 5, 1],
      [-1, -3.6, 1, 2.4],
      [-3, -3.6, 0, 2.4],
      [-2, 2.4, -0.5, -3.6],
      [1, -3.6, 4, 2.4],
      [-5, 1, 5, -0.5]]


def get_ic(l1, l2):
    # y1 = s1[1] + (x-s1[0]) * k1
    # y2 = s2[1] + (x-s2[0]) * k2
    s1 = l1[0:2]
    e1 = l1[2:4]
    s2 = l2[0:2]
    e2 = l2[2:4]
    if e1[0] == s1[0]:
        x = e1[0]
        k2 = (e2[1] - s2[1]) / (e2[0] - s2[0])
        y = s2[1] + (x-s2[0])*k2
    elif e2[0] == s2[0]:
        x = e2[0]
        k1 = (e1[1] - s1[1]) / (e1[0] - s1[0])
        y = s1[1] + (x -s1[0])*k1
    else:
        k1 = (e1[1]-s1[1])/(e1[0]-s1[0])
        k2 = (e2[1]-s2[1])/(e2[0]-s2[0])
        b2 = s2[1]
        a2 = s2[0]
        b1 = s1[1]
        a1 = s1[0]
        x = (b2 - a2*k2 - b1 + a1*k1) / (k1 - k2)
        y = s1[1] + (x-s1[0]) * k1
    return [x, y, 0]

