import math
class Star:
    def calculate_apparent_brightness(self, absolute_brightness, distance):
        """
        Calculate the apparent brightness of a star based on its absolute brightness and distance.

        Args:
        absolute_brightness (float): The absolute brightness of the star in magnitudes.
        distance (float): The distance to the star in parsecs.

        Returns:
        float: The apparent brightness of the star in magnitudes.
        """
        # Convert distance to parsecs
        distance_pc = distance * 3.26

        # Calculate luminosity using the inverse square law
        luminosity = 10**(-0.4 * (absolute_brightness - 4.83))
        apparent_brightness = absolute_brightness + 5 * math.log10(distance_pc)

        return apparent_brightness
    
    def calculate_star_distance(self, apparent_brightness, absolute_brightness):
        """
        Calculate the distance to a star based on its apparent brightness and absolute brightness.

        Args:
        apparent_brightness (float): The apparent brightness of the star in magnitudes.
        absolute_brightness (float): The absolute brightness of the star in magnitudes.

        Returns:
        float: The distance to the star in parsecs.
        """
        # Convert magnitudes to luminosity
        luminosity_ratio = 100**(0.4 * (apparent_brightness - absolute_brightness))

        # Calculate distance using luminosity and the inverse square law
        distance = math.sqrt(1 / luminosity_ratio)

        # Convert distance to parsecs
        distance_parsecs = distance / 3.26

        return distance_parsecs
    
    def calculate_absolute_brightness(self, apparent_brightness, distance):
        """
        Calculate the absolute brightness of a star based on its apparent brightness and distance.

        Args:
        apparent_brightness (float): The apparent brightness of the star in magnitudes.
        distance (float): The distance to the star in parsecs.

        Returns:
        float: The absolute brightness of the star in magnitudes.
        """
        # Calculate absolute brightness using the formula:
        # absolute_brightness = apparent_brightness - 5 * math.log10(distance) + 5
        absolute_brightness = apparent_brightness - 5 * math.log10(distance) + 5

        return absolute_brightness
      
    

    
