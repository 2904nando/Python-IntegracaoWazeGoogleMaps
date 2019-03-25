import WazeRouteCalculator
import googlemaps
from datetime import timedelta

API_Google = "*API Google*"

saida = "IBM Tutoia"
chegada = "Jundiai Shopping"

gmaps_key = googlemaps.Client(key=API_Google)

geoResSaida = gmaps_key.geocode(saida)
geoResChegada = gmaps_key.geocode(chegada)

latSaida = geoResSaida[0]['geometry']['location']['lat']
lonSaida = geoResSaida[0]['geometry']['location']['lng']
latChegada = geoResChegada[0]['geometry']['location']['lat']
lonChegada = geoResChegada[0]['geometry']['location']['lng']

saidaCoords = str(latSaida) + ", " + str(lonSaida)
chegadaCoords = str(latChegada) + ", " + str(lonChegada)

region = "US"

route = WazeRouteCalculator.WazeRouteCalculator(saidaCoords, chegadaCoords, region, log_lvl=None)

tempo, distancia = route.calc_route_info()

print("Tempo: " + str(tempo) + " minutos\n" + "Distância: " + str(distancia) + "Km")