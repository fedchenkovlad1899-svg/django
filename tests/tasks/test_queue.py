import unittest
import random

from src.task_manager.unique_queue import UniqueQueue, EmptyQueueError


class TestUniqueQueue(unittest.TestCase):

    def setUp(self):
        strategy = "LIFO"
        self.queue = UniqueQueue(strategy)


    def test_no_exist_strategy(self):
        with self.assertRaises(TypeError):
            queue = UniqueQueue("LIFA")


    def test_add_item_to_queue(self):
        item_1 = 5
        self.queue.add(item_1)
        item = self.queue.storage[0]
        self.assertEqual(item_1,item)


    def test_add_and_get_item_from_queue(self):
        item_1 = 5
        self.queue.add(item_1)
        item = self.queue.remove()
        self.assertEqual(item_1,item)


    def test_add_and_get_multi_value_from_queue(self):
        item_1 = 5
        item_2 = 4
        item_3 = 3
        self.queue.add(item_1)
        self.queue.add(item_2)
        self.queue.add(item_3)
        item = self.queue.remove()
        self.assertEqual(item_1,item)
        item = self.queue.remove()
        self.assertEqual(item_2,item)
        item = self.queue.remove()
        self.assertEqual(item_3,item)

    def test_add_many_random_items(self):
        item_1 = 5
        self.queue.add(item_1)
        for _ in range(10):
            self.queue.add(random.randint(10,20))
        item = self.queue.remove()
        self.assertEqual(item_1,item)

    def test_get_item_from_empty_queue(self):
        with self.assertRaises(EmptyQueueError):
            self.queue.remove()

    def test_len_uniq_queue(self):
        item_1 = 3
        item_2 = 4
        self.queue.add(item_1)
        self.assertEqual(self.queue.len_uniq_queue(),1)
        self.queue.add(item_2)
        self.assertEqual(self.queue.len_uniq_queue(), 2)

    def test_len_empty_queue(self):
        len = self.queue.len_uniq_queue()
        self.assertEqual(0, len)

    def test_len_duplicate_doesnt_change(self):
        item_1 = 3
        item_2 = 3
        self.queue.add(item_1)
        self.assertEqual(self.queue.len_uniq_queue(),1)
        self.queue.add(item_2)
        self.assertEqual(self.queue.len_uniq_queue(), 1)

    def test_last_item(self):
        item_1 = 5
        self.queue.add(item_1)
        self.assertEqual(item_1,self.queue.last_item())
        item_2 = 7
        self.queue.add(item_2)
        self.assertEqual(item_2, self.queue.last_item())


if __name__ == '__main__':
    unittest.main()