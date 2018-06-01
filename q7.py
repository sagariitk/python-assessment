class Human:
	def __init__(self, name, gender ):
      self.name = name
      self.gender = gender

class Employee(Human):
	def __init__(self, first, last, id , company, salary ):
        Human.__init__(self,first, last)
        self.id = id
        self.company = company
        self.salary = salary
    def employee(self):
    	return(self.name, self.company, self.salary)


