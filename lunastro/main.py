import datetime

class myMoon:
    def __init__(self):
        self.lunartime = 29.530588853

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





    def get_lunar_age(self):
        percent = self.get_lunar_age_percent()
        age = percent * self.lunartime
        return age


    def get_lunar_age_percent(self):
        julian_date = self.get_julian_date()
        tmp = (julian_date - 2451550.1) / self.lunartime
        percent = self.normalize(tmp)
        return percent


    def normalize(self,value):
        value = value - int(value)
        if value < 0:
            value = value + 1
        return value

    def get_lunar_phase(self):
        age = self.get_lunar_age()
        if age < 1.84566:
            return "new moon"
        elif age < 5.53699:
            return "waxing crescent"
        elif age < 9.22831:
            return "first quarter"
        elif age < 12.91963:
            return "waxing gibbous"
        elif age < 16.61096:
            return "full"
        elif age < 20.30228:
            return 'waning gibbous'
        elif age < 23.99361:
            return "third quarter"
        elif age < 27.68493:
            return "waning crescent"

        # in case it has just finished it's cycle
        return "new"
    
    

