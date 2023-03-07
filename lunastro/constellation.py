import math
class Stellar:
           # as of march 6th, I updated the function to make it more accurate, it takes into account height and lat_min/lat_max as well.
           def get_viewable_constellations(self, latitude, height):
                """
                Get a list of viewable constellations based on latitude.

                Args:
                latitude (float): The latitude in degrees.

                Returns:
                list: A list of viewable constellations.
                """
                constellation_data = {
                'Andromeda': {'lat_min': 0, 'lat_max': 90},
                'Aquarius': {'lat_min': -65, 'lat_max': 10},
                'Aquila': {'lat_min': -90, 'lat_max': 50},
                'Aries': {'lat_min': -90, 'lat_max': 60},
                'Auriga': {'lat_min': 0, 'lat_max': 90},
                'Boötes': {'lat_min': 0, 'lat_max': 90},
                'Cancer': {'lat_min': -90, 'lat_max': 60},
                'Canes Venatici': {'lat_min': 0, 'lat_max': 90},
                'Canis Major': {'lat_min': -90, 'lat_max': 60},
                'Capricornus': {'lat_min': -90, 'lat_max': 10},
                'Cassiopeia': {'lat_min': 0, 'lat_max': 90},
                'Centaurus': {'lat_min': -60, 'lat_max': 30},
                'Cepheus': {'lat_min': 0, 'lat_max': 90},
                'Cetus': {'lat_min': -90, 'lat_max': 20},
                'Corona Borealis': {'lat_min': 0, 'lat_max': 90},
                'Corvus': {'lat_min': -60, 'lat_max': 20},
                'Crater': {'lat_min': -90, 'lat_max': 5},
                'Cygnus': {'lat_min': 30, 'lat_max': 90},
                'Delphinus': {'lat_min': 0, 'lat_max': 90},
                'Draco': {'lat_min': 0, 'lat_max': 90},
                'Equuleus': {'lat_min': 0, 'lat_max': 90},
                'Gemini': {'lat_min': -60, 'lat_max': 90},
                'Hercules': {'lat_min': 0, 'lat_max': 90},
                'Hydra': {'lat_min': -60, 'lat_max': 20},
                'Leo': {'lat_min': -90, 'lat_max': 60},
                'Leo Minor': {'lat_min': 0, 'lat_max': 90},
                'Libra': {'lat_min': -60, 'lat_max': 20},
                'Lupus': {'lat_min': -60, 'lat_max': 20},
                'Lynx': {'lat_min': 30, 'lat_max': 90},
                'Lyra': {'lat_min': 30, 'lat_max': 90},
                'Monoceros': {'lat_min': -60, 'lat_max': 20},
                'Ophiuchus': {'lat_min': -80, 'lat_max': 10},
                'Orion': {'lat_min': -85, 'lat_max': 85},
                'Pegasus': {'lat_min': 0, 'lat_max': 90},
                'Perseus': {'lat_min': 0, 'lat_max': 90},
                'Pisces': {'lat_min': -90, 'lat_max': 20},
                'Piscis Austrinus': {'lat_min': -90, 'lat_max': -30},
                'Sagitta': {'lat_min': 0, 'lat_max': 90},
                'Sagittarius': {'lat_min': -55, 'lat_max': 20},
                'Scorpius': {'lat_min': -40, 'lat_max': -55},
                'Sculptor': {'lat_min': -90, 'lat_max': 20},
                'Scutum': {'lat_min': -10, 'lat_max': 90},
                'Serpens': {'lat_min': -80, 'lat_max': 10},
                'Taurus': {'lat_min': -65, 'lat_max': 90},
                'Triangulum': {'lat_min': 0, 'lat_max': 90},
                'Triangulum Australe': {'lat_min': -90, 'lat_max': -25},
                'Ursa Major': {'lat_min': 0, 'lat_max': 90},
                'Ursa Minor': {'lat_min': 0, 'lat_max': 90},
                'Vela': {'lat_min': -60, 'lat_max': -45},
                'Virgo': {'lat_min': -60, 'lat_max': 20},
                'Volans': {'lat_min': -75, 'lat_max': -45},
                'Vulpecula': {'lat_min': 0, 'lat_max': 90}
                        }

                constellations = []
                count = 0
                for name, data in constellation_data.items():
                    # Adjust latitude range based on observer height
                    adj_degrees = 180 / math.pi * math.asin(6371 / (6371 + height))
                    lat_min = max(data['lat_min'] - adj_degrees, -90)
                    lat_max = min(data['lat_max'] + adj_degrees, 90)
                    if latitude >= lat_min and latitude <= lat_max:
                        constellations.append(name)
                        count += 1
                return constellations


