# lunastro
lunastro is a python library for lunar and solar information

<br>
<h1>Lunar Usage:</h1>:
<br>

```python

    
    from lunation.main import myMoon
    # create instance of myMoon
    moon = myMoon()
    
    # functions
    phase = moon.get_lunar_phase() # returns lunar phase
    age = moon.get_lunar_age() # returns lunar age
    percent = moon.get_lunar_age_percent() # returns percent of lunar age
```
The library can also be used to calculate distance from the sun
<br>
<h1> Solar Usage: </h1>

```python

    
    from lunation.sun import Sun
    # instance of Sun
    sun = Sun()
    distance = sun.solardistance() # returns solar distance in astronomical units
```
