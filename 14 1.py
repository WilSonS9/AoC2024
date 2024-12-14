class Robot:
    def __init__(self, pos, vel, h, w):
        self.pos = pos
        self.vel = vel
        self.h   = h
        self.w   = w
    
    def move(self):
        x, y         = self.pos
        dx, dy       = self.vel
        new_x, new_y = (x + dx) % self.w, (y + dy) % self.h
        self.pos     = (new_x, new_y)
    
    def position(self):
        return self.pos
    
    def __repr__(self):
        return f'p: {self.pos}, v: {self.vel}'

def safety_value(robots):
    q1, q2, q3, q4 = (0, 0, 0, 0)

    for robot in robots:
        x, y = robot.position()
        if x < w // 2 and y < h // 2:
            q1 += 1
        elif x < w // 2 and y > h // 2:
            q3 += 1
        elif x > w // 2 and y < h // 2:
            q2 += 1
        elif x > w // 2 and y > h // 2:
            q4 += 1

    return q1 * q2 * q3 * q4

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = 103
w = 101

robots = []

for r in l:
    s1, s2 = r.split(' ')
    x, y   = map(int, s1.split('=')[1].split(','))
    dx, dy = map(int, s2.split('=')[1].split(','))
    robots.append(Robot((x, y), (dx, dy), h, w))

for _ in range(100):
    for robot in robots:
        robot.move()

print(safety_value(robots))