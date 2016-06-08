import unittest

from queue import Queue
from map import Map


class QueueTest(unittest.TestCase):
    def test(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.put(1)
        self.assertFalse(queue.is_empty())
        self.assertEqual(1, queue.get())


class MapTest(unittest.TestCase):
    def test_init(self):
        map = Map(1, 2, 3)
        self.assertEqual(map.node_list, (1, 2, 3))
        self.assertEqual(map.map, {1: {1: None, 2: None, 3: None}, 2: {1: None, 2: None, 3: None}, 3: {1: None, 2: None, 3: None}})

    def test_append(self):
        map = Map(1, 2, 3)
        map.append(1, 2, 3)
        map.append(1, 3, 3)
        map.append(3, 2, 4)
        self.assertEqual(map.node_list, (1, 2, 3))
        self.assertEqual(map.map, {1: {1: None, 2: 3, 3: 3}, 2: {1: None, 2: None, 3: None}, 3: {1: None, 2: 4, 3: None}})
        with self.assertRaises(AssertionError):
            map.append(2, 3, 0)
        with self.assertRaises(AssertionError):
            map.append(4, 3, 1)

    def test_distance(self):
        map = Map(1, 2, 3)
        map.append(1, 2, 3)
        map.append(1, 3, 3)
        map.append(3, 2, 4)
        self.assertEqual(map.distance(1, 2), 3)
        self.assertEqual(map.distance(1, 3), 3)
        self.assertEqual(map.distance(3, 2), 4)
        self.assertIsNone(map.distance(2, 1))

    def test_sum_distance(self):
        map = Map(1, 2, 3)
        map.append(1, 2, 1)
        map.append(2, 3, 2)
        map.append(3, 1, 4)
        self.assertEqual(map.sum_distance(1, 2), 1)
        self.assertEqual(map.sum_distance(1, 2, 3), 3)
        self.assertEqual(map.sum_distance(1, 2, 3, 1), 7)
        self.assertEqual(map.sum_distance(2, 1), 'NO SUCH ROUTE')

    def test_shortest_route_1(self):
        map = Map(1, 2, 3)
        map.append(1, 3, 100)
        map.append(1, 2, 1)
        map.append(2, 3, 2)
        self.assertEqual(map.shortest_route(1, 3), 3)

    def test_shortest_route_2(self):
        map = Map(1, 2, 3)
        map.append(1, 3, 100)
        self.assertEqual(map.shortest_route(1, 3), 100)

    def test_all_trips_1(self):
        map = Map(1, 2, 3)
        map.append(1, 3, 100)
        accept_func = lambda step, distance: True
        trim_func   = lambda step, distance: False
        self.assertEqual(map.all_trips(1, 3, accept_func, trim_func), 1)

    def test_all_trips_2(self):
        map = Map(1, 2, 3)
        map.append(1, 3, 1)
        map.append(1, 2, 1)
        map.append(2, 3, 1)
        accept_func = lambda step, distance: True
        trim_func   = lambda step, distance: False
        self.assertEqual(map.all_trips(1, 3, accept_func, trim_func), 2)

    def test_all_trips_3(self):
        map = Map(1, 2, 3)
        map.append(1, 3, 1)
        map.append(3, 1, 1)
        accept_func = lambda step, distance: True
        trim_func   = lambda step, distance: step > 5
        self.assertEqual(map.all_trips(1, 3, accept_func, trim_func), 3)

    def test_all_trips_4(self):
        map = Map(1, 2, 3)
        map.append(1, 3, 10)
        map.append(3, 1, 1)
        accept_func = lambda step, distance: distance <= 12
        trim_func   = lambda step, distance: distance > 12
        self.assertEqual(map.all_trips(1, 3, accept_func, trim_func), 1)

        accept_func = lambda step, distance: distance <= 21
        trim_func   = lambda step, distance: distance > 21
        self.assertEqual(map.all_trips(1, 3, accept_func, trim_func), 2)


if __name__ == '__main__':
    unittest.main()
