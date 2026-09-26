class employee:
    def __init__(self):
        self.id=123
        self.salary=50000
        self.desig="SDE"

    def travel(self,destination):
        print(f"person is travelling to {destination}")
sam=employee()
print(sam.id)
sam.travel("kerala")
sam.travel("udupi")