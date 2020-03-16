class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idSet = {}
        for employee in employees:
            idSet[employee.id] = employee
            
        def getImportanceHelper(id):
            employee = idSet[id]
            importanceSum = employee.importance
            for sub in employee.subordinates:
                subEmployee = idSet[sub]
                importanceSum += getImportanceHelper(subEmployee.id)
            return importanceSum
        return getImportanceHelper(id)
        