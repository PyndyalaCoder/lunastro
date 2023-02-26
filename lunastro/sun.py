import math
import datetime
# start by calculating julian date
class Sun:
        def get_julian_date(self):
                date = None
                # If no date is provided, use the current date and time
                if date is None:
                    date = datetime.datetime.now()

                # Convert the date to a timestamp in milliseconds
                timestamp = date.timestamp() * 1000

                # Calculate the timezone offset in minutes
                if date.utcoffset():
                    timezone_offset = date.utcoffset().total_seconds() // 60
                else:
                    timezone_offset = 0

                # Calculate the Julian date and return it
                julian_date = (timestamp / 86400000) - (timezone_offset / 1440) + 2440587.5
                return julian_date

        def solardistance(self):
                 juliandate = self.get_julian_date()
                 # days since greenwich noon
                 n = juliandate - 2451545 
                 # positions
                 meanlong = 280.460 + 0.9856474 * n
                 # g is mean anomaly 
                 g = 357.528 + 0.9856003 * n
                 tmp = math.cos(g)
                 temptwo = math.cos(2*g)
                 # solar distance is in astronomical units
                 solardistance = 1.00014 - 0.01671*tmp - 0.00014*temptwo
                 return solardistance * 92955807.3 # miles
  
        def declination(self, l, b):
                e = (math.pi/180) * 23.4397
                return math.asin(math.sin(b) * math.cos(e) + math.cos(b) * math.sin(e) * math.sin(l))
        
        def solarmeananomaly(self, d):
                return math.pi/180 * (357.5291 + 0.98560028 * d)
        
        def eclipticlongtitude(self, anomaly):
                tmp = math.pi/180 * (1.9148 * math.sin(anomaly) + 0.02 * math.sin(2 * anomaly) + 0.0003 * math.sin(3 * anomaly))
                sectemp = math.pi/180 * 102.9372
                return tmp + sectemp + math.pi
        
        
                
        def currentdeclination(self, d):
                s = self.solarmeananomaly(d)
                longtitude = self.eclipticlongtitude(s)
                return self.declination(longtitude, 0)
        
        def siderealtime(self, days, longtitudewest):
                return math.pi/180 * (280.16 + 360.9856235 * days) - longtitudewest
        
        def rightascension(self, l, b):
                e = (math.pi/180) * 23.4397
                return math.atan(math.sin(l) * math.cos(e) - math.tan(b) * math.sin(e), math.cos(l))
                
        def azimuth(self, h, phi, declination):
                return math.atan(math.sin(h), math.cos(h) * math.sin(phi) - math.tan(declination) * math.cos(phi))
        
        def sunazimuth(self, date, latitude, longtitude):
                lw = math.pi/180 * - longtitude
                phi = math.pi/180 * latitude
                tmp = self.currentdeclination(date)
                h = self.siderealtime(date, lw) - tmp
                return self.azimuth(h, phi, tmp)
        
                
                
                
