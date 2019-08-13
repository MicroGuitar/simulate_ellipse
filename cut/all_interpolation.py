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

def cal_NN_interpolation(sorted_curve, NN_index_left, curve_left, NN_index_right, curve_right):
    flag = float(0.0)
    new_pt_list = []
    for i in range(0, NN_index_left,4):
        if flag < 100:
            rate = float(flag / 100.0)
            pt1 = sorted_curve[i]
            pt2 = get_NN(curve_left, pt1)
            new_pt = pt1 * rate + pt2 * (1 - rate)
            new_pt_list.append(new_pt)
            flag = flag + 1
        else:
            break
    flag = float(0.0)
    # new_pt_list2 = []
    for i in range(NN_index_right, sorted_curve.shape[0],4):
        if flag < 100:
            rate = float(flag / 100.0)
            pt1 = sorted_curve[i]
            pt2 = get_NN(curve_right, pt1)
            new_pt = pt1 * (1-rate) + pt2 * rate
            new_pt_list.append(new_pt)
            flag = flag + 1
        else:
            break
    return new_pt_list

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

# find endpoint
y1_min = y1_axis.min()
pt1_down_index = np.argwhere(y1_axis == y1_min)[0][0]
point_1_down = curve1[pt1_down_index]
y1_max = y1_axis.max()
pt1_up_index = np.argwhere(y1_axis == y1_max)[0][0]
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


# print curve4
# print curve4[np.lexsort(curve4[:, ::-1].T)]
sort_curve3 = curve3[np.lexsort(curve4[:, ::-1].T)]
sort_curve4 = curve4[np.lexsort(curve4[:, ::-1].T)]
print 'start4:', sort_curve4[0]
print 'end4:', sort_curve4[sort_curve4.shape[0]-1]
print 'shape4:', sort_curve4.shape

print 'start3:', sort_curve3[0]
print 'end3:', sort_curve3[sort_curve3.shape[0]-1]
print 'shape3:', sort_curve3.shape
# print sort_curve3

# sort_x1_axis = sort_curve1[:, 0]
# sort_y1_axis = sort_curve1[:, 1]
# sort_x2_axis = sort_curve2[:, 0]
# sort_y2_axis = sort_curve2[:, 1]
sort_x3_axis = sort_curve3[:, 0]
# sort_y3_axis = sort_curve3[:, 1]
sort_x4_axis = sort_curve4[:, 0]
# sort_y4_axis = sort_curve4[:, 1]
NN_index_1_4 = np.argwhere(sort_x4_axis == pt1_down_NN[0])[0][0]
NN_index_2_4 = np.argwhere(sort_x4_axis == pt2_down_NN[0])[0][0]
NN_index_1_3 = np.argwhere(sort_x3_axis == pt1_up_NN[0])[0][0]
NN_index_2_3 = np.argwhere(sort_x3_axis == pt2_up_NN[0])[0][0]
pt_list_down = cal_NN_interpolation(sort_curve4, NN_index_1_4, curve1, NN_index_2_4, curve2)
print len(pt_list_down)
pt_list_up = cal_NN_interpolation(sort_curve3, NN_index_1_3, curve1, NN_index_2_3, curve2)
print len(pt_list_up)
# flag = 0.0
# new_1_4 = []
# for i in range(0, NN_index_1_4, 4):
#     if flag < 100:
#         rate = float(flag / 100.0)
#         pt1 = sort_curve4[i]
#         pt2 = get_NN(curve1, pt1)
#         new_pt = pt1*rate + pt2*(1 - rate)
#         # print 'pt1:', pt1
#         # print 'pt2:', pt2
#         # print 'new_pt:', new_pt
#         # print rate
#         # print '----------------'
#         new_1_4.append(new_pt)
#         flag = flag + 1
#     else:
#         break
# print len(new_1_4)
# with open('all_interpolation.txt', 'w') as f:
#     for pt in curve1:
#         # if pt[0] < pt4_left_NN[0] or pt[0] < pt3_left_NN[0]:
#         out_coord = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
#         f.write(out_coord)
#         f.write('\n')
#     for pt in curve4:
#         # if pt[0] > pt1_down_NN[0] and pt[0] < pt2_down_NN[0]:
#         out_coord = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
#         f.write(out_coord)
#         f.write('\n')
#     for pt in new_1_4:
#         out_put = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
#         print out_put
#         f.write(out_put)
#         f.write('\n')

with open('all_interpolation.txt', 'w') as f:
    for pt in curve1:
        if pt[0] < pt4_left_NN[0] or pt[0] < pt3_left_NN[0]:
        # if pt[1] > pt4_left_NN[1]:
            out_coord = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
            f.write(out_coord)
            f.write('\n')

    for pt in curve4:
        if pt[0] > pt1_down_NN[0] and pt[0] < pt2_down_NN[0]:
            out_coord = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
            f.write(out_coord)
            f.write('\n')

    for pt in curve3:
        if pt[0] > pt1_up_NN[0] and pt[0] < pt2_up_NN[0]:
            out_coord = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
            f.write(out_coord)
            f.write('\n')

    for pt in curve2:
        if pt[1] > pt4_right_NN[1] and pt[1] < pt3_right_NN[1]:
        # if pt[1] > pt4_right_NN[1]:
            out_coord = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
            f.write(out_coord)
            f.write('\n')

    for pt in pt_list_down:
        out_put = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
        # print out_put
        f.write(out_put)
        f.write('\n')

    for pt in pt_list_up:
        out_put = str(pt[0]) + ' ' + str(pt[1]) + ' ' + str(pt[2])
        # print out_put
        f.write(out_put)
        f.write('\n')