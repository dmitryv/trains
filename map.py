from queue import Queue

class Map:
    def __init__(self, *node_list):
        map = {}
        tmp = {}
        for i in node_list:
            tmp[i] = None
        for i in node_list:
            map[i] = tmp.copy()
        self.map = map
        self.node_list = node_list
        return

    def append(self, node_from, node_to, distance):
        assert distance > 0
        assert node_from in self.node_list
        assert node_to   in self.node_list
        self.map[node_from][node_to] = distance
        return

    def distance(self, node_from, node_to):
        return self.map[node_from][node_to]

    def sum_distance(self, *node_list):
        sum = 0
        while True:
            if 1 == len(node_list):
                return sum
            distance = self.distance(node_list[0], node_list[1])
            if distance is None:
                return 'NO SUCH ROUTE'
            sum += distance
            node_list = node_list[1:]

    def shortest_route(self, node_from, node_to):
        shortest = -1
        queue = Queue()

        def put_in(node, route):
            for i in self.node_list:
                distance = self.distance(node, i)
                if distance is not None:
                    queue.put((i, route + distance))
            return

        put_in(node_from, 0)

        while not queue.is_empty():
            node, route = queue.get()
            if route > shortest > 0:
                continue
            if node == node_to:
                if -1 == shortest or route < shortest:
                    shortest = route
                continue
            put_in(node, route)

        return shortest

    def all_trips(self, node_from, node_to, accept_func, trim_func):
        number = 0
        queue = Queue()

        def put_in(node, step, route):
            for i in self.node_list:
                distance = self.distance(node, i)
                if distance is not None:
                    queue.put((i, step + 1, route + distance))
            return

        put_in(node_from, 0, 0)

        while not queue.is_empty():
            node, step, route = queue.get()
            if node == node_to and accept_func(step, route):
                number += 1
            if trim_func(step, route):
                continue

            put_in(node, step, route)

        return number
