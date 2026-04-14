import pytest
from television import *


def test_init():
    tv1 = Television()
    assert str(tv1) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    tv2 = Television()
    tv2.power()
    assert str(tv2) == "Power = True, Channel = 0, Volume = 0"
    tv2.power()
    assert str(tv2) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    tv3 = Television()
    tv3.power()
    tv3.volume_up()
    tv3.mute()
    assert str(tv3) == "Power = True, Channel = 0, Volume = 0"
    tv3.mute()
    assert str(tv3) == "Power = True, Channel = 0, Volume = 1"
    tv3.power()
    tv3.mute()
    assert str(tv3) == "Power = False, Channel = 0, Volume = 1"
    tv3.mute()
    assert str(tv3) == "Power = False, Channel = 0, Volume = 1"


def test_channel_up():
    tv4 = Television()
    tv4.channel_up()
    assert str(tv4) == "Power = False, Channel = 0, Volume = 0"
    tv4.power()
    tv4.channel_up()
    assert str(tv4) == "Power = True, Channel = 1, Volume = 0"
    tv4.channel_up()
    assert str(tv4) == "Power = True, Channel = 2, Volume = 0"
    tv4.channel_up()
    assert str(tv4) == "Power = True, Channel = 3, Volume = 0"
    tv4.channel_up()
    assert str(tv4) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    tv5 = Television()
    tv5.channel_down()
    assert str(tv5) == "Power = False, Channel = 0, Volume = 0"
    tv5.power()
    tv5.channel_down()
    assert str(tv5) == "Power = True, Channel = 3, Volume = 0"
    tv5.channel_down()
    assert str(tv5) == "Power = True, Channel = 2, Volume = 0"
    tv5.channel_down()
    assert str(tv5) == "Power = True, Channel = 1, Volume = 0"
    tv5.channel_down()
    assert str(tv5) == "Power = True, Channel = 0, Volume = 0"


def test_volume_up():
    tv6 = Television()
    tv6.volume_up()
    assert str(tv6) == "Power = False, Channel = 0, Volume = 0"
    tv6.power()
    tv6.volume_up()
    assert str(tv6) == "Power = True, Channel = 0, Volume = 1"
    tv6.mute()
    tv6.volume_up()
    assert str(tv6) == "Power = True, Channel = 0, Volume = 2"
    tv6.volume_up()
    assert str(tv6) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    tv7 = Television()
    tv7.power()
    tv7.volume_up()
    tv7.volume_up()
    tv7.power()
    tv7.volume_down()
    assert str(tv7) == "Power = False, Channel = 0, Volume = 2"
    tv7.power()
    tv7.volume_down()
    assert str(tv7) == "Power = True, Channel = 0, Volume = 1"
    tv7.mute()
    tv7.volume_down()
    assert str(tv7) == "Power = True, Channel = 0, Volume = 0"
    tv7.volume_down()
    assert str(tv7) == "Power = True, Channel = 0, Volume = 0"



if __name__ == "__main__":
    pytest.main()


