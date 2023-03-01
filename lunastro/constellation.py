class Stellar:
            def getViewableConstellations(self, latitude):
                        constellations = {
                              "aquarius": 0,
                              "aries": 2,
                              "cancer": 2,
                              "capricornus": 1,
                              "gemini": 2,
                              "leo": 0,
                              "libra": 1,
                              "ophiuchus":0,
                              'pisces': 0,
                              'sagittarius':1,
                              'scorpius':1,
                              'taurus': 0,
                              'virgo': 0,
                              'andromeda': 2,
                              'aquila': 0,
                              'ara': 1,
                              "argo navis: Carina Puppis Vela": 1,
                              'auriga': 2,
                              'Boötes': 2,
                              'Canis Major': 1,
                              'Canis Minor': 0,
                              'cassiopeia': 2,
                              'centaurus': 1,
                              'cepheus': 1,
                              'cetus': 0,
                              'coma berenices': 1,
                              'corona australis': 1,
                              'corona borealis': 2,
                              'corvus and crater': 1,
                              'cygnus': 2,
                              'delphinus': 2,
                              'draco': 2,
                              'equuleus': 2,
                              'eridanus': 0,
                              'hercules': 2,
                              'hydra': 0,
                              'lepus': 1,
                              'lupus': 1,
                              'lyra': 2,
                              'orion': 0,
                              'pegasus': 2,
                              'perseus': 2,
                              'piscis austrinus': 1,
                              'sagitta': 2,
                              'serpens': 0,
                              'triangulum': 2,
                              'ursa major': 2,
                              'ursa minor': 2,
                              # animal constellations
                              'apus': 1,
                              'camelopardalis': 2,
                              'canes venatici': 2,
                              'chameleon': 1,
                              'comlumba': 1,
                              'dorado': 1,
                              'grus': 1,
                              'hydrus':1,
                              'indus':1,
                              'lacerta': 2,
                              'leo minor': 2,
                              'lynx': 2,
                              'monoceros': 0,
                              'musca': 1,
                              'pavo': 1,
                              'phoenix': 1,
                              'tucana': 1,
                              'volans': 1,
                              'vulpecula': 2, 
                              # modern constellations
                              'antlia': 1,
                              'caelum': 1,
                              'circinus': 1,
                              'crux': 1,
                              'fornax': 1,
                              'horologium': 1,
                              'mensa': 1,
                              'microscopium':1,
                              'norma': 1,
                              'octans': 1,
                              'pictor': 1,
                              'pyxis': 1,
                              'reticulum': 1,
                              'sculptor': 1,
                              'scutum': 1,
                              'sextans': 0,
                              'telescsopium': 1,
                              'triangulum australe': 1,
                        }
                        hemisphere = 0
                        if latitude > 0:
                            hemisphere = 2
                        else:
                            hemisphere = 1

                        viewable = []
                        for k,v in constellations.items():
                            if v == hemisphere:
                                viewable.append(k)
                            if v == 0:
                                viewable.append(k)


                        return viewable


