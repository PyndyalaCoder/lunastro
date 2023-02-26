# lunastro
lunastro is a python library for lunar and solar information


Installation:

To install lunastro:

```python
    pip install lunastro
```
<br>

<h1>Functions</h1>

```python
    get_lunar_phase() # returns phase
    get_lunar_age() # returns age of moon
    get_lunar_age_percentage() # returns age percentage of moon
    solardistance() # returns distance to the sun in miles
    declination(galactic_latitude, galactic_longtitude) # solar declination
    eclipticlongtitude(anomaly) # ecliptic longtitude
    rightAscension(galactic_latitude, galactic_longtitude) # right Ascension
    azimuth(hour_angle, latitude, declination) # azimuth
    hourangle() # returns solar hour angle (approximate)
```

<h1>Lunar Usage:</h1>:
<br>

```python

    
    from lunation.main import myMoon
    # create instance of myMoon
    moon = myMoon()
    
    # functions
    phase = moon.get_lunar_phase() # returns lunar phase
    age = moon.get_lunar_age() # returns lunar age
    percent = moon.get_lunar_age_percent() # returns percent of lunar age as a decimal
```
The library can also be used to calculate distance from the sun
<br>
<h1> Solar Usage: </h1>

```python

    
    from lunation.sun import Sun
    # instance of Sun
    sun = Sun()
    distance = sun.solardistance() # returns solar distance in miles
```
