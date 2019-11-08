import urllib.request
import re

def lookup_place_name(place_code):
    url_tpl = 'http://statistics.gov.scot/id/statistical-geography/{}'
    url = url_tpl.format(place_code)

    with urllib.request.urlopen(url) as response:
        r = response.read()
    
    found = re.findall(r'<h1 class="title">([\w \-\,]*)</h1>', r.decode())
    if not found:
        print(place_code, 'not found')
        place_name = '<not found>'
    else:
        place_name = found[0]
    
    return place_name

def create_place_mapping(place_codes):
    place_mapping = {}
    unique_place_codes = set(place_codes)
    for i, place_code in enumerate(unique_place_codes):
        print(f'looking up {place_code} ({i+1}/{len(unique_place_codes)}).. ')
        place_name = lookup_place_name(place_code)
        place_mapping[place_code] = place_name
        
    return place_mapping


if __name__=='__main__':
    import pandas as pd
    
    src = 'CarbonFootprintBreakdown'
    df = pd.read_csv(f'{src}.csv')
    
    place_mapping = create_place_mapping(df.FeatureCode.unique())

    df_mapping = pd.Series(place_mapping, name='place_name').to_frame()
    df_mapping.index.name = 'FeatureCode'

    df_merged = pd.merge(df, df_mapping, on='FeatureCode')
    df_merged.to_csv(f'{src}+.csv', index=False)
