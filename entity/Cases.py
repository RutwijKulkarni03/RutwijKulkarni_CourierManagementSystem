class Case:
    def __init__(self, caseID, caseDescription):
        self.__caseID = caseID
        self.__caseDescription = caseDescription


    def __str__(self):
        return f"Case(CaseID: {self.__caseID}, CaseDescription: {self.__caseDescription})"
