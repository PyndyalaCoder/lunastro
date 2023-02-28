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
    
    def get_lunar_phase_description(self):
        age = self.get_lunar_age()
        if age < 1.84566:
            return "new moon: the marking of the new beginning of the lunar cycle. The new moon shows up around once a month (every 29.5 days). During this time, the moon is in line with the sun, causing its illumination to be around 0%."
        elif age < 5.53699:
            return "waxing crescent: the second phase in the cycle of phases. This Moon phase occurs once a month, rising around 9 AM, and setting around 9 PM, sticking around for approximately 7.38 days before going into the First Quarter phase. "
        elif age < 9.22831:
            return "first quarter: rises around noon and sets around midnight. It’s high in the sky in the evening and makes for excellent viewing."
        elif age < 12.91963:
            return "waxing gibbous: when the lit-up part of the Moon grows from 50.1% to 99.9%. It starts just after the First Quarter Moon and lasts until the Full Moon."
        elif age < 16.61096:
            return "full: when the Sun and the Moon are aligned on opposite sides of Earth, and 100% of the Moon's face is illuminated by the Sun"
        elif age < 20.30228:
            return 'waning gibbous: when the lit-up part of the Moon shrinks from 99.9% to 50.1%. It starts just after Full Moon and lasts until the Third Quarter Moon.'
        elif age < 23.99361:
            return "third quarter: the seventh phase in the cycle of phases. This Moon phase occurs once a month, rising around 12 AM, and setting around 12 PM, almost instantaneously becoming a Waning Crescent."
        elif age < 27.68493:
            return "waning crescent: the eighth and final phase in the cycle of phases. This Moon phase occurs once a month, rising around 3 AM, and setting around 3 PM, sticking around for approximately 7.38 days before going into the New Moon phase."
        
        return "new moon: the marking of the new beginning of the lunar cycle. The new moon shows up around once a month (every 29.5 days). During this time, the moon is in line with the sun, causing its illumination to be around 0%."
    

