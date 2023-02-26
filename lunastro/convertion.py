class Measurement:
    def lightyeardist_to_miles(self, lightyears):
        return lightyears * 5880000000000
    
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
      
    
