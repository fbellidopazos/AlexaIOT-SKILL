import io
import reverse_geocoder as rg

geo = rg.RGeocoder(mode=2, verbose=True, stream=io.StringIO(open('custom_source.csv', encoding='utf-8').read()))
coordinates = (51.5214588,-0.1729636),(9.936033, 76.259952),(37.38605,-122.08385)
results = geo.query(coordinates)
