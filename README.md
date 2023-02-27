# lunastro
<strong>lunastro</strong> is a python library for <i>lunar</i> and <i>solar</i> information. It provides <strong>astronomers, data experts, and python developers</strong> with a quick, easy, and accurate approach to get information on <strong>celestial bodies</strong>.

<h1>To install lunastro:</h1>

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
    declination(galactic_latitude, galactic_longitude) # solar declination
    eclipticlongtitude(anomaly) # ecliptic longitude
    rightAscension(galactic_latitude, galactic_longitude) # right Ascension
    azimuth(hour_angle, latitude, declination) # azimuth
    hourangle() # returns solar hour angle (approximate)
    mean_solar_time(longitude) # returns mean solar time
    solar_mean_anomaly(longitude) # returns anomaly
    center_equation(longitude) # returns center
```

<h1>Astronomical Measurement:</h1>

```python
    lightyeardist_to_miles(lightyears) # returns miles 
    miles_to_lightyeardist(miles) # returns lightyeardistance
    miles_to_au(miles) # returns astronomical units
    au_to_miles(au) # returns miles from astronomical units
    parsec_to_miles(parsec) # returns miles from parsec (3.26 light years is a parsec)
    miles_to_parsec(miles) # returns parsecs from miles 
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

