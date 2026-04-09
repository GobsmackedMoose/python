import unittest
from television import * 


class tests(unittest.TestCase):
    def test_init(self):
        tv1 = Television()
        self.assertEqual(tv1.__str__(), "Power = False, Channel = 0, Volume = 0")
    
    def test_power(self):
        tv2 = Television()
        tv2.power()
        self.assertEqual(tv2.__str__(), "Power = True, Channel = 0, Volume = 0")
        tv2.power()
        self.assertEqual(tv2.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_mute(self):
        tv3 = Television()
        tv3.power()
        tv3.volume_up()
        tv3.mute()
        self.assertEqual(tv3.__str__(), "Power = True, Channel = 0, Volume = 0")
        tv3.mute()
        self.assertEqual(tv3.__str__(), "Power = True, Channel = 0, Volume = 1")
        tv3.power()
        tv3.mute()
        self.assertEqual(tv3.__str__(), "Power = False, Channel = 0, Volume = 1")
        tv3.mute()
        self.assertEqual(tv3.__str__(), "Power = False, Channel = 0, Volume = 1")

    def test_channel_up(self):
        tv4 = Television()
        tv4.channel_up()
        self.assertEqual(tv4.__str__(), "Power = False, Channel = 0, Volume = 0")
        tv4.power()
        tv4.channel_up()
        self.assertEqual(tv4.__str__(), "Power = True, Channel = 1, Volume = 0")
        tv4.channel_up()
        self.assertEqual(tv4.__str__(), "Power = True, Channel = 2, Volume = 0")
        tv4.channel_up()
        self.assertEqual(tv4.__str__(), "Power = True, Channel = 3, Volume = 0")
        tv4.channel_up()
        self.assertEqual(tv4.__str__(), "Power = True, Channel = 0, Volume = 0")

    def test_channel_down(self):
        tv5 = Television()
        tv5.channel_down()
        self.assertEqual(tv5.__str__(), "Power = False, Channel = 0, Volume = 0")
        tv5.power()
        tv5.channel_down()
        self.assertEqual(tv5.__str__(), "Power = True, Channel = 3, Volume = 0")
        tv5.channel_down()
        self.assertEqual(tv5.__str__(), "Power = True, Channel = 2, Volume = 0")
        tv5.channel_down()
        self.assertEqual(tv5.__str__(), "Power = True, Channel = 1, Volume = 0")
        tv5.channel_down()
        self.assertEqual(tv5.__str__(), "Power = True, Channel = 0, Volume = 0")
    
    

if __name__ == '__main__':
    unittest.main()