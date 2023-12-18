import unittest
from main import Metrics, test_echo
import re


class TestMetrics(unittest.TestCase):
    def setUp(self):
        self.metrics = Metrics()
    
    def test_cpu(self):
        res = self.metrics.get_cpu()
        self.assertTrue(len(res) > 0)
        for cpu in res:
            regexp_result = re.findall(r"^[0-9]+$", cpu)
            self.assertTrue(regexp_result)
    
    def tearDown(self):
        pass

class TestEchoFunc(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_func(self):
        res = test_echo()
        self.assertEqual(res, "test echo")


if __name__ == "__main__":
    unittest.main()