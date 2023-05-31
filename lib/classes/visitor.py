class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        self._national_parks = []
        self._trips = []
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and 1<= len(value)<= 15 and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception("value must be a string and be 1 to 15 characters long")
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip,Trip):
            self._trips.append(new_trip)
        return [trip for trip in Trip.all if trip.visitor == self]
        
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        from classes.trip import Trip
        if isinstance(new_national_park,NationalPark):
            self._national_parks.append(new_national_park)
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
        