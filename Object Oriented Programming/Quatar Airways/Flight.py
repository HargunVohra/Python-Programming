class Flight:
    def __init__(self, FlightNumber, FlightName, StartPoint, EndPoint, StartDateTime, EndDateTime, TotalSeats, SeatsBooked, Bookings):
        
        self.__FlightNumber = FlightNumber
        self.__FlightName = FlightName
        self.__StartPoint = StartPoint
        self.__EndPoint = EndPoint
        self.__StartDateTime = StartDateTime
        self.__EndDateTime = EndDateTime
        self.__TotalSeats = TotalSeats
        self.__SeatsBooked = SeatsBooked
        self.__Bookings = Bookings
        
    @property
    def FlightNumber(self):
        return self.__FlightNumber
    
    @FlightNumber.setter
    def FlightNumber(self, FlightNumber):
        self.__FlightNumber = FlightNumber
        
    @property
    def FlightName(self):
        return self.__FlightName
    
    @FlightName.setter
    def FlightName(self, FlightName):
        self.__FlightName = FlightName
        
        
    @property
    def StartPoint(self):
        return self.__StartPoint
    
    @StartPoint.setter
    def StartPoint(self, StartPoint):
        self.__StartPoint = StartPoint
        
        
    @property
    def EndPoint(self):
        return self.__EndPoint
    
    @EndPoint.setter
    def EndPoint(self, EndPoint):
        self.__EndPoint = EndPoint
        
        
    @property
    def StartDateTime(self):
        return self.__StartDateTime
    
    @StartDateTime.setter
    def StartDateTime(self, StartDateTime):
        self.__StartDateTime = StartDateTime
        
        
    @property
    def EndDateTime(self):
        return self.__EndDateTime
    
    @EndDateTime.setter
    def EndDateTime(self, EndDateTime):
        self.__EndDateTime = EndDateTime
        
        
    @property
    def TotalSeats(self):
        return self.__TotalSeats
    
    @TotalSeats.setter
    def TotalSeats(self, TotalSeats):
        self.__TotalSeats = TotalSeats
        
        
    @property
    def SeatsBooked(self):
        return self.__SeatsBooked
    
    @SeatsBooked.setter
    def SeatsBooked(self, SeatsBooked):
        self.__SeatsBooked = SeatsBooked
        
        
    @property
    def SeatsAvailable(self):
        return self.__TotalSeats - self.__SeatsBooked
    
    
    @property
    def Bookings(self):
        return self.__Bookings
    
    @Bookings.setter
    def Bookings(self, Bookings):
        self.__Bookings = Bookings