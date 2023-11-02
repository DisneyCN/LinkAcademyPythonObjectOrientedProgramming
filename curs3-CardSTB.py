class CardSTB:
    travelCost =3
    def __init__(self,name:str = "Anonim", avabileJourney:int= 0, amount:float =0 ) -> None:
            self.name = name
            self.avabileJourney=avabileJourney
            self.amount=amount
    def __str__(self):
        return f"\nName : \n{self.name} \nAvabile travels: {self.avabileJourney}\nAmount: {self.amount} "
    def validateJourney(self):
        if self.avabileJourney> 0:
             self.avabileJourney-=1
        else:
            return "You must have at least 1 avabile journey"
        

card1 = CardSTB("John",13,200)
print(card1)