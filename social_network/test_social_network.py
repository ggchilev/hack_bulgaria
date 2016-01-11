import unittest
from network import SocialNetwork
from panda import Panda


class TestSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.ivo = Panda("Ivo", "fwadwa", "male")
        self.rado = Panda("Rado", "retre", "male")
        self.canko = Panda("Canko", "retre", "male")
        self.network = SocialNetwork()

    def test_has_and_add_panda_in_network(self):
        self.network.add_panda(self.ivo)
        self.assertTrue(self.network.has_panda(self.ivo))

    def test_are_friedns_and_make_friends(self):
        self.network.make_friends(self.ivo, self.rado)
        self.assertTrue(self.network.are_friends(self.ivo, self.rado))

    def test_friends_of(self):
        self.network.make_friends(self.ivo, self.rado)
        self.network.make_friends(self.ivo, self.canko)
        my_list = [self.rado, self.canko]
        #self.assertTrue(self.rado in self.network.friends_of(self.ivo))

    def test_connection_level(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavli", "pavlin@pandamail.com", "male")
        maria = Panda("maria", "maria@pandamail.com", "female")

        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(rado, pavli)
        self.network.make_friends(pavli, maria)

        self.assertEqual(self.network.connection_level(self.ivo, rado), 1)
        self.assertEqual(self.network.connection_level(self.ivo, pavli), 2)
        self.assertEqual(self.network.connection_level(self.ivo, maria), 3)



if __name__ == '__main__':
    unittest.main()