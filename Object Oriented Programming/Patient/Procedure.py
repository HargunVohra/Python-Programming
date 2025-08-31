class Procedure:
    def __init__(self, ProcedureName, ProcedureDate, PractitionerName, ProcedureCharges):
        self.__ProcedureName = ProcedureName
        self.__ProcedureDate = ProcedureDate
        self.__PractitionerName = PractitionerName
        self.__ProcedureCharges = ProcedureCharges
        
    
    def GetProcedureName(self):
        return self.__ProcedureName
    
    def GetProcedureDate(self):
        return self.__ProcedureDate
    
    def GetPractitionerName(self):
        return self.__PractitionerName
    
    def GetProcedureCharges(self):
        return self.__ProcedureCharges
    
    
    def SetProcedureName(self, ProcedureName):
        self.__ProcedureName = ProcedureName
        
    def SetProcedureDate(self, ProcedureDate):
        self.__ProcedureDate = ProcedureDate
        
    def SetPractitionerName(self, PractitionerName):
        self.__PractitionerName = PractitionerName
        
    def SetProcedureCharges(self, ProcedureCharges):
        self.__ProcedureCharges = ProcedureCharges
        