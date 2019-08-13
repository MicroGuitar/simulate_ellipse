import toolbox. vgl as vgl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

pose1 = [200, 0, 0, 0, 90, 0] # y aix 90
pose2 = [-200, 0, 0, 0, -90, 0] # y aix -90
pose3 = [0, 200, 0, -90, 0, 0] # x aix -90
pose4 = [0, -200, 0, 90, 0, 0] # x aix 90

Tc1w = vgl.Pose2T(pose1)
Twc1 = np.linalg.inv(Tc1w)
Tc2w = vgl.Pose2T(pose2)
Twc2 = np.linalg.inv(Tc2w)
Tc3w = vgl.Pose2T(pose3)
Twc3 = np.linalg.inv(Tc3w)
Tc4w = vgl.Pose2T(pose4)
Twc4 = np.linalg.inv(Tc4w)

gt_pts = np.loadtxt('point_xyz.txt')

noise1 = np.array([random.random()*2-1, random.random()*2-1, random.random()*2-1, \
                   random.random(), random.random(), random.random()], dtype=np.float)
noise2 = np.array([random.random()*2-1, random.random()*2-1, random.random()*2-1, \
                   random.random(), random.random(), random.random()], dtype=np.float)
noise3 = np.array([random.random()*2-1, random.random()*2-1, random.random()*2-1, \
                   random.random(), random.random(), random.random()], dtype=np.float)
noise4 = np.array([random.random()*2-1, random.random()*2-1, random.random()*2-1, \
                   random.random(), random.random(), random.random()], dtype=np.float)

pose1 = np.array(pose1, dtype=np.float)
pose1_noise = pose1 + noise1
pose2_noise = pose2 + noise2
pose3_noise = pose3 + noise3
pose4_noise = pose4 + noise4
point_det_w1 = []
point_det_w2 = []
point_det_w3 = []
point_det_w4 = []
for point in gt_pts:
    print point[1]
    if point[0] < -10:
        point = point.reshape((3, 1))
        pt_w_homo = vgl.Homo(point)
        pt_c_homo = np.dot(Twc1, pt_w_homo)
        Tc1w_noise = vgl.Pose2T(pose1_noise)
        pt_w_det = np.dot(Tc1w_noise, pt_c_homo)
        pt_w_det = vgl.unHomo(pt_w_det)
        point_det_w1.append(pt_w_det)
    elif point[0] > 10:
        point = point.reshape((3, 1))
        pt_w_homo = vgl.Homo(point)
        pt_c_homo = np.dot(Twc2, pt_w_homo)
        Tc2w_noise = vgl.Pose2T(pose2_noise)
        pt_w_det = np.dot(Tc2w_noise, pt_c_homo)
        pt_w_det = vgl.unHomo(pt_w_det)
        point_det_w2.append(pt_w_det)
    if point[1] > 5:
        point = point.reshape((3, 1))
        pt_w_homo = vgl.Homo(point)
        pt_c_homo = np.dot(Twc3, pt_w_homo)
        Tc3w_noise = vgl.Pose2T(pose3_noise)
        pt_w_det = np.dot(Tc3w_noise, pt_c_homo)
        pt_w_det = vgl.unHomo(pt_w_det)
        point_det_w3.append(pt_w_det)
    elif point[1] < -5:
        point = point.reshape((3, 1))
        pt_w_homo = vgl.Homo(point)
        pt_c_homo = np.dot(Twc4, pt_w_homo)
        Tc4w_noise = vgl.Pose2T(pose4_noise)
        pt_w_det = np.dot(Tc4w_noise, pt_c_homo)
        pt_w_det = vgl.unHomo(pt_w_det)
        point_det_w4.append(pt_w_det)

print point_det_w4

x1 = []
y1 = []
z1 = []
for pt_det in point_det_w1:
    x1.append(pt_det[0])
    y1.append(pt_det[1])
    z1.append(pt_det[2])

x2 = []
y2 = []
z2 = []
for pt_det in point_det_w2:
    x2.append(pt_det[0])
    y2.append(pt_det[1])
    z2.append(pt_det[2])

x3 = []
y3 = []
z3 = []
for pt_det in point_det_w3:
    x3.append(pt_det[0])
    y3.append(pt_det[1])
    z3.append(pt_det[2])

x4 = []
y4 = []
z4 = []
for pt_det in point_det_w4:
    x4.append(pt_det[0])
    y4.append(pt_det[1])
    z4.append(pt_det[2])
# print x
gt_x = []
gt_y = []
gt_z = []
# print gt_pts[0][0]
for gt in gt_pts:
    gt_x.append(gt[0])
    gt_y.append(gt[1])
    gt_z.append(gt[2])

fig1 = plt.figure()
ax1 = Axes3D(fig1)
ax1.scatter(x1, y1, z1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
fig2 = plt.figure()
ax2 = Axes3D(fig2)
ax2.scatter(x2, y2, z2)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
fig3 = plt.figure()
ax3 = Axes3D(fig3)
ax3.scatter(x3, y3, z3)
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
fig4 = plt.figure()
ax4 = Axes3D(fig4)
ax4.scatter(x4, y4, z4)
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('z')
# plt.show()
figgt = plt.figure()
bx = Axes3D(figgt)
bx.scatter(gt_x, gt_y, gt_z)
bx.set_xlabel('x')
bx.set_ylabel('y')
bx.set_zlabel('z')
plt.show()

zero = np.array([0], dtype=np.float32)

with open('point1_xyz.txt', 'w') as f:
    for i in range(len(point_det_w1)):
        out = str(point_det_w1[i][0][0]) + ' ' + str(point_det_w1[i][1][0]) + ' ' + str(point_det_w1[i][2][0])
        # print out
        f.write(out)
        f.write('\n')

with open('point2_xyz.txt', 'w') as f:
    for i in range(len(point_det_w2)):
        out = str(point_det_w2[i][0][0]) + ' ' + str(point_det_w2[i][1][0]) + ' ' + str(point_det_w2[i][2][0])
        # print out
        f.write(out)
        f.write('\n')

with open('point3_xyz.txt', 'w') as f:
    for i in range(len(point_det_w3)):
        out = str(point_det_w3[i][0][0]) + ' ' + str(point_det_w3[i][1][0]) + ' ' + str(point_det_w3[i][2][0])
        # print out
        f.write(out)
        f.write('\n')

with open('point4_xyz.txt', 'w') as f:
    for i in range(len(point_det_w4)):
        out = str(point_det_w4[i][0][0]) + ' ' + str(point_det_w4[i][1][0]) + ' ' + str(point_det_w4[i][2][0])
        # print out
        f.write(out)
        f.write('\n')

with open('merge.txt', 'w') as f:
    for i in range(len(point_det_w1)):
        out = str(point_det_w1[i][0][0]) + ' ' + str(point_det_w1[i][1][0]) + ' ' + str(point_det_w1[i][2][0])
        # print out
        f.write(out)
        f.write('\n')
    for i in range(len(point_det_w2)):
        out = str(point_det_w2[i][0][0]) + ' ' + str(point_det_w2[i][1][0]) + ' ' + str(point_det_w2[i][2][0])
        # print out
        f.write(out)
        f.write('\n')
    for i in range(len(point_det_w3)):
        out = str(point_det_w3[i][0][0]) + ' ' + str(point_det_w3[i][1][0]) + ' ' + str(point_det_w3[i][2][0])
        # print out
        f.write(out)
        f.write('\n')
    for i in range(len(point_det_w4)):
        out = str(point_det_w4[i][0][0]) + ' ' + str(point_det_w4[i][1][0]) + ' ' + str(point_det_w4[i][2][0])
        # print out
        f.write(out)
        f.write('\n')

print len(point_det_w1)
print len(point_det_w2)
print len(point_det_w3)
print len(point_det_w4)