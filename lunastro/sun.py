import math
import datetime
import pytz


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
    
    def altitude(self, latitude, declination):
        return 90 - (latitude + declination) # returns in degrees
    

    def sun_azimuth(self, lat, lon):
        # Get the current date and time in the observer's time zone
        now = datetime.datetime.now(pytz.timezone('US/Pacific'))

        # Convert the observer's latitude and longitude to radians
        lat = math.radians(lat)
        lon = math.radians(lon)

        # Calculate the observer's local sidereal time
        gst = now.astimezone(pytz.utc).strftime('%H:%M:%S')
        lst = (datetime.datetime.strptime(gst, '%H:%M:%S') + datetime.timedelta(hours=lon / math.pi * 12)).time()

        # Calculate the Sun's right ascension and declination for the current date and time
        d = now.date()
        n = (datetime.datetime(d.year, d.month, d.day, tzinfo=pytz.utc) - datetime.datetime(2000, 1, 1, 12,
                                                                                            tzinfo=pytz.utc)).days + 1
        g = 357.529 + 0.98560028 * n
        g = math.radians(g % 360)
        dec = math.asin(0.39779 * math.sin(g))
        ra = math.atan2(math.cos(g), 0.91746 * math.tan(dec))
        if ra < 0:
            ra += 2 * math.pi

        # Calculate the Sun's hour angle
        ha = math.radians((lst.hour + lst.minute / 60 + lst.second / 3600) * 15 - math.degrees(ra))

        # Calculate the Sun's azimuth using the formula
        sin_az = math.sin(ha) / (math.cos(lat) * math.tan(dec) - math.sin(lat) * math.cos(ha))
        cos_az = (math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(ha))
        azimuth = math.degrees(math.atan2(sin_az, cos_az))

        # Convert the azimuth to a compass direction
        if azimuth < 0:
            azimuth += 360
        if azimuth > 360:
            azimuth -= 360
        if azimuth < 11.25 or azimuth >= 348.75:
            return 'N'
        elif azimuth < 33.75:
            return 'NNE'
        elif azimuth < 56.25:
            return 'NE'
        elif azimuth < 78.75:
            return 'ENE'
        elif azimuth < 101.25:
            return 'E'
        elif azimuth < 123.75:
            return 'ESE'
        elif azimuth < 146.25:
            return 'SE'
        elif azimuth < 168.75:
            return 'SSE'
        elif azimuth < 191.25:
            return 'S'
        elif azimuth < 213.75:
            return 'SSW'
        elif azimuth < 236.25:
            return 'SW'
        elif azimuth < 258.75:
            return 'WSW'
        elif azimuth < 281.25:
            return 'W'
        elif azimuth < 303.75:
            return 'WNW'
        elif azimuth < 326.25:
            return 'NW'
        else:
            return 'NNW'





