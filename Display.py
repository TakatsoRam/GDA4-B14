import pygame
from pygame.locals import QUIT, DOUBLEBUF, OPENGL, K_1, K_2, K_3, K_a, K_d, K_w, K_s, K_q, K_e, K_i, K_k, K_j, K_l, K_u, K_o, K_z, K_x, K_c, K_v, K_b, K_n
from OpenGL.GL import glBegin, glEnd, glVertex3fv, glRotatef, glScalef, glClear, glGetError, glClearColor, glEnable, glTranslatef, glLoadIdentity, glColor3f, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_LINES, GL_DEPTH_TEST, GL_NO_ERROR
from OpenGL.GLU import gluPerspective
import sys

import Cube
import Pyramid
import Prism

class Display:
    def __init__(self):
        pygame.init()
        self.display = (800, 600)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        self.translation = [0, 0, -5]  # Initial translation to move the object away from the camera
        self.rotation = [0, 0, 0]  # Initial rotation angles for x, y, and z axes
        self.scale = [1, 1, 1]  # Initial scaling factors for x, y, and z axes
        self.object_to_draw = 'cube'
        self.models = {
            'cube': (Cube.vertices, Cube.edges),
            'pyramid': (Pyramid.vertices, Pyramid.edges),
            'prism': (Prism.vertices, Prism.edges)
        }

        # Set the background color
        glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
        glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering

    def draw(self, vertices, edges):
        glColor3f(1, 1, 1)  # Set color to white
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
        error = glGetError()
        if error != GL_NO_ERROR:
            print(f'OpenGL Error: {error}')

    def translate_obj(self, dx, dy, dz):
        self.translation[0] += dx
        self.translation[1] += dy
        self.translation[2] += dz

    def rotate_obj(self, rx, ry, rz):
        
        self.rotation[0] += rx
        self.rotation[1] += ry
        self.rotation[2] += rz

    def scale_obj(self, sx, sy, sz):
        self.scale[0] *= sx
        self.scale[1] *= sy
        self.scale[2] *= sz

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        self.object_to_draw = 'cube'
                    elif event.key == K_2:
                        self.object_to_draw = 'pyramid'
                    elif event.key == K_3:
                        self.object_to_draw = 'prism'
                    elif event.key == K_a:
                        self.translate_obj(-0.1, 0, 0)
                    elif event.key == K_d:
                        self.translate_obj(0.1, 0, 0)
                    elif event.key == K_w:
                        self.translate_obj(0, 0.1, 0)
                    elif event.key == K_s:
                        self.translate_obj(0, -0.1, 0)
                    elif event.key == K_q:
                        self.translate_obj(0, 0, 0.1)
                    elif event.key == K_e:
                        self.translate_obj(0, 0, -0.1)
                    elif event.key == K_i:
                        self.rotate_obj(-5, 0, 0)  # Rotate around x-axis in positive direction
                    elif event.key == K_k:
                        self.rotate_obj(5, 0, 0)  # Rotate around x-axis in negative direction
                    elif event.key == K_j:
                        self.rotate_obj(0, -5, 0)  # Rotate around y-axis in positive direction
                    elif event.key == K_l:
                        self.rotate_obj(0, 5, 0)  # Rotate around y-axis in negative direction
                    elif event.key == K_u:
                        self.rotate_obj(0, 0, -5)  # Rotate around z-axis in positive direction
                    elif event.key == K_o:
                        self.rotate_obj(0, 0, 5)  # Rotate around z-axis in negative direction
                    elif event.key == K_z:
                        self.scale_obj(0.9, 1, 1)  # Shrink along x-axis
                    elif event.key == K_x:
                        self.scale_obj(1.1, 1, 1)  # Grow along x-axis
                    elif event.key == K_c:
                        self.scale_obj(1, 0.9, 1)  # Shrink along y-axis
                    elif event.key == K_v:
                        self.scale_obj(1, 1.1, 1)  # Grow along y-axis
                    elif event.key == K_b:
                        self.scale_obj(1, 1, 0.9)  # Shrink along z-axis
                    elif event.key == K_n:
                        self.scale_obj(1, 1, 1.1)  # Grow along z-axis

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslatef(*self.translation)
            # Apply rotations in the order: x, y, z
            glRotatef(self.rotation[0], 1, 0, 0)
            glRotatef(self.rotation[1], 0, 1, 0)
            glRotatef(self.rotation[2], 0, 0, 1)
            # Applying scaling
            glScalef(*self.scale)

            vertices, edges = self.models[self.object_to_draw]
            self.draw(vertices, edges)

            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    display = Display()
    display.run()




