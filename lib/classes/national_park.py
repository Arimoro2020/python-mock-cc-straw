class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        NationalPark.all.append(self)


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception("value must be a string and cannot be changed if exists.")

        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        from classes.trip import Trip
        if isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        from classes.trip import Trip
        return len([trip for trip in Trip.all if trip.national_park == self])
    
    def best_visitor(self):
        from classes.trip import Trip
        visitor_list = [trip.visitor for trip in Trip.all if trip.national_park == self]
        best_one = {}
        for visitor in visitor_list:
            if visitor in best_one:
                best_one[visitor] += 1
            else:
                best_one[visitor] = 1
        best_list = list(best_one.items())
        sorted_best_list = sorted(best_list, key=lambda x: x[1], reverse= True)
        return sorted_best_list[0][0]
     
        

