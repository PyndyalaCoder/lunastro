# lunastro
<strong>lunastro</strong> is a python library for <i>lunar</i> and <i>solar</i> information. It provides <strong>astronomers, data experts, and python developers</strong> with a quick, easy, and accurate approach to get information on <strong>celestial bodies</strong>.

<h1>To install lunastro:</h1>
<br>
As of 2023, <b>Lunastro</b> is only available through pip. <br>
You can run the <b>following</b> command in your <i>terminal</i>

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
    moon_alt_az(lat, lon, date) # altitude and azimuth of the moon
    moon_illumination_percent(phase) # takes special input and returns percentage of moon_illumination
    
    """
    Solar Functions
    """
    solardistance() # returns distance to the sun in miles
    astro_info(year, month, day, hour, minute, second, lat, lon) # returns list with jd, jc, geometric mean longitude, geometric mean anomaly, eccentricity of earth's orbit, equation of center, true longitude, true anomaly, sun's distance from earth (AU), longitude of omega, mean obliquity of ecliptic, sun's right ascension, sun's declination ,local hour angle.
    apparent_magnitude() # returns magnitude of the sun
    solar_declination() # solar declination
    eclipticlongtitude(anomaly) # ecliptic longitude
    rightAscension(galactic_latitude, galactic_longitude) # right Ascension
    sun_azimuth(latitude, longitude) # returns azimuth of the sun as a compass direction (N, S, W, E, NW, NE, SW, SE, NNW, NNE, etc.)
    hourangle() # returns solar hour angle (approximate)
    mean_solar_time(longitude) # returns mean solar time
    solar_mean_anomaly(longitude) # returns anomaly
    center_equation(longitude) # returns center
    altitude(latitude, declination) # returns angle from horizon to the center of the sun disk in degrees
    
    """
    Constellation Function
    """
    get_viewable_constellations(latitude, height) # as of march 6th 2023, the new function calculates viewable constellations while also taking into account lat_max, lat_min of each constellation, as well as the range of constellations he/she can see based on height.
    
    """
    Star Functions
    """
    calculate_apparent_brightness(absolute_brightness, distance) # apparent brightness
    calculate_absolute_brightness(apparent_brightness, distance) # absolute brightness
    calculate_star_distance(apparent_brightness, absolute_brightness) # distance to star in parsecs (1 parsec is 3.2 light years)
```

<h1>Astronomical Measurement Functions:</h1>

```python
    lightyeardist_to_miles(lightyears) # returns miles 
    miles_to_lightyeardist(miles) # returns lightyeardistance
    miles_to_au(miles) # returns astronomical units
    au_to_miles(au) # returns miles from astronomical units
    parsec_to_miles(parsec) # returns miles from parsec (3.26 light years is a parsec)
    miles_to_parsec(miles) # returns parsecs from miles 
    kilometers_to_au(kilometers, rounded) # if rounded is set to true, it rounds value, else ,it returns au from kilometers
    au_to_kilometers(au) # returns kilometers from au
    kilometers_to_parsec(kilometers) # returns parsec from kilometers
    parsec_to_kilometers(parsecs) # returns kilometers from parsecs
    kilometers_to_lightyeardist(kilometers) # returns lightyear dist from kilometers
    lightyeardist_to_kilometers(lightyears) # returns kilometers from lightyears
```

<h1>Usage:</h1>
<br>

To use your functions, make sure to declare an instance of the class:

```python
    # if desiring sun information
    from lunastro import Sun
    sun = Sun()
    
    # if desiring moon information
    from lunastro import myMoon
    moon = myMoon()
    
    # if desiring astronomical conversions
    from lunastro import Measurement
    measure = Measurement()
    
    # if desiring constellation information
    from lunastro import Stellar
    stars = Stellar()
    
    # if desiring star information
    from lunastro import Star
    star_info = Star()
```

<br>

<h1>Input of a Moon Phase:</h1>

In order to <strong>input</strong> a value between 0 and 1 to get the lunar illumination percentage, you can use the following guide:
<br>
| Phase | Name            |
| -----:| --------------- |
| 0     | Full Moon        |
| 0.125  | Waning Gibbous |
| 0.25  | Last Quarter   |
| 0.375   | Waning Crescent  |
| 0.5   | New Moon       |
| 0.625 | Waxing Crescent  |
| 0.75  | First Quarter    |
| 0.875     | Waxing Gibbous |


## Contributing to Lunastro
Thank you for your interest in contributing to Lunastro! Here are a few guidelines to help you get started.

## Getting Started
- Fork the repository on GitHub.
- Clone your forked repository to your local machine.
- Create a new branch for your changes: git checkout -b your-branch-name.
- Make your changes and commit them: git commit -m "Your commit message".
- Push your changes to your forked repository: git push origin your-branch-name.
- Create a pull request (PR) from your forked repository to the main Lunastro repository.

## Code Style
Please follow the PEP 8 style guide for Python code. If you're not sure about something, feel free to ask in your pull request or create an issue.

## Testing
All code changes should include appropriate tests to ensure that the changes work as expected and do not break existing functionality. Please make sure that all tests pass before submitting a pull request.


## Documentation
Please update the documentation as appropriate when making changes to the code. This includes docstrings for functions, as well as updating the README and any other relevant documentation.

## Issues
If you encounter a bug or have a feature request, please open an issue on the GitHub repository. Be as specific as possible in your description of the issue or feature request.

## Review Process
All pull requests will be reviewed by the Lunastro team. Feedback and comments will be provided, and changes may be requested before the pull request is merged.

## Help
If you have any questions about usage, please email <strong>lunastrohelp@gmail.com</strong>. Expect a 1-3 day wait before you receive a response.
