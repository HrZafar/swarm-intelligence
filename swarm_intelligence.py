import random


def fitness(x, y):
    return round(100 * (x ** 2 - y) ** 2 + (1 - x) ** 2, 2)


def gen_individuals(n):
    list = []
    for i in range(n):
        dict = {}
        dict['x'] = round(random.uniform(-2, 2.01), 2)
        if dict['x'] > 2:
            dict['x'] = 2
        dict['y'] = round(random.uniform(-1, 3.01), 2)
        if dict['y'] > 3:
            dict['y'] = 3
        dict['present'] = fitness(dict['x'], dict['y'])
        dict['xbest'] = dict['x']
        dict['ybest'] = dict['y']
        dict['best'] = dict['present']
        dict['x_velocity'] = 0
        dict['y_velocity'] = 0
        list.append(dict)
    return list


def loc_best(list):
    best = 0
    local = {}
    for i in range(len(list)):
        if list[i]['best'] > best:
            best = list[i]['best']
            local['x'] = list[i]['x']
            local['y'] = list[i]['y']
            local['best'] = list[i]['best']
    return local


def velocity(particle):
    c1 = c2 = 2
    vx = particle['x_velocity'] + c1 * random.uniform(0, 1) * (
        particle['xbest'] - particle['x']) + c2 * random.uniform(0, 1) * (global_best['x'] - particle['x'])
    vy = particle['y_velocity'] + c1 * random.uniform(0, 1) * (
        particle['ybest'] - particle['y']) + c2 * random.uniform(0, 1) * (global_best['y'] - particle['y'])
    return vx, vy


def swarm_intelligence(list):
    list1 = []
    for i in range(len(list)):
        dict1 = {}
        vx, vy = velocity(list[i])
        x = round(list[i]['x'] + vx, 2)
        if -2 <= x <= 2:
            dict1['x'] = x
        else:
            dict1['x'] = list[i]['x']
        y = round(list[i]['y'] + vy, 2)
        if -1 <= y <= 3:
            dict1['y'] = y
        else:
            dict1['y'] = list[i]['y']
        dict1['present'] = fitness(dict1['x'], dict1['y'])
        if dict1['present'] > list[i]['best']:
            dict1['xbest'] = dict1['x']
            dict1['ybest'] = dict1['y']
            dict1['best'] = dict1['present']
        else:
            dict1['xbest'] = list[i]['xbest']
            dict1['ybest'] = list[i]['ybest']
            dict1['best'] = list[i]['best']
        dict1['x_velocity'] = vx
        dict1['y_velocity'] = vy
        list1.append(dict1)
    return list1


local_best = global_best = {'x': 0, 'y': 0, 'best': 0}
particles = gen_individuals(25)
print(particles)
for i in range(20):
    local_best = loc_best(particles)
    if global_best['best'] < local_best['best']:
        global_best = local_best
    print('global best', global_best)
    particles = swarm_intelligence(particles)