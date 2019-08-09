import numpy as np

def get_NN(curve, point_find_NN):
    '''

    :param curve: the point finds NN on this curve
    :param point_find_NN:
    :return: point's NN on curve
    '''
    dist_list = []
    for pt in curve:
        diff_square = np.square(pt - point_find_NN)
        distance = np.square(sum((diff_square)))
        dist_list.append(distance)
    dist_array = np.array(dist_list)
    coord_index = np.argwhere(dist_array == dist_array.min())[0][0]
    NN = curve[coord_index]
    return NN


curve1 = np.loadtxt('curve1.txt')
curve2 = np.loadtxt('curve2.txt')
curve3 = np.loadtxt('curve3.txt')
curve4 = np.loadtxt('curve4.txt')

x1_axis = curve1[:, 0]
y1_axis = curve1[:, 1]
x2_axis = curve2[:, 0]
y2_axis = curve2[:, 1]
x3_axis = curve3[:, 0]
y3_axis = curve3[:, 1]
x4_axis = curve4[:, 0]
y4_axis = curve4[:, 1]

y1_min = y1_axis.min()
pt1_down_index = np.argwhere(y1_axis == y1_min)[0][0]
point_1_down = curve1[pt1_down_index]
y1_max = y1_axis.max()
pt1_up_index = np.argwhere(y1_axis == y1_min)[0][0]
point_1_up = curve1[pt1_up_index]

y2_min = y2_axis.min()
pt2_down_index = np.argwhere(y2_axis == y2_min)[0][0]
point_2_down = curve2[pt2_down_index]
y2_max = y2_axis.max()
pt2_up_index = np.argwhere(y2_axis == y2_max)[0][0]
point_2_up = curve2[pt2_up_index]

x3_min = x3_axis.min()
pt3_left_index = np.argwhere(x3_axis == x3_min)[0][0]
point_3_left = curve3[pt3_left_index]
x3_max = x3_axis.max()
pt3_right_index = np.argwhere(x3_axis == x3_max)[0][0]
point_3_right = curve3[pt3_right_index]

# curve4 left point and right point
x4_min = x4_axis.min()
pt4_left_index = np.argwhere(x4_axis == x4_min)[0][0]
point_4_left = curve4[pt4_left_index]
x4_max = x4_axis.max()
pt4_right_index = np.argwhere(x4_axis == x4_max)[0][0]
point_4_right = curve4[pt4_right_index]
#*********************NN*******************************#

pt1_down_NN = get_NN(curve4, point_1_down)

pt1_up_NN = get_NN(curve3, point_1_up)

pt4_left_NN = get_NN(curve1, point_4_left)

pt4_right_NN = get_NN(curve2, point_4_right)

pt2_down_NN = get_NN(curve4, point_2_down)

pt2_up_NN = get_NN(curve3, point_2_up)

pt3_left_NN = get_NN(curve1, point_3_left)

pt3_right_NN = get_NN(curve2, point_3_right)
#---------------------NN-----------------------#

#***********************************************************#

