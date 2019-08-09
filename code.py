def toParameters(self):
    """
    根据椭圆一般方程，得到椭圆圆心、长短轴和旋转角度

    .. image:: ../material/core/common/datatype/EllipseCanonicalForm.png

    Returns
    ----------
    c_x : float
            圆心横坐标
    c_y : float
            圆心纵坐标
    f_a : float
            长轴长度
    f_b : float
            短轴长度
    theta : float
            旋转角度，单位是degree

    References
    ----------
    https://en.wikipedia.org/wiki/Ellipse
    """
    temp_0 = self.B**2 - 4*self.A*self.C
    temp_1 = self.A*self.E**2 + self.C*self.D**2-self.B*self.D*self.E+temp_0*self.F
    temp_2 = ((self.A-self.C)**2 + self.B**2)**0.5
    temp_3 = self.A + self.C + temp_2
    temp_4 = self.A + self.C - temp_2
    f_a = -(2 * temp_1 * temp_3)**0.5 / temp_0
    f_b = -(2 * temp_1 * temp_4)**0.5 / temp_0

    c_x = (2*self.C*self.D-self.B*self.E)/temp_0
    c_y = (2*self.A*self.E-self.B*self.D)/temp_0

    if np.around(self.B, PRECISION) == 0:
        if np.around(self.A, PRECISION) < np.around(self.C, PRECISION):
            theta = 0
        else:
            theta = np.pi / 2
    else:
        theta = np.math.atan((self.C - self.A - temp_2) / self.B)

    return c_x, c_y, f_a, f_b, np.math.degrees(theta)

