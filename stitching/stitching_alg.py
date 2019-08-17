import open3d
import numpy as np
import os
import time

def get_NN(curve, point_find_NN):
    '''
    find point's Nearest Neighbor on curve
    :param curve: Type: np.ndarray
    :param point_find_NN: Shape: 1x3
    :return: point's Nearest Neighbor
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

def cal_distance(endpoint_1, endpoint_2):
    diff = endpoint_1 - endpoint_2
    distance = np.sqrt(sum(np.square(diff)))
    return distance

def cal_NN(curve_target, edpt1, edpt2):
    '''
    One curve has two end-points.
    Each end-points has its own Nearest Neighbor on the target curve.
    The closer pair of points is what we need.
    :param curve_target: target curve. Type: np.ndarray
    :param edpt1: end-point of curve. Shape: 3x1
    :param edpt2: end-point of curve. Shape: 3x1
    :return:
    '''
    NN_edpt1 = get_NN(curve_target, edpt1)
    NN_edpt2 = get_NN(curve_target, edpt2)
    distance1 = cal_distance(NN_edpt1, edpt1)
    distance2 = cal_distance(NN_edpt2, edpt2)
    if distance1 > distance2:
        NN = NN_edpt2
        pt = edpt2
    else:
        NN = NN_edpt1
        pt = edpt1

    return pt, NN

def fuse2curve(curve1, curve2):
    '''
    fuse the overlapping part of 2 curves
    :param curve1: Type: np.ndarray
    :param curve2: Type: np.ndarray
    :return:one continuous curve. Type: np.ndarray
    '''
    pt1_c1 = curve1[0]
    pt2_c1 = curve1[-1]
    curve1_endpoint, curve1_edpt_NN_in_curve2 = cal_NN(curve_target=curve2, edpt1=pt1_c1, edpt2=pt2_c1)
    curve1_endpoint_index = np.argwhere(curve1_endpoint[0] == curve1[:, 0])[0][0]
    curve1_edpt_NN_in_curve2_index = np.argwhere(curve1_edpt_NN_in_curve2[0] == curve2[:, 0])[0][0]

    pt1_c2 = curve2[0]
    pt2_c2 = curve2[-1]
    curve2_endpoint, curve2_edpt_NN_in_curve1 = cal_NN(curve_target=curve1, edpt1=pt1_c2, edpt2=pt2_c2)
    curve2_endpoint_index = np.argwhere(curve2_endpoint[0] == curve2[:, 0])[0][0]
    curve2_edpt_NN_in_curve1_index = np.argwhere(curve2_edpt_NN_in_curve1[0] == curve1[:, 0])[0][0]

    NN_intepolation = []
    for i, pt in enumerate(curve1[curve1_endpoint_index:curve2_edpt_NN_in_curve1_index]):
        rate = float(i) / float(curve2_edpt_NN_in_curve1_index + 1 - curve1_endpoint_index)
        NN_inter = get_NN(curve=curve2, point_find_NN=pt)
        interpolation = NN_inter * (1 - rate) + pt * rate
        NN_intepolation.append(interpolation)

    NN_intepolation = np.array(NN_intepolation)

    keep1 = curve1[curve2_edpt_NN_in_curve1_index :]
    keep2 = curve2[0:curve1_edpt_NN_in_curve2_index]
    fusion_result = np.vstack((keep2, NN_intepolation))
    fusion_result = np.vstack((fusion_result, keep1))

    return fusion_result

def closed_loop(curve):
    '''
    merge the head and the end of the curve
    :param curve: Type: np.ndarray
    :return: one continuous closed curve. Type: np.ndarray
    '''
    half_index = int((curve.shape[0]) / 2)
    start = curve[0]
    end = curve[-1]

    start_NN = get_NN(curve[half_index:], start)
    end_NN = get_NN(curve[:half_index], end)

    start_NN_index = np.argwhere(start_NN[0] == curve[:, 0])[0][0]
    end_NN_index = np.argwhere(end_NN[0] == curve[:, 0])[0][0]

    final_intepolation = []
    for i, pt in enumerate(curve[start_NN_index:]):
        rate = float(i) / float(curve.shape[0] - 1 - start_NN_index)
        temp_NN_inter = get_NN(curve=curve[0:end_NN_index], point_find_NN=pt)
        temp = temp_NN_inter * rate + pt * (1 - rate)
        final_intepolation.append(temp)

    fusion_result = np.vstack((final_intepolation, curve[end_NN_index: start_NN_index]))

    return fusion_result

def loadData(path):
    Data = []
    path_list = os.listdir(path)
    path_list.sort(key= lambda name_str: int(name_str[name_str.find('_')+4 : name_str.rfind('_')-2]))
    for pcd_name in path_list:
        path_name = path + pcd_name
        # print(path_name)
        pcd = open3d.io.read_point_cloud(path_name)
        temp_curve = np.array(pcd.points)
        Data.append(temp_curve)
    Data = np.array(Data)

    return Data

def main():
    pcd_data = loadData('/home/pi/work_RR/stitching/pointclouds/')
    fusion = pcd_data[0]
    for i in range(pcd_data.shape[0]):
        if i < pcd_data.shape[0] - 1:
            fusion = fuse2curve(fusion, pcd_data[i+1])
    result = closed_loop(fusion)

    result_pcd = open3d.geometry.PointCloud()
    result_pcd.points = open3d.utility.Vector3dVector(result)
    open3d.visualization.draw_geometries([result_pcd])
    open3d.io.write_point_cloud('fusion_result.pcd', result_pcd)

if __name__ == '__main__':
    main()
