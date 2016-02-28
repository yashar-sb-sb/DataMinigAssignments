from algorithms.array import selection

import sys, pygame, math
from pygame.locals import *

import random

from OpenGL.GL import *
from OpenGL.GLU import *

def plot(mi, q1, q2, q3, ma):
  if(ma - mi > 0):
    q1 -= mi
    q2 -= mi
    q3 -= mi
    ma -= mi
    mi = 0

    q1 /= ma
    q2 /= ma
    q3 /= ma
    ma = 1

    q1 = 1.9 * q1 -0.95
    q2 = 1.9 * q2 -0.95
    q3 = 1.9 * q3 -0.95
    mi = 1.9 * mi -0.95
    ma = 1.9 * ma -0.95

    
  pygame.init()
  display = (600, 600)
  pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
  clock = pygame.time.Clock()
    
  framesCount = 0
    
  a, x, y, z = 1,0,0,0 #random.randint(-2,2),random.randint(-2,2),random.randint(-2,2),random.randint(-2,2)
    
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
          x = 1
        elif event.key == pygame.K_y:
          y = 1
        elif event.key == pygame.K_z:
          z = 1
          
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_x:
          x = 0
        elif event.key == pygame.K_y:
          y = 0
        elif event.key == pygame.K_z:
          z = 0
        
    glRotatef(a,x,y,z)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    sq(genFlat(mi))
    sq(genFlat(q1))
    sq(genFlat(q2))
    sq(genFlat(q3))
    sq(genFlat(ma))
    sq((
      (-0.1,-0.1,q1),
      (-0.1,-0.1,q3),
      ))
    sq((
      (0.1,-0.1,q1),
      (0.1,-0.1,q3),
      ))
    sq((
      (-0.1,0.1,q1),
      (-0.1,0.1,q3),
      ))
    sq((
      (0.1,0.1,q1),
      (0.1,0.1,q3),
      ))
    pygame.display.flip()
    clock.tick(30)

def genFlat(a):
  return (
    (-0.1,-0.1,a),
    (-0.1,0.1,a),
    (0.1,-0.1,a),
    (0.1,0.1,a),
    )

def trans(v):
  return (v[0],v[2],v[1])

def sq(verts):
  glBegin(GL_LINES)
  for i in range(len(verts)):
    for j in range(i):
      glVertex3fv(trans(verts[i]))
      glVertex3fv(trans(verts[j]))
  glEnd()

def findMedian(a):
  selection.randomizedSelection(a, len(a)/2)
  p = int(math.floor(len(a)/2))
  if len(a)%2 == 1:
    return a[:p], a[p], a[p+1:]
  selection.randomizedSelection(a, p-1, r = p)
  return a[:p], (a[p-1]+a[p])/2, a[p:]

def main():
  data = []
  if len(sys.argv) > 1:
    data = list(map(int, sys.argv[1:]))
  else:
    inp = sys.stdin.read()
    tmp = 0

    for i in inp:
      if i.isdigit():
        tmp = 10 * tmp + int(i)
        flag = True
      elif(flag):
        data.append(tmp)
        tmp = 0
        flag = False
  l, q2, r = findMedian(data)
  l, q1, _ = findMedian(l)
  _, q3, r = findMedian(r)
  mi = min(l)
  ma = max(r)
  plot(mi,q1,q2,q3,ma)

main()
#selection.randomizedSelection(
