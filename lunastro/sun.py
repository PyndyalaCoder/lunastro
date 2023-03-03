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
    
    def astro_info(self, year, month, day, hour, minute, second, lat, lon):
        # Convert latitude and longitude to radians
        lat_rad = math.radians(lat)
        lon_rad = math.radians(lon)
        ltr = []
        # Calculate the Julian Day (JD) for the given date and time
        jd = 367 * year - 7 * (year + (month + 9) // 12) // 4 + 275 * month // 9 + day + 1721013.5
        jd += (hour + minute / 60 + second / 3600) / 24
        ltr.append(jd)
        # jd, jc, geometric mean longitude, geometric mean anomaly, eccentricity of earth's orbit, equation of center, true longitude, true anomaly, sun's distance from earth (AU), longitude of omega, mean obliquity of ecliptic, sun's right ascension, sun's declination ,local hour angle.

        # Calculate the Julian Century (JC) for the given JD
        jc = (jd - 2451545) / 36525
        ltr.append(jc)

        # Calculate the Geometric Mean Longitude of the Sun (L0) in degrees
        l0 = 280.46646 + jc * (36000.76983 + jc * 0.0003032) % 360
        ltr.append(l0)

        # Calculate the Geometric Mean Anomaly of the Sun (M) in degrees
        m = 357.52911 + jc * (35999.05029 - 0.0001537 * jc)
        ltr.append(m)

        # Calculate the Eccentricity of Earth's Orbit (e)
        e = 0.016708634 - jc * (0.000042037 + 0.0000001267 * jc)
        ltr.append(e)

        # Calculate the Equation of Center (C) in degrees
        c = math.sin(math.radians(m)) * (1.914602 - jc * (0.004817 + 0.000014 * jc)) + math.sin(math.radians(2 * m)) * (0.019993 - 0.000101 * jc) + math.sin(math.radians(3 * m)) * 0.000289
        ltr.append(c)
        
        # Calculate the True Longitude of the Sun (l) in degrees
        l = l0 + c
        ltr.append(l)
        
        # Calculate the True Anomaly of the Sun (v) in degrees
        v = m + c
        ltr.append(v)
        
        # Calculate the Sun's Distance from Earth (r) in Astronomical Units (AU)
        r = 1.000001018 * (1 - e * e) / (1 + e * math.cos(math.radians(v)))
        ltr.append(r)

        # Calculate the Longitude of the Sun's Ascending Node (Omega) in degrees
        omega = 125.04 - 1934.136 * jc
        ltr.append(omega)

        # Calculate the Mean Obliquity of the Ecliptic (epsilon) in degrees
        epsilon = 23.439291 - jc * (0.0130042 + 0.00000016 * jc)
        ltr.append(epsilon)

        # Calculate the Sun's Right Ascension (alpha) in degrees
        alpha = math.degrees(math.atan2(math.cos(math.radians(epsilon)) * math.sin(math.radians(l)), math.cos(math.radians(l))))

        # Convert alpha to the range 0-360 degrees
        alpha = (alpha + 360) % 360
        ltr.append(alpha)

        # Calculate the Sun's Declination (delta) in degrees
        delta = math.degrees(math.asin(math.sin(math.radians(epsilon)) * math.sin(math.radians(l))))
        ltr.append(delta)

        # Calculate the Local Hour Angle (H) in degrees
        H = math.degrees(math.acos((math.sin(math.radians(-0.83)) - math.sin(math.radians(lat_rad)) * math.sin(math.radians(delta))) / (math.cos(math.radians(lat_rad)) * math.cos(math.radians(delta)))))
        ltr.append(H)
        
        return ltr


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





