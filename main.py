import geopandas as gpd
import json
import pandas as pd
from shapely import geometry, wkt

import db_settings as st


def main():
    df = pd.read_sql(st.query, con=st.engine)
    df.fillna(0, inplace=True)

    gdf = gpd.GeoDataFrame(df)

    geojson_layer = {
        'type': 'FeatureCollection',
        'features': []
    }

    properties = ['cluster_id', 'macro_cluster']

    for _, row in gdf.iterrows():
        feature = {
            'type': 'Feature',
            'properties': {},
            'geometry': {
                'type': 'Polygon',
                'coordinates': []
                }
            }
        poly = wkt.loads(row['geometry'])
        poly_mapped = geometry.mapping(poly)
        poly_coord = poly_mapped['coordinates'][0]
        poly_ = [[[coords[0], coords[1]] for coords in poly_coord]]
        feature['geometry']['coordinates'] = poly_

        for p in properties:
            feature['properties'][p] = row[p]

        geojson_layer['features'].append(feature)

    with open('geo_file.geojson', 'w') as geo_file:
        json.dump(geojson_layer, geo_file)


if __name__ == '__main__':
    main()
