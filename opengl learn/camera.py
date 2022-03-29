from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.GLU import *
from Vector3f import Vector3f
import math, json


def load_machinde():
    path = 'machine.ini'
    init = {'HTM-250M': {'x': 270, 'y': 270, 'z': 315, 'select': True, 'name': 'HTM-250M'}}
    try:
        with open(path, 'r') as (f):
            machines = json.load(f)
            for machine in machines.keys():
                if machines[machine]['select']:
                    return machines[machine]

    except:
        with open(path, 'w') as (f):
            json.dump(init, f, indent=4)

    return init['HTM-250M']


MACHINE = load_machinde()


class camera3d:
    a = []

    def __init__(self):
        self.reinit(MACHINE, 100)
        self.ratio = 0.68

    def reinit(self, machine, unit):
        self.machine = machine
        self.mPos = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2, self.machine['z'] * unit / 2)
        self.mViewCenter = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                    self.machine['z'] * unit / 2 - 1)
        self.mUp = Vector3f(0.0, 1.0, 0.0)
        long_len = math.sqrt(
            self.machine['x'] * self.machine['x'] + self.machine['y'] * self.machine['y'] + self.machine['z'] *
            self.machine['z'])
        self.right = long_len * 0.55 * unit
        self.top = long_len * 0.55 * unit
        self.forwardDir = self.mViewCenter - self.mPos
        self.rithtDir = self.forwardDir.cross(self.mUp)
        self.Pitch(90)
        self.Yaw(-30)
        self.Pitch(-10)

    def change_sight(self, direction=0):
        unit = 100
        if direction == 0:
            self.reinit(self.machine, unit)
        else:
            if direction == 1:
                self.mPos = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                     self.machine['z'] * unit / 2)
                self.mViewCenter = Vector3f(self.machine['x'] * unit / 2 + 1, self.machine['y'] * unit / 2,
                                            self.machine['z'] * unit / 2)
                self.mUp = Vector3f(0.0, 0.0, 1.0)
            else:
                if direction == 2:
                    self.mPos = Vector3f(self.machine['x'] * unit / 2 + 1, self.machine['y'] * unit / 2,
                                         self.machine['z'] * unit / 2)
                    self.mViewCenter = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                                self.machine['z'] * unit / 2)
                    self.mUp = Vector3f(0.0, 0.0, 1.0)
                else:
                    if direction == 3:
                        self.mPos = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                             self.machine['z'] * unit / 2)
                        self.mViewCenter = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2 + 1,
                                                    self.machine['z'] * unit / 2)
                        self.mUp = Vector3f(0.0, 0.0, 1.0)
                    else:
                        if direction == 4:
                            self.mPos = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2 + 1,
                                                 self.machine['z'] * unit / 2)
                            self.mViewCenter = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                                        self.machine['z'] * unit / 2)
                            self.mUp = Vector3f(0.0, 0.0, 1.0)
                        else:
                            if direction == 5:
                                self.mPos = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                                     self.machine['z'] * unit / 2)
                                self.mViewCenter = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                                            self.machine['z'] * unit / 2 + 1)
                                self.mUp = Vector3f(0.0, -1.0, 0.0)
                            else:
                                if direction == 6:
                                    self.mPos = Vector3f(self.machine['x'] * unit / 2, self.machine['y'] * unit / 2,
                                                         self.machine['z'] * unit / 2 + 1)
                                    self.mViewCenter = Vector3f(self.machine['x'] * unit / 2,
                                                                self.machine['y'] * unit / 2,
                                                                self.machine['z'] * unit / 2)
                                    self.mUp = Vector3f(0.0, 1.0, 0.0)
                            long_len = math.sqrt(
                                self.machine['x'] * self.machine['x'] + self.machine['y'] * self.machine['y'] +
                                self.machine['z'] * self.machine['z'])
                            self.right = long_len * 0.55 * unit
                            self.top = long_len * 0.55 * unit
                            self.forwardDir = self.mViewCenter - self.mPos
                            self.rithtDir = self.forwardDir.cross(self.mUp)

    def Update(self):
        """glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glInitNames()
        x,y = (-1,-1)
        gluPickMatrix(x,y,2, 2,glGetIntegerv( GL_VIEWPORT ))

        glSelectBuffer(512,self.a)
        glRenderMode(GL_SELECT)
        glScale(self.ratio,1,1)
        glOrtho(-self.right,self.right,-self.top,self.top,-35000,35000)
        gluLookAt(self.mPos.X,self.mPos.Y,self.mPos.Z,self.mViewCenter.X,self.mViewCenter.Y,self.mViewCenter.Z,self.mUp.X,self.mUp.Y,self.mUp.Z)"""
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glScale(self.ratio, 1, 1)
        glOrtho(-self.right, self.right, -self.top, self.top, -35000, 35000)
        gluLookAt(self.mPos.X, self.mPos.Y, self.mPos.Z, self.mViewCenter.X, self.mViewCenter.Y, self.mViewCenter.Z,
                  self.mUp.X, self.mUp.Y, self.mUp.Z)

    def Move(self, deltax, deltay):
        self.forwardDir.Normalize()
        self.rithtDir.Normalize()
        self.mUp.Normalize()
        dx = self.rithtDir * deltax
        dy = self.mUp * deltay
        self.mPos = self.mPos - dx + dy
        self.mViewCenter = self.mPos + self.forwardDir

    def Rotate(self, viewDirection, angle, x, y, z):
        C = math.cos(angle * math.pi / 180)
        S = math.sin(angle * math.pi / 180)
        newX = viewDirection.X * (x * x + (1 - x * x) * C) + viewDirection.Y * (
                    x * y * (1 - C) - z * S) + viewDirection.Z * (x * z * (1 - C) + y * S)
        newY = viewDirection.X * (x * y * (1 - C) + z * S) + viewDirection.Y * (
                    y * y + (1 - y * y) * C) + viewDirection.Z * (y * z * (1 - C) - x * S)
        newZ = viewDirection.X * (x * z * (1 - C) - y * S) + viewDirection.Y * (
                    y * z * (1 - C) + x * S) + viewDirection.Z * (z * z + (1 - z * z) * C)
        newdir = Vector3f(newX, newY, newZ)
        return newdir

    def Yaw(self, angle):
        self.forwardDir = self.Rotate(self.forwardDir, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.rithtDir = self.Rotate(self.rithtDir, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.mPos = self.mViewCenter - self.forwardDir

    def Pitch(self, angle):
        self.forwardDir = self.Rotate(self.forwardDir, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mUp = self.Rotate(self.mUp, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mPos = self.mViewCenter - self.forwardDir


class camera_axis:

    def __init__(self):
        self.reinit()

    def reinit(self):
        self.mPos = Vector3f(31000, 20000, 1)
        self.mViewCenter = Vector3f(31000, 20000, 0)
        self.mUp = Vector3f(0, 1, 0)
        self.right = 25000
        self.top = 25000
        self.forwardDir = self.mViewCenter - self.mPos
        self.rithtDir = self.forwardDir.cross(self.mUp)
        self.Pitch(90)
        self.Yaw(-30)
        self.Pitch(-10)

    def change_sight(self, direction=0):
        if direction == 0:
            self.reinit()
        else:
            if direction == 1:
                self.mPos = Vector3f(-1, -31000, 20000.0)
                self.mViewCenter = Vector3f(0, -31000.0, 20000.0)
                self.mUp = Vector3f(0, 0, 1)
            else:
                if direction == 2:
                    self.mPos = Vector3f(1, 31000, 20000.0)
                    self.mViewCenter = Vector3f(0, 31000.0, 20000.0)
                    self.mUp = Vector3f(0, 0, 1)
                else:
                    if direction == 3:
                        self.mPos = Vector3f(31000.0, -1, 20000)
                        self.mViewCenter = Vector3f(31000.0, 0, 20000.0)
                        self.mUp = Vector3f(0, 0, 1)
                    else:
                        if direction == 4:
                            self.mPos = Vector3f(-31000, 1, 20000.0)
                            self.mViewCenter = Vector3f(-31000.0, 0, 20000.0)
                            self.mUp = Vector3f(0, 0, 1)
                        else:
                            if direction == 5:
                                self.mPos = Vector3f(31000.0, -21000, -1)
                                self.mViewCenter = Vector3f(31000, -21000, 0)
                                self.mUp = Vector3f(0, -1, 0)
                            else:
                                if direction == 6:
                                    self.mPos = Vector3f(31000, 20000, 1)
                                    self.mViewCenter = Vector3f(31000, 20000, 0)
                                    self.mUp = Vector3f(0, 1, 0)
                            self.right = 25000
                            self.top = 25000
                            self.forwardDir = self.mViewCenter - self.mPos
                            self.rithtDir = self.forwardDir.cross(self.mUp)

    def Update(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glScale(0.68, 1, 1)
        glOrtho(-self.right, self.right, -self.top, self.top, -350000, 350000)
        gluLookAt(self.mPos.X, self.mPos.Y, self.mPos.Z, self.mViewCenter.X, self.mViewCenter.Y, self.mViewCenter.Z,
                  self.mUp.X, self.mUp.Y, self.mUp.Z)

    def Move(self, deltax, deltay):
        self.forwardDir.Normalize()
        self.rithtDir.Normalize()
        self.mUp.Normalize()
        dx = self.rithtDir * deltax
        dy = self.mUp * deltay
        self.mPos = self.mPos - dx + dy
        self.mViewCenter = self.mPos + self.forwardDir

    def Rotate(self, viewDirection, angle, x, y, z):
        C = math.cos(angle * math.pi / 180)
        S = math.sin(angle * math.pi / 180)
        newX = viewDirection.X * (x * x + (1 - x * x) * C) + viewDirection.Y * (
                    x * y * (1 - C) - z * S) + viewDirection.Z * (x * z * (1 - C) + y * S)
        newY = viewDirection.X * (x * y * (1 - C) + z * S) + viewDirection.Y * (
                    y * y + (1 - y * y) * C) + viewDirection.Z * (y * z * (1 - C) - x * S)
        newZ = viewDirection.X * (x * z * (1 - C) - y * S) + viewDirection.Y * (
                    y * z * (1 - C) + x * S) + viewDirection.Z * (z * z + (1 - z * z) * C)
        newdir = Vector3f(newX, newY, newZ)
        return newdir

    def Yaw(self, angle):
        self.forwardDir = self.Rotate(self.forwardDir, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.rithtDir = self.Rotate(self.rithtDir, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.mPos = self.Rotate(self.mPos, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.mViewCenter = self.Rotate(self.mViewCenter, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)

    def Pitch(self, angle):
        self.forwardDir = self.Rotate(self.forwardDir, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mUp = self.Rotate(self.mUp, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mPos = self.Rotate(self.mPos, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mViewCenter = self.Rotate(self.mViewCenter, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)


class camera:

    def __init__(self, machine=None):
        if machine == None:
            self.machine = MACHINE
        else:
            self.machine = machine
        self.reinit(self.machine)
        self.ratio = 0.72

    def reinit(self, machine=None):
        if machine is not None:
            self.machine = machine
        self.mPos = Vector3f(self.machine['x'] / 2, self.machine['y'] / 2, 0.0)
        self.mViewCenter = Vector3f(self.machine['x'] / 2, self.machine['y'] / 2, -1.0)
        self.mUp = Vector3f(0.0, 1.0, 0.0)
        self.right = 1.2 * max(self.machine['x'] / 2, self.machine['y'] / 2)
        self.top = 1.2 * max(self.machine['x'] / 2, self.machine['y'] / 2)
        self.forwardDir = self.mViewCenter - self.mPos
        self.rithtDir = self.forwardDir.cross(self.mUp)

    def Update(self):
        '''glMatrixMode有3种模式: GL_PROJECTION 投影, GL_MODELVIEW 模型视图, GL_TEXTURE 纹理.
            所以，在操作投影矩阵以前，需要调用函数：
            glMatrixMode(GL_PROJECTION); //将当前矩阵指定为投影矩阵
            然后把矩阵设为单位矩阵：
            glLoadIdentity();
            glOrtho(left, right, bottom, top, near, far)
            glOrtho(投影变换函数)创建一个正交平行的视景体，一般用于"物体不会因为离屏幕的远近而产生大小的变换"的情况。
            glOrtho将产生一个矩阵，这个矩阵将填到投影矩阵上
            gluLookAt设置从哪一个方位观察事物
            gluLookAt有三组数据，
            你把相机想象成为你自己的脑袋：
            第一组数据就是脑袋的位置
            第二组数据就是眼睛看的物体的位置
            第三组就是头顶朝向的方向（因为你可以歪着头看同一个物体）。
        '''
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glScale(self.ratio, 1, 1)  # glScale —— 将新的缩放矩阵乘以当前矩阵 ratio=0.72,1,1
        glOrtho(-self.right, self.right, -self.top, self.top, -200, 200)
        gluLookAt(self.mPos.X, self.mPos.Y, self.mPos.Z, self.mViewCenter.X, self.mViewCenter.Y, self.mViewCenter.Z,
                  self.mUp.X, self.mUp.Y, self.mUp.Z)

    def Move(self, deltax, deltay):
        self.forwardDir.Normalize()
        self.rithtDir.Normalize()
        self.mUp.Normalize()
        dx = self.rithtDir * deltax
        dy = self.mUp * deltay
        self.mPos = self.mPos - dx + dy
        self.mViewCenter = self.mPos + self.forwardDir

    def Rotate(self, viewDirection, angle, x, y, z):
        C = math.cos(angle * math.pi / 180)
        S = math.sin(angle * math.pi / 180)
        newX = viewDirection.X * (x * x + (1 - x * x) * C) + viewDirection.Y * (
                    x * y * (1 - C) - z * S) + viewDirection.Z * (x * z * (1 - C) + y * S)
        newY = viewDirection.X * (x * y * (1 - C) + z * S) + viewDirection.Y * (
                    y * y + (1 - y * y) * C) + viewDirection.Z * (y * z * (1 - C) - x * S)
        newZ = viewDirection.X * (x * z * (1 - C) - y * S) + viewDirection.Y * (
                    y * z * (1 - C) + x * S) + viewDirection.Z * (z * z + (1 - z * z) * C)
        newdir = Vector3f(newX, newY, newZ)
        return newdir

    def Yaw(self, angle):
        self.forwardDir = self.Rotate(self.forwardDir, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.rithtDir = self.Rotate(self.rithtDir, angle, self.mUp.X, self.mUp.Y, self.mUp.Z)
        self.mPos = self.mViewCenter - self.forwardDir

    def Pitch(self, angle):
        self.forwardDir = self.Rotate(self.forwardDir, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mUp = self.Rotate(self.mUp, angle, self.rithtDir.X, self.rithtDir.Y, self.rithtDir.Z)
        self.mPos = self.mViewCenter - self.forwardDir