class Measurement:
    def lightyeardist_to_miles(self, lightyears):
        return lightyears * 5880000000000
    
    def lightyeardist_to_kilometers(self, lightyears):
        return lightyears * 149597870.7
    
    def kilometers_to_lightyeardist(self, kilometers):
        return kilometers / 149597870.7
    
    def miles_to_lightyeardist(self, miles):
        return miles / 5880000000000
   
    def miles_to_au(self, miles):
        return miles / 92955807.267433 
      
    def au_to_miles(self, au):
        return au * 92955807.267433 
      
    def miles_to_parsec(self, miles):
        return miles / self.lightyeardist_to_miles(3.26)
      
    def parsec_to_miles(self, parsecs):
        return self.lightyeardist_to_miles(3.26) * parsecs
    
    def au_to_kilometers(self, au):
        return au * 149597870.7
    
    def kilometers_to_au(self, kilometers, rounded):
        if rounded == True:
            return kilometers // 149597870.7
        else:
            return kilometers / 149597870.7
    
    def kilometers_to_parsec(self, kilometers):
        return kilometers / self.lightyeardist_to_kilometers(3.26)
    
    def parsec_to_kilometers(self, parsecs):
        return self.lightyeardist_to_kilometers(3.26) * parsecs
    
    
