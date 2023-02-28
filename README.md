# lunastro
<strong>lunastro</strong> is a python library for <i>lunar</i> and <i>solar</i> information. It provides <strong>astronomers, data experts, and python developers</strong> with a quick, easy, and accurate approach to get information on <strong>celestial bodies</strong>.

<h1>To install lunastro:</h1>

```python
    pip install lunastro
```
<br>

<h1>Functions and their output</h1>

```python
    """ 
    Lunar functions
    """
    
    
    get_lunar_phase() # returns the current lunar phase as words
    get_lunar_age() # returns age of moon
    get_lunar_age_percentage() # returns age percentage of moon
    get_lunar_phase_description() # returns description of the current moon phase
    
    """
    Solar Functions
    """
    solardistance() # returns distance to the sun in miles
    declination(galactic_latitude, galactic_longitude) # solar declination
    eclipticlongtitude(anomaly) # ecliptic longitude
    rightAscension(galactic_latitude, galactic_longitude) # right Ascension
    azimuth(hour_angle, latitude, declination) # azimuth
    hourangle() # returns solar hour angle (approximate)
    mean_solar_time(longitude) # returns mean solar time
    solar_mean_anomaly(longitude) # returns anomaly
    center_equation(longitude) # returns center
```

<h1>Astronomical Measurement Functions:</h1>

```python
    lightyeardist_to_miles(lightyears) # returns miles 
    miles_to_lightyeardist(miles) # returns lightyeardistance
    miles_to_au(miles) # returns astronomical units
    au_to_miles(au) # returns miles from astronomical units
    parsec_to_miles(parsec) # returns miles from parsec (3.26 light years is a parsec)
    miles_to_parsec(miles) # returns parsecs from miles 
    kilometers_to_au(self, kilometers, rounded) # if rounded is set to true, it rounds value, else ,it returns au from kilometers
    au_to_kilometers(self, au) # returns kilometers from au
    kilometers_to_parsec(self, kilometers) # returns parsec from kilometers
    parsec_to_kilometers(self, parsecs) # returns kilometers from parsecs
    kilometers_to_lightyeardist(self, kilometers) # returns lightyear dist from kilometers
    lightyeardist_to_kilometers(self, lightyears) # returns kilometers from lightyears
```



