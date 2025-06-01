class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        if self.__hours < 0 or self.__hours > 24:
            raise ValueError("Hours must be between 0 and 24")
        return self.__hours
    
    @property
    def minutes(self):
        if self.__minutes < 0 or self.__minutes > 60:
            raise ValueError("Minutes must be between 0 and 60")
        return self.__minutes
    
    @property
    def seconds(self):
        if self.__seconds < 0 or self.__seconds > 60:
            raise ValueError("Seconds must be between 0 and 60")
        return self.__seconds
    
        
    
    