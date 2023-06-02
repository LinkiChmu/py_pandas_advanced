import pandas as pd

"""For the dataframe generated from visit_log.csv, create a new column 'source_type' 
 according to the rules:
- if 'traffic_source' is equal to Yandex or Google, then 'source_type' is set to organic;
- for paid and email sources from Russia- ad;
- for paid and email sources not from Russia- other;
- in other cases, parameters are taken from column 'traffic_source' without changes.
"""

log = pd.read_csv('visit_log.csv', sep=';')

log.loc[log.traffic_source.isin(['google', 'yandex']), 'source_type'] = 'organic'
log.loc[log.traffic_source.isin(['paid', 'email']) & (log.region == 'Russia'),
        'source_type'] = 'ad'
log.loc[log.traffic_source.isin(['paid', 'email']) & (log.region != 'Russia'),
        'source_type'] = 'other'
log['source_type'].fillna(log.traffic_source, inplace=True)

print(log.head(16)[['region', 'traffic_source', 'source_type']])
