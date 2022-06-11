from Utils import *
import pygame

BACKGROUND = (51, 51, 51)
WHITE = (236, 240, 241)
GRAY = (61, 72, 73)
BLACK = (23, 32, 42)
YELLOW = (244, 208, 63)
BLUE = (52, 152, 219)
RED = (203, 67, 53)
PURPLE = (136, 78, 160)
ORANGE = (230, 126, 34)
GREEN = (50, 180, 99)
BROWN = (100, 30, 22)
STICKCOLOR = (249, 231, 159)
COLORS = [YELLOW, BLUE, RED, PURPLE, ORANGE, GREEN, BROWN, BLACK]

width = 720
height = 360
margin = 20
radius = 10
mass_of_air = 0.2
class Ball():
    def __init__(self,ballNum,color,position,iscueball = False,mass = 3,speed=0,angle=0):      
        self.Ballnum = ballNum
        self.color = color
        self.x , self.y = position
        self.isCueball = iscueball
        self.speed = speed
        self.angle = angle
        self.mass = mass
        self.drag = 0.9988
    def draw(self,display):
        pygame.draw.circle(display, self.color, (self.x,self.y),radius)
        if self.Ballnum > 8:
            pygame.draw.circle(display, WHITE, (self.x,self.y),radius-3)
    def move(self):
        self.speed *= self.drag
        if self.speed < 0.01: self.speed *= self.drag
        if self.speed < 0.001:
            self.speed = 0
            self.angle = 0
        self.x += sin(self.angle)*self.speed
        self.y -= cos(self.angle)*self.speed
    def getPos(self):
        return (self.x,self.y)

    def bounce(self):
        #[[width,20], [width-margin,50],[width-margin,height-50],[width,height-20]]
        if (self.x + radius > width - margin  and 
            (self.y-20)/(50-20) > (self.x+radius-width)/(width-margin-width) and
            (self.y-(height-50))/(height-20-(height-50)) < (self.x+radius-width+margin)/(width-(width-margin))):
            dy = 50-20
            dx = width-margin-width
            if 50 > self.y:
                angle = 0.5*pi - atan2(dy,dx)
                self.x += sin(angle)
                self.y -= cos(angle)
                self.angle = -self.angle -angle
                self.speed *= 0.8
            elif 50 <= self.y < height - 50:
                self.x = width - radius - margin
                self.angle = -self.angle
                self.speed *= 0.8
            elif height - 50 <= self.y:
                angle = 0.5*pi - atan2(dy,dx)
                self.x += sin(angle)
                self.y += cos(angle)
                self.angle = -self.angle +angle
                self.speed *= 0.8
        #[[width/2 + 20, margin], [width/2 +10, 0],[width-20,0],[width-50,margin]]
        if (self.y - radius < margin  and 
            (self.y - radius -margin)/(0-margin) > (self.x-(width/2 + 20))/(width/2 +10 - (width/2 + 20)) and
            (self.y - radius -0)/(margin-0) < (self.x-(width-20))/(width-50-(width-20))):
            if width/2 + 20 > self.x:
                dy = 0-margin
                dx = width/2 +10 - (width/2 + 20)
                angle = 0.5*pi + atan2(dy,dx)
                self.x += sin(angle)
                self.y += cos(angle)
                self.angle = -self.angle +angle
                self.speed *= 0.8
            if width/2 + 20 <= self.x < width-50:
                self.y = margin + radius
                self.angle = pi - self.angle
                self.speed *= 0.8
            if width-50 <= self.x:
                dy = margin-0
                dx = width-50-(width-20)
                angle = 0.5*pi - atan2(dy,dx)
                self.x -= sin(angle)
                self.y += cos(angle)
                self.angle = -self.angle -angle
                self.speed *= 0.8
        #[[20,0],[50,margin],[width/2-20, margin], [width/2 - 10, 0]]
        if (self.y - radius < margin  and 
            (self.y - radius -0)/(margin-0) < (self.x-(20))/(50 - 20) and
            (self.y - radius -margin)/(0-margin) > (self.x-(width/2-20))/(width/2 - 10-(width/2-20))):
            if 50 > self.x:
                dy = margin-0
                dx = (50 - 20)
                angle = 0.5*pi + atan2(dy,dx)
                self.x -= sin(angle)
                self.y -= cos(angle)
                self.angle = - self.angle - angle
                self.speed *= 0.8
            if 50 <= self.x < width/2-20:
                self.y = margin + radius
                self.angle = pi - self.angle
                self.speed *= 0.8
            if width/2-20 <= self.x:
                dy = 0-margin
                dx = (width/2 - 10-(width/2-20))
                angle = 0.5*pi - atan2(dy,dx)
                self.x += sin(angle)
                self.y -= cos(angle)
                self.angle = self.angle +angle
                self.speed *= 0.8        
        #[[0,20],[margin,50],[margin, height-50], [0, height-20]]
        if (self.x - radius < margin  and 
            (self.y-20)/(50-20) > (self.x-radius-0)/(margin-0) and
            (self.y-(height-50))/(height-20-(height-50)) < (self.x-radius-margin)/(0-(margin))):
            dy = 50-20
            dx = margin-0
            if 50 > self.y:
                angle = 0.5*pi - atan2(dy,dx)
                self.x += sin(angle)
                self.y -= cos(angle)
                self.angle = -self.angle -angle
                self.speed *= 0.8
            elif 50 <= self.y < height - 50:
                self.x = radius + margin
                self.angle = -self.angle
                self.speed *= 0.8
            elif height - 50 <= self.y:
                angle = 0.5*pi - atan2(dy,dx)
                self.x += sin(angle)
                self.y += cos(angle)
                self.angle = -self.angle +angle
                self.speed *= 0.8
        #[[20,height],[50,height-margin],[width/2-20, height-margin], [width/2 - 10, height]]
        if (self.y + radius > height - margin  and 
            (self.y + radius -height)/(height-margin-height) < (self.x-(20))/(50 - 20) and
            (self.y + radius -(height-margin))/(height-(height-margin)) > (self.x-(width/2-20))/(width/2 - 10-(width/2-20))):
            if 50 > self.x:
                dy = margin-0
                dx = (50 - 20)
                angle = 0.5*pi + atan2(dy,dx)
                self.x -= sin(angle)
                self.y += cos(angle)
                self.angle =  self.angle + angle
                self.speed *= 0.8
            if 50 <= self.x < width/2-20:
                self.y = height - (margin + radius)
                self.angle = pi - self.angle
                self.speed *= 0.8
            if width/2-20 <= self.x:
                dy = height-(height-margin)
                dx = (width/2 - 10-(width/2-20))
                angle = 0.5*pi - atan2(dy,dx)
                self.x += sin(angle)
                self.y -= cos(angle)
                self.angle =  -self.angle - angle
                self.speed *= 0.8   
        #[[width/2 + 20, height-margin], [width/2 +10, height],[width-20,height],[width-50,height-margin]] 
        if (self.y + radius > height - margin  and 
            (self.y + radius -(height-margin))/(height-(height-margin)) > (self.x-(width/2 + 20))/(width/2 +10 - (width/2 + 20)) and
            (self.y + radius -(height))/((height-margin)-height) < (self.x-(width-20))/(width-50-(width-20))):
            if width/2 + 20 > self.x:
                dy = height-(height-margin)
                dx = width/2 +10 - (width/2 + 20)
                angle = 0.5*pi + atan2(dy,dx)
                self.x += sin(angle)
                self.y += cos(angle)
                self.angle = self.angle +angle
                self.speed *= 0.8
            if width/2 + 20 <= self.x < width-50:
                self.y = height - (margin + radius)
                self.angle = pi - self.angle
                self.speed *= 0.8
            if width-50 <= self.x:
                dy = (height-margin)-height
                dx = width-50-(width-20)
                angle = 0.5*pi - atan2(dy,dx)
                self.x -= sin(angle)
                self.y += cos(angle)
                self.angle = self.angle +angle
                self.speed *= 0.8

        if self.x > width - radius:
            self.x = 2 * (width - radius) - self.x
            self.angle = - self.angle
        elif self.x < radius:
            self.x = radius
            self.angle = - self.angle
        if self.y > height - radius:
            self.y = 2 * (height - radius) - self.y
            self.angle = pi - self.angle
        elif self.y < radius:
            self.y = 2 * radius - self.y
            self.angle = pi - self.angle
    
    def isSink(self,Pocket):
        for (x,y) in Pocket.pos:
            dx = self.x - x
            dy = self.y - y
            dist = hypot(dx,dy)
            if dist < radius + 4:
                return True
        return False

class Table():
    def __init__(self):
        self.shape = [
            [[0,20],[margin,50],[margin, height-50], [0, height-20]],#left
            [[20,0],[50,margin],[width/2-20, margin], [width/2 - 10, 0]],#top left
            [[width/2 + 20, margin], [width/2 +10, 0],[width-20,0],[width-50,margin]],#top right
            [[width,20], [width-margin,50],[width-margin,height-50],[width,height-20]],#right
            [[width/2 + 20, height-margin], [width/2 +10, height],[width-20,height],[width-50,height-margin]],#Bottom rigth
            [[20,height],[50,height-margin],[width/2-20, height-margin], [width/2 - 10, height]]# bottom left
        ]

    def draw(self,display):
        for edge in self.shape:
            pygame.draw.polygon(display,GRAY,edge)
         
class Pocket():
    def __init__(self):
        self.num = 6
        self.pos = [
            (width/2,7),(16,16),(width-16,16),(16,height-16),(width-16,height-16),(width/2,height-7)
        ]
        self.radius = 16
    def draw(self,display):
        for pock_pos in self.pos:
            pygame.draw.circle(display, BLACK, pock_pos,self.radius)

class Game():
    def __init__(self):
        self.table = Table()
        self.pockets = Pocket()
        s = 120
        self.balls = [
            Ball(0,WHITE,(width*3/4,height/2),True),
            Ball(1,COLORS[0],(s, height/2 - 4*radius)),
            Ball(2,COLORS[1],(s + 2*(radius-1.5), height/2 - 3*radius)),
            Ball(3,COLORS[2],(s, height/2 - 2*radius)),
            Ball(4,COLORS[3],(s + 4*(radius-1.5), height/2 - 2*radius)),
            Ball(5,COLORS[4],(s + 2*(radius-1.5), height/2 - 1*radius)),
            Ball(6,COLORS[5],(s, height/2)),
            Ball(7,COLORS[6],(s + 6*(radius-1.5), height/2 - 1*radius)),
            Ball(8,COLORS[7],(s + 4*(radius-1.5), height/2)),
            Ball(9,COLORS[0],(s + 8*(radius-1.5), height/2)),
            Ball(10,COLORS[1],(s + 6*(radius-1.5), height/2 + 1*radius)),
            Ball(11,COLORS[2],(s + 2*(radius-1.5), height/2 + 1*radius)),
            Ball(12,COLORS[3],(s, height/2 + 2*radius)),
            Ball(13,COLORS[4],(s + 4*(radius-1.5), height/2 + 2*radius)),
            Ball(14,COLORS[5],(s + 2*(radius-1.5), height/2 + 3*radius)),
            Ball(15,COLORS[6],(s, height/2 + 4*radius)),
        ]
        self.sinked = 0
        self.GameOver = False
        self.Iswin = False
    
    def draw(self,display):
        if self.GameOver:
            display.fill((0,128,0))
            self.table.draw(display)
            self.pockets.draw(display)
            for ball in self.balls:
                ball.draw(display)
            overtxt = pygame.font.SysFont("Agency FB", 30).render("GAME OVER", True, WHITE)
            display.blit(overtxt,(width/2,height/2))
        elif self.Iswin:
            display.fill((0,128,0))
            self.table.draw(display)
            self.pockets.draw(display)
            for ball in self.balls:
                ball.draw(display)
            wintxt = pygame.font.SysFont("Agency FB", 30).render("YOU WIN", True, WHITE)
            display.blit(wintxt,(width/2,height/2))
        else:
            display.fill((0,128,0))
            self.table.draw(display)
            self.pockets.draw(display)
            if self.isStopped():
                self.drawCuestick(self.balls[0].x,self.balls[0].y,display)
            for ball in self.balls:
                ball.draw(display)

    def drawCuestick(self,cuex,cuey,display):
        x, y = pygame.mouse.get_pos()
        tangent = (degrees(atan2((cuey - y), (cuex - x))))
        pygame.draw.line(display, WHITE, (cuex + 10000*cos(radians(tangent)), cuey + 10000*sin(radians(tangent))), (cuex, cuey), 1)
        pygame.draw.line(display, BROWN, (x, y), (cuex, cuey), 3)

    def update(self):
        if self.GameOver:return
        if not self.isStopped():
            for i,ball in enumerate(self.balls):
                # if ball.isCueball:
                #     print(ball.angle%(2*pi))
                ball.move()
                ball.bounce()
                for ball2 in self.balls[i+1:]:
                    self.collide(ball,ball2)

                if ball.isSink(self.pockets):
                    if not ball.isCueball:
                        self.sinked += 1
                        self.balls.remove(ball)
                    else:
                        self.GameOver = True
                        self.balls.remove(ball)
            if len(self.balls) == 1 and self.balls[0].isCueball:
                self.Iswin = True

    def full_update(self):
        if self.GameOver:return
        while not self.isStopped():
            for i,ball in enumerate(self.balls):
                ball.move()
                ball.bounce()
                for ball2 in self.balls[i+1:]:
                    self.collide(ball,ball2)
                if ball.isSink(self.pockets):
                    if not ball.isCueball:
                        self.sinked += 1
                        self.balls.remove(ball)
                    else:
                        self.GameOver = True
                        self.balls.remove(ball)
            if len(self.balls) == 1 and self.balls[0].isCueball:
                self.Iswin = True

    def collide(self,ball1,ball2):
        dx = ball1.x - ball2.x
        dy = ball1.y - ball2.y
        dist = hypot(dx,dy)
        if dist < radius*2:
            # print(ball1.Ballnum,ball2.Ballnum)
            angle = atan2(dy,dx) + 0.5*pi
            angle1, speed1 = addVectors(ball1.angle, 0, angle, ball2.speed)
            angle2, speed2 = addVectors(ball2.angle, 0, angle+pi, ball1.speed)
            # print(abs(ball1.angle%(2*pi)-(atan2(dy,dx) - 0.5*pi)%(2*pi)),abs(ball2.angle%(2*pi)-(atan2(dy,dx) - 0.5*pi)%(2*pi)))
            angledif = min(abs(ball1.angle%(2*pi)-(atan2(dy,dx) - 0.5*pi)%(2*pi)),abs(ball2.angle%(2*pi)-(atan2(dy,dx) - 0.5*pi)%(2*pi)))
            # angledif = abs(ball1.angle%(2*pi)-(atan2(dy,dx) - 0.5*pi)%(2*pi))
            if ball2.speed == 0:
                if ball1.angle%(2*pi) > angle2%(2*pi):
                    if  pi*3/2 < ball1.angle%(2*pi) < pi*2 and 0 < angle2%(2*pi) < pi/2:
                        ball1.angle =  ball1.angle - (pi/2 + (ball1.angle%(2*pi) - angle2%(2*pi))%(2*pi))%(2*pi)
                    else:
                        ball1.angle =  ball1.angle + (pi/2 - (ball1.angle%(2*pi) - angle2%(2*pi))%(2*pi))%(2*pi)


                else:
                    if  pi*3/2 < angle2%(2*pi) < pi*2 and 0 < ball1.angle%(2*pi) < pi/2:
                        ball1.angle =  ball1.angle + (pi/2 - (ball1.angle%(2*pi) - angle2%(2*pi))%(2*pi))%(2*pi)
                    else:
                        ball1.angle =  ball1.angle - (pi/2 + (ball1.angle%(2*pi) - angle2%(2*pi))%(2*pi))%(2*pi)
            else:
                ball1.angle,ball1.speed = angle1, speed1

            ball1.speed = speed1

            ball2.angle,ball2.speed = angle2, speed2
            # print(ball1.speed,ball2.speed)
            # print(angledif)
            angledif = sigmoid(angledif)
            # print(angledif)
            if ball2.speed == 0 and angledif > 0.01:
                ball2.speed = ball1.speed *(1-angledif)
                ball1.speed *=  angledif
            elif ball1.speed == 0 and angledif < 0.99:
                ball1.speed = ball2.speed * angledif
                ball2.speed *= 1 - angledif

            # if angledif > 2:
            #     overlap = 0.5 * (20-dist)
            #     ball1.x += sin(angle) * overlap
            #     ball1.y -= cos(angle) * overlap
            #     ball2.x -= sin(angle) * overlap
            #     ball2.y += cos(angle) * overlap
            #     dx = ball1.x - ball2.x
            #     dy = ball1.y - ball2.y
            #     dist = hypot(dx,dy)
            #     angle = atan2(dy,dx) + 0.5*pi
            #     angle1, speed1 = addVectors(ball1.angle, 0, angle, ball2.speed)
            #     angle2, speed2 = addVectors(ball2.angle, 0, angle+pi, ball1.speed)
            #     angledif = abs(ball1.angle%(2*pi)-(atan2(dy,dx) - 0.5*pi)%(2*pi))
                # ball1.speed = ball2.speed * (1 - (angledif/(2*pi)))
                # ball2.speed *= (angledif/(2*pi))
                # print(angledif)
            #     if ball1.speed == 0 or ball2.speed != 0:
            #         ball1.speed = ball2.speed * (angledif/2)
            #         ball2.speed *= 1 - (angledif%(pi))
            #     else:
            #         ball1.speed *= 1 - (angledif%(pi))
            #         ball2.speed *= ball1.speed * (angledif/2)
            # else:
            #     if ball1.speed == 0 or ball2.speed != 0:
            #         ball1.speed = ball2.speed * (angledif/2)
            #         ball2.speed *= 1 - (angledif/2)
            #     else:

            # print(ball1.speed,ball2.speed)
            ball1.speed *=0.99
            ball2.speed *=0.99
            overlap = 0.5 * (20-dist) + 0.05
            ball1.x += sin(angle) * overlap
            ball1.y -= cos(angle) * overlap
            ball2.x -= sin(angle) * overlap
            ball2.y += cos(angle) * overlap
    def getAllballPos(self):
        ballpos= []
        for ball in self.balls:
            ballpos.append(ball.getPos())
        return ballpos
    
    def getDistribution(self):
        fitness = 0
        dist = 0
        ballpos = self.getAllballPos()
        for ball in self.balls:
            if ball.isCueball:continue
            pockPos = self.pockets.pos
            ballpos = ball.getPos()
            Pdist = [hypot(ppos[0]-ballpos[0],ppos[1]-ballpos[1]) for ppos in pockPos]
            dist += min(Pdist)
        if dist == 0: dist = 1000000000
        fitness = 1/dist 
        for i in range(16-len(self.balls)):
            fitness = 1/dist + 0.1
        return fitness
        

    def ForcetoCue(self,angle,force):
        if force > 2: force = 2
        self.balls[0].angle = angle
        self.balls[0].speed = force

    def isStopped(self):
        if all([not ball.speed for ball in self.balls]):
            return True
        else: 
            return False


