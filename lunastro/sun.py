import math
import datetime


# start by calculating julian date
class Sun:
    def __init__(self):

        self.dayMs = 1000 * 60 * 60 * 24
        self.J1970 = 2440588
        self.J2000 = 2451545

    def toJulian(self, date):
        return date.timestamp() / self.dayMs - 0.5 + self.J1970

    def fromJulian(self, j):
        return datetime.datetime.fromtimestamp((j + 0.5 - self.J1970) * self.dayMs)

    def toDays(self):
        date = datetime.datetime.now()
        return self.toJulian(date) - self.J2000

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
        temptwo = math.cos(2 * g)
        # solar distance is in astronomical units
        solardistance = 1.00014 - 0.01671 * tmp - 0.00014 * temptwo
        return solardistance * 92955807.3  # miles

    def solar_declination(self):
        # Get the current date (in UTC)
        now = datetime.datetime.utcnow()
        day_of_year = now.timetuple().tm_yday
        solar_declination = -23.45 * math.cos(math.radians((360 / 365) * (day_of_year + 10)))
        return solar_declination


    def observerAngle(self, height):
        return -2.076 * math.sqrt(height) / 60
    
    
    
    def eclipticlongitude(self, anomaly):
        tmp = math.pi / 180 * (
        1.9148 * math.sin(anomaly) + 0.02 * math.sin(2 * anomaly) + 0.0003 * math.sin(3 * anomaly))
        sectemp = math.pi / 180 * 102.9372
        return tmp + sectemp + math.pi



    def rightAscension(self, l, b):
        e = math.pi / 180 * 23.4397
        return math.atan2(math.sin(l) * math.cos(e) - math.tan(b) * math.sin(e), math.cos(l))

    def azimuth(self, h, phi, declination):
        return math.atan2(math.sin(h), math.cos(h) * math.sin(phi) - math.tan(declination) * math.cos(phi))



    def hourangle(self):
        # it is approximate (doesn't take into account minutes)
        if datetime.datetime.now().hour > 12:
            return 15 * (datetime.datetime.now().hour - 12)
        else:
            return 15 * (-(datetime.datetime.now().hour) + 12)
            
    def mean_solar_time(self, longitude):
        solartime = self.get_julian_date() - longitude/360
        return solartime # returns in approximate mean solar time
   
    def solar_mean_anomaly(self, longitude):
        solartime = self.mean_solar_time(longitude)
        anomaly = (357.5291 + 0.98560028 * solartime)%360
        return anomaly
    
    def center_equation(self, longitude):
        m = self.solar_mean_anomaly(longitude)
        c = 1.9148*math.sin(m) + 0.02 * math.sin(2 * m) + 0.0003*math.sin(3*m)
        return c
    
    def moon_alt_az(self, lat, lon, date):
        # Convert latitude and longitude to radians
        lat = math.radians(lat)
        lon = math.radians(lon)

        # Calculate the Julian date
        J2000 = 2451545
        J = date.timestamp() / 86400 + 2440587.5 - J2000

        # Calculate the moon's position in radians
        N = math.radians((125.1228 - 0.0529538083 * J) % 360)
        i = math.radians(5.1454)
        w = math.radians((318.0634 + 0.1643573223 * J) % 360)
        a = 60.2666
        e = 0.054900
        M = math.radians((115.3654 + 13.0649929509 * J) % 360)
        E = M + e * math.sin(M) * (1.0 + e * math.cos(M))
        xv = a * (math.cos(E) - e)
        yv = a * (math.sqrt(1.0 - e * e) * math.sin(E))
        v = math.atan2(yv, xv)
        r = math.sqrt(xv * xv + yv * yv)
        xh = r * (math.cos(N) * math.cos(v + w) - math.sin(N) * math.sin(v + w) * math.cos(i))
        yh = r * (math.sin(N) * math.cos(v + w) + math.cos(N) * math.sin(v + w) * math.cos(i))
        zh = r * (math.sin(v + w) * math.sin(i))

        # Calculate the Greenwich sidereal time
        JD = date.timestamp() / 86400 + 2440587.5
        T = (JD - 2451545.0) / 36525
        L0 = math.radians(280.4665 + 36000.7698 * T)
        dL = math.radians(218.3165 + 481267.8813 * T)
        GMST0 = L0 + dL
        SIDTIME = GMST0 + lon

        # Calculate the moon's altitude and azimuth
        HA = SIDTIME - math.degrees(math.atan2(yh, xh))
        alt = math.asin(zh / r)
        az = math.degrees(
            math.atan2(math.sin(HA), math.cos(HA) * math.sin(lat) - math.tan(math.asin(zh / r)) * math.cos(lat)))
        if az < 0:
            az += 360

        return alt, az





