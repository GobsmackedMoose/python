
class Television():
    """
    This has the class variables, and are all meant to be constants. 
    """
    MIN_VOLUME:int = 0
    MAX_VOLUME:int = 2
    MIN_CHANNEL:int = 0 
    MAX_CHANNEL:int = 3
    
    def __init__(self):
        """
        These are the class variables of the television class. 
        """
        self.status:bool = False
        self.muted:bool = False
        self.volume:int = self.MIN_VOLUME
        self.channel:int = self.MIN_CHANNEL

    def power(self):
        """
        This is the power method, which will turn the television on and off when invoked. It will 
        make the variable opposite of what it is when the method is invoked. 
        """
        self.status:bool = not(self.status)

    def mute(self):
        """
        This is the mute method, which will mute or unmute the television when invoked. 
        It will make the variable opposite of what it is when the method is invoked.
        """

        if self.status:
            self.muted:bool = not(self.muted)

    def channel_up(self):
        """
        This is the channel up method, which will increase the channel by 1 when invoked. 
        If the channel is at the maximum channel, it will go back around to the minimum channel.
        """
        if self.status:
            self.channel += 1
            if self.channel > self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL

    def channel_down(self):
        """
        This is the channel down method, which will decrease the channel by 1 when invoked.
        If the channel is at the minimum channel, it will go back around to the maximum channel
        """
        if self.status:
            self.channel -= 1
            if self.channel < self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL

    def volume_up(self):
        """
        The volume up method will increase the volume by 1 when invoked.
        If the volume is at the maximum volume, it will stay at the maximum volume. 
        If the television is muted, it will unmute the television and then increase the volume by 1.
        """
        if self.muted:
            self.muted = False
        if self.status:
            if self.volume < self.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        """
        The volume down method will decrease the volume by 1 when invoked.
        If the volume is at the minimum volume, it will stay at the minimum volume. 
        If the television is muted, it will unmute the television and then decrease the volume by 1.
        """
        
        if self.muted:
            self.muted = False
        if self.status:
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        """
        This is the string representation method for the Television class.
        It returns the power, channel and volume variables. 
        """
        if not(self.muted):
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = 0'
