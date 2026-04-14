class Television():
    """
    This has the class variables, and are all meant to be constants. 
    """
    MIN_VOLUME:int = 0
    MAX_VOLUME:int = 2
    MIN_CHANNEL:int = 0 
    MAX_CHANNEL:int = 3
    
    def __init__(self) -> None:
        """
        These are the class variables of the television class. 
        """
        self.__status:bool = False
        self.__muted:bool = False
        self.__volume:int = Television.MIN_VOLUME
        self.__channel:int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This is the power method, which will turn the television on and off when invoked. It will 
        make the variable opposite of what it is when the method is invoked. 
        """
        self.__status:bool = not(self.__status)

    def mute(self) -> None:
        """
        This is the mute method, which will mute or unmute the television when invoked. 
        It will make the variable opposite of what it is when the method is invoked.
        """
        if self.__status:
            self.__muted:bool = not(self.__muted)

    def channel_up(self) -> None:
        """
        This is the channel up method, which will increase the channel by 1 when invoked. 
        If the channel is at the maximum channel, it will go back around to the minimum channel.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This is the channel down method, which will decrease the channel by 1 when invoked.
        If the channel is at the minimum channel, it will go back around to the maximum channel
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        The volume up method will increase the volume by 1 when invoked.
        If the volume is at the maximum volume, it will stay at the maximum volume. 
        If the television is muted, it will unmute the television and then increase the volume by 1.
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        The volume down method will decrease the volume by 1 when invoked.
        If the volume is at the minimum volume, it will stay at the minimum volume. 
        If the television is muted, it will unmute the television and then decrease the volume by 1.
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        This is the string representation method for the Television class.
        It returns the power, channel and volume variables. 
        """
        if not(self.__muted):
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0'

