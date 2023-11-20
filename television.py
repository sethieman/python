class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''All default instance variables are set in this method'''
        
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self) -> None:
        '''This method is used to turn the tv on and off by changing the
            value of the status variable.'''


        self.__status = not self.__status


    def mute(self) -> None:
        '''This method is used to mute and unmute the tv when it is on
            by changing the value of the muted variable.'''


        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self) -> None:
        '''This method is used to increase the tv channel. If it is at the maximum,
            then it loops back around to the minimum channel.'''

        if self.__status: 
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    
    def channel_down(self) -> None:
        '''This method is used to decrease the tv channel. If it is at the minimum,
            then it loops around to the maximum channel.'''

        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1


    def volume_up(self) -> None:
        '''This method is used to turn the volume up to at most the MAX_VOLUME, when the
            tv is on. If the tv was muted, changing the volume will unmite it.'''

        if self.__status:
            if self.__volume == Television.MAX_VOLUME and self.__muted:
                self.__muted = not self.__muted
                
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1
                self.__muted = False


    def volume_down(self) -> None:
        '''This method is used to turn the volume down to at least the MIN_VOLUME, when the
            tv is on. If the tv was muted, changing the volume will unmite it.'''

        if self.__status:
            if self.__volume == Television.MIN_VOLUME and self.__muted:
                self.__muted = not self.__muted
                
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -=1
                self.__muted = False   

    def __str__(self) -> str:
        '''This methods sends the values of the tv object to be displayed.'''

        if self.__muted:
            current_volume = MIN_VOLUME
        else:
            current_volume = self.__volume
            
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {current_volume}"
    
