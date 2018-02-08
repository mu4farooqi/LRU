import unittest
from LRU import LRUCache, LRUCacheLibrary

# You can replace it with `LRUCacheLibrary` to test other implementation
LRU_Testing = LRUCache


class LRUTesting(unittest.TestCase):

    @staticmethod
    def lru_testing_utility(commands, inputs):
        """
        Commands will be in following format:
            ['init', 'put', 'get', 'put', 'put', 'get']
        And inputs, which corresponds to commands, will be in following format:
            [2, [1,1], 1, [2,2], [3,3], 3]
        :param commands: Commands, which will dictate what do we want to do with LRU Cache
        :param inputs:  Inputs which will be fed along with the commands
        """
        assert len(commands) == len(inputs)

        cache = None
        output = []
        for index in range(len(commands)):
            if commands[index] == 'init':
                cache = LRU_Testing(inputs[index])
                output.append(None)
            elif commands[index] == 'get':
                output.append(cache.get(inputs[index]))
            elif commands[index] == 'put':
                output.append(cache.put(inputs[index][0], inputs[index][1]))
            else:
                raise Exception("Command is not Value, it should be init, get or put")

        return output

    def test_lru_1(self):
        """
        When size of LRU cache is zero (which is highly unlikely), it should just return error (-1) for both get and put
        """
        commands = ['init', 'put', 'get']
        inputs = [0, [1, 1], 1]
        output = self.lru_testing_utility(commands, inputs)
        assert output == [None, -1, -1]

    def test_lru_2(self):
        """
        when size of LRU cache is unity. It should work fine
        """
        commands = ['init', 'put', 'get', 'put', 'get', 'get']
        inputs = [1, [1, 1], 1, [2, 2], 2, 1]
        output = self.lru_testing_utility(commands, inputs)
        assert output == [None, None, 1, None, 2, -1]

    def test_lru_3(self):
        """
        When we get an element from cache, it should be moved to start of the cache (become most recently used)
        """
        commands = ['init', 'put', 'put', 'get', 'put', 'get', 'get']
        inputs = [2, [1, 1], [2, 2], 1, [3, 3], 2, 1]
        output = self.lru_testing_utility(commands, inputs)
        assert output == [None, None, None, 1, None, -1, 1]

    def test_lru_4(self):
        """
        When we try to insert an element which is already present in cache, then cache should make it most recently used 
        and update its value
        """
        commands = ['init', 'put', 'put', 'put', 'get', 'put', 'put', 'get', 'get']
        inputs = [3, [1, 1], [2, 2], [3, 3], 1, [1, 2], [4, 4], 1, 2]
        output = self.lru_testing_utility(commands, inputs)
        assert output == [None, None, None, None, 1, None, None, 2, -1]

    def test_lru_5(self):
        """
        When there is no more space for cache to accommodate a new key, it should remove least recently used element
        """
        commands = ['init', 'put', 'put', 'put', 'get']
        inputs = [2, [1, 1], [2, 2], [3, 3], 1]
        output = self.lru_testing_utility(commands, inputs)
        assert output == [None, None, None, None, -1]

    def test_lru_6(self):
        """
        All elements which are inserted can be retrieved too
        """
        commands = ['init', 'put', 'put', 'put', 'get', 'get', 'get']
        inputs = [3, [1, 1], [2, 2], [3, 3], 1, 2, 3]
        output = self.lru_testing_utility(commands, inputs)
        assert output == [None, None, None, None, 1, 2, 3]


if __name__ == "__main__":
    unittest.main()



