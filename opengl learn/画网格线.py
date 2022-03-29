from OpenGL.GL import *
from OpenGL.GLUT import *
import math




def draw():
        PI = 3.1415926
        R = 0.5
        TR = R - 0.05
        glClear(GL_COLOR_BUFFER_BIT)
        segment = 6
        fragment_distance_width = segment                       #间隔
        fragment_distance_height = segment
        fragment_width = 270 // segment
        fragment_height = 270 // segment
        glColor(150, 150, 150)        #线条的颜色
        a=5
        b=20

        glBegin(GL_LINE_LOOP)

        glVertex2f(0, 0)
        glVertex2f(0.5, 0)
        glVertex2f(0.5, 0.5)
        glVertex2f(0, 0.5)
        glEnd()

        # glBegin(GL_LINES)
        # for i in range(1, fragment_width):
        #     if i % 5 == 0:
        #         glVertex2f(i * fragment_distance_width, 0)
        #         glVertex2f(i * fragment_distance_width, 270)
        #     else:
        #         glVertex2f(i * fragment_distance_width, 0)
        #         glVertex2f(i * fragment_distance_width, 2)
        #
        # for i in range(1, fragment_height):
        #     if i % 5 == 0:
        #         glVertex2f(0, i * fragment_distance_height)
        #         glVertex2f(270, i * fragment_distance_height)
        #     else:
        #         glVertex2f(0, i * fragment_distance_height)
        #         glVertex2f(2, i * fragment_distance_height)
        #
        # glEnd()

        glBegin(GL_LINE_LOOP)
        for i in range(100):
            glVertex2f(R * math.cos(2 * PI / 100 * i), R * math.sin(2 * PI / 100 * i))
        glEnd()


        glFlush()

if __name__ == '__main__':
    glutInit()
    glutCreateWindow('Gridlines')
    glutDisplayFunc(draw)
    glutMainLoop()