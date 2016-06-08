from map import Map

def input(graph):
    node_list = set()
    edge_list = []
    for i in graph:
        node_list.add(i[0])
        node_list.add(i[1])
        edge_list.append([i[0], i[1], int(i[2:])])
    map = Map(*node_list)
    for i in edge_list:
        map.append(*i)
    return map

def output(number, result):
    print('Output #{}: {}'.format(number, result))
    return

def question_1(map):
    output(1, map.sum_distance('A', 'B', 'C'))

def question_2(map):
    output(2, map.sum_distance('A', 'D'))

def question_3(map):
    output(3, map.sum_distance('A', 'D', 'C'))

def question_4(map):
    output(4, map.sum_distance('A', 'E', 'B', 'C', 'D'))

def question_5(map):
    output(5, map.sum_distance('A', 'E', 'D'))

def question_6(map):
    accept_func = lambda step, distance: step <= 3
    trim_func   = lambda step, distance: step > 3
    output(6, map.all_trips('C', 'C', accept_func, trim_func))

def question_7(map):
    accept_func = lambda step, distance: 4 == step
    trim_func   = lambda step, distance: step > 4
    output(7, map.all_trips('A', 'C', accept_func, trim_func))

def question_8(map):
    output(8, map.shortest_route('A', 'C'))

def question_9(map):
    output(9, map.shortest_route('B', 'B'))

def question_10(map):
    accept_func = lambda step, distance: distance < 30
    trim_func   = lambda step, distance: distance >= 30
    output(10, map.all_trips('C', 'C', accept_func, trim_func))

def main():
    map = input(['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])
    question_1(map)
    question_2(map)
    question_3(map)
    question_4(map)
    question_5(map)
    question_6(map)
    question_7(map)
    question_8(map)
    question_9(map)
    question_10(map)
    return

if __name__ == '__main__':
    main()
