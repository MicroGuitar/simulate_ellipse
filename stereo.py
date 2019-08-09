import toolbox.vgl as vgl
import numpy as np

# fx = 3000
# fy = 3000
# cx = 1920
# cy = 960

# intrinsic = np.zeros((3, 3), dtype=np.float32)
# intrinsic[0][0] = fx
# intrinsic[1][1] = fy
# intrinsic[2][2] = 1.0
# intrinsic[0][2] = cx
# intrinsic[1][2] = cy

# print intrinsic
pose1 = [200, 0, 0, 0, 90, 0] # y aix 90
pose2 = [-200, 0, 0, 0, -90, 0] # y aix -90
pose3 = [0, 200, 0, -90, 0, 0] # x aix -90
pose4 = [0, -200, 0, 90, 0, 0] # x aix 90

Tc1w = vgl.Pose2T(pose1)
print Tc1w
Twc1 = np.linalg.inv(Tc1w)
Tc2w = vgl.Pose2T(pose2)
# E = np.loadtxt('/home/pi/Desktop/Stereo/E.txt')
# F = np.loadtxt('/home/pi/Desktop/Stereo/F.txt')
# pose_c1s = [0, -50, 0, 0, 0, 0]
# Tc1s = vgl.Pose2T(pose_c1s)
# pose_c2s = [0, -50, 0, 0, 0, 0]
# Tc2s = vgl.Pose2T(pose_c2s)
# stereoc1 = vgl.stereo_vision.StereoVision(intrinsic,intrinsic,(), (), Tc1s, E, F)

gt_pts = np.loadtxt('point_xyz.txt')
# pt_www = []
# for pt in gt_pts:
#     pt_w = pt.reshape(3,1)
#     pt_w = vgl.Homo(pt_w)
#     pt_c11 = np.dot(Twc1, pt_w)
#     pt_c11 = vgl.unHomo(pt_c11)
#     pt_c12 = vgl.projectPts(pt_c11, Tc1s)
#     pt_c11_2d = stereoc1.projectPts(pt_c11, flag=stereoc1.CAM_A)
#     pt_c12_2d = stereoc1.projectPts(pt_c12, flag=stereoc1.CAM_B)
#     det_pt_3d_c1 = stereoc1.get3dPts(pt_c11_2d, pt_c12_2d)
#     print det_pt_3d_c1
#     pt_www.append(det_pt_3d_c1)
#     # add noise
#     print '****************'
#     print det_pt_3d_c1[0] # point in cam coordinate
#     print pt_c11
#     print '****************'
#
#     print 'c11:', pt_c11_2d.shape
#     print 'c12:', pt_c12_2d.shape
#     print '--------------------'


# print pt_www[0][0]
