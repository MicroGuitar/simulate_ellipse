import numpy as np


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

y3_min = y3_axis.min()
pt3_down_index = np.argwhere(y3_axis == y3_min)[0][0]
point_3_down = curve3[pt3_down_index]

# x3_min = x3_axis.min()
# pt3_left_index = np.argwhere(x3_axis == x3_min)[0][0]
# point_3_left = curve3[pt3_left_index]

# curve4 left point and right point
x4_min = x4_axis.min()
pt4_left_index = np.argwhere(x4_axis == x4_min)[0][0]
point_4_left = curve4[pt4_left_index]
x4_max = x4_axis.max()
pt4_right_index = np.argwhere(x4_axis == x4_max)[0][0]
point_4_right = curve4[pt4_right_index]
# NN
d1 = []
for pt4 in curve4:
    diff_square = np.square(pt4 - point_1_down)
    # print diff_square
    distance = np.sqrt(sum(diff_square))
    # print distance
    d1.append(distance)

d1 = np.array(d1)
d1_index = np.argwhere(d1 == d1.min())[0][0]
pt1_down_NN = curve4[d1_index]

# NN
d2 = []
for pt1 in curve1:
    diff_square = np.square(pt1 - point_4_left)
    distance = np.sqrt(sum(diff_square))
    d2.append(distance)

d2 = np.array(d2)
d2_index = np.argwhere(d2 == d2.min())[0][0]
pt4_left_NN = curve1[d2_index]

# NN
d3 = []
for pt3 in curve3:
    diff_square = np.square(pt3 - point_4_right)
    distance = np.sqrt(sum(diff_square))
    d3.append(distance)

d3 = np.array(d3)
d3_index = np.argwhere(d3 == d3.min())[0][0]
pt4_right_NN = curve3[d3_index]

# d4 = []
# for pt4 in curve4:
#     diff_square = np.square(pt4 - point_3_down)
#     distance = np.sqrt(sum(diff_square))
#     d3.append(distance)
#
# d3 = np.array(d3)
# d3_index = np.argwhere(d3 == d3.min())[0][0]
# pt4_right_NN = curve3[d3_index]


# print 'pt1', point_1_down
# print 'pt1\'s NN', pt1_down_NN
# print 'pt4', point_4_left
# print 'pt4\'s NN', pt4_left_NN
#

with open('new_curve1.txt', 'w') as f1:
    for point in curve1:
        if point[0] < pt4_left_NN[0] or point[1] > pt4_left_NN[1]:
            out_coord = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
            f1.write(out_coord)
            f1.write('\n')

with open('new_curve4.txt', 'w') as f2:
    for point in curve4:
        if point[0] > pt1_down_NN[0]:
            out_coord = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
            f2.write(out_coord)
            f2.write('\n')

with open('merge.txt', 'w') as f:
    for point in curve1:
        if point[0] < pt4_left_NN[0] or point[1] > pt4_left_NN[1]:
            out_coord = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
            f.write(out_coord)
            f.write('\n')

    for point in curve4:
        if point[0] > pt1_down_NN[0]:
            out_coord = str(point[0]) + ' ' + str(point[1]) + ' ' + str(point[2])
            f.write(out_coord)
            f.write('\n')

