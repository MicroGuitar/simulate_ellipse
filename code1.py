def setByParameters(self, centerX, centerY, radiusX, radiusY, rotation_deg):
    """
    通过给定的圆心，长轴短轴和旋转角度，得到椭圆的一般方程，一般用于计算

    .. image:: ../material/core/common/datatype/GeneralEllipse.png

    Parameters
    ----------
    centerX : float
            圆心横坐标
    centerY : float
            圆心纵坐标
    radiusX : float
            长轴长度
    radiusY : float
            短轴长度
    rotation_deg : float
            旋转角度，单位是degree

    Returns
    ----------
    None

    References
    ----------
    https://en.wikipedia.org/wiki/Ellipse
    """
    rotate_rad = np.deg2rad(rotation_deg)
    sin_theta = np.sin(rotate_rad)
    cos_theta = np.cos(rotate_rad)

    self.A = radiusX**2 * sin_theta**2 + radiusY**2 * cos_theta**2
    self.B = 2 * (radiusY**2 - radiusX**2) * sin_theta * cos_theta
    self.C = radiusX**2 * cos_theta**2 + radiusY**2 * sin_theta**2
    self.D = -2 * self.A * centerX - self.B * centerY
    self.E = -1 * self.B * centerX -2 * self.C * centerY
    self.F = self.A * centerX**2 + self.B * centerX * centerY \
             + self.C * centerY**2 - radiusX**2 * radiusY**2
