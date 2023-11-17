import pytest
from television import Television

def test_init():
    tv = Television()

    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)


def test_power():
    tv = Television()


    tv.power() 
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.power()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

def test_mute():
    tv = Television()
    
    tv.power()
    tv.volume_up()
    tv.mute()
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.mute()
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 1" in str(tv)

    tv.power()
    tv.mute()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 1" in str(tv)

    tv.mute()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 1" in str(tv)


def test_channel_up():
    tv = Television()

    tv.channel_up()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.power()
    tv.channel_up()
    assert "Power = True" in str(tv)
    assert "Channel = 1" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()

    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)


def test_channel_down():
    tv = Television()

    tv.channel_down()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv) 


    tv.power()
    tv.channel_down()
    assert "Power = True" in str(tv)
    assert "Channel = 3" in str(tv)
    assert "Volume = 0" in str(tv)

   
    

def test_volume_up():
    tv = Television()

    tv.volume_up()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.power()
    tv.volume_up()
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 1" in str(tv)

    tv.mute() 
    tv.volume_up() 
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 2" in str(tv)

    tv.volume_up()
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 2" in str(tv)

    

def test_volume_down():
    tv = Television()

    tv.volume_down()
    assert "Power = False" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.power() 
    tv.volume_up() 
    tv.volume_up() 

    tv.volume_down()
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 1" in str(tv)

    tv.mute()
    tv.volume_down() 
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)

    tv.volume_down()
    assert "Power = True" in str(tv)
    assert "Channel = 0" in str(tv)
    assert "Volume = 0" in str(tv)
    

    
if __name__ == "__main__":
    pytest.main()
