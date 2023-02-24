import math
# start by calculating julian date
def get_julian_date():
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
 
def solardistance():
         juliandate = get_julian_date()
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
         return solardistance
  
