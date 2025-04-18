import unittest
from hashmap import HashMap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hm = HashMap()

    def test_empty_get(self):
        # getting a non‑existent key returns None
        self.assertIsNone(self.hm.get("nothing"))

    def test_put_and_get(self):
        self.hm.put("apple", 1)
        self.assertEqual(self.hm.get("apple"), 1)

    def test_update_value(self):
        self.hm.put("key", "first")
        self.hm.put("key", "second")
        self.assertEqual(self.hm.get("key"), "second")

    def test_collision_and_linear_probing(self):
        # craft two different keys that collide under capacity=2
        # ex: "ab" and "ba" both sum to same ASCII total
        k1 = "ab"
        k2 = "ba"
        self.assertEqual(self.hm.hash(k1), self.hm.hash(k2))
        self.hm.put(k1, 100)
        self.hm.put(k2, 200)
        self.assertEqual(self.hm.get(k1), 100)
        self.assertEqual(self.hm.get(k2), 200)

    def test_rehashing_increases_capacity_and_preserves_items(self):
        initial_cap = self.hm.capacity
        # Insert enough items to force at least one rehash:
        # since you rehash whenever size >= capacity//2, inserting `initial_cap`
        # items will always trigger at least one resize.
        for i in range(initial_cap):
            self.hm.put(f"key{i}", i)

        # 1) capacity must have gone up
        self.assertGreater(self.hm.capacity, initial_cap,
                           f"Capacity should increase beyond {initial_cap}")

        # 2) every key must still map to its correct value
        for i in range(initial_cap):
            self.assertEqual(self.hm.get(f"key{i}"), i,
                             f"After resize, key key{i} should still return {i}")


if __name__ == "__main__":
    unittest.main()