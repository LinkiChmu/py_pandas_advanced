import pandas as pd

"""The statistics of transportation services for the company's customers by types are given:
rzd - rail transport;
auto - road transport;
air - air transportation;
client_base - client addresses.
Create two tables:
1. Table with three types of revenue for each client_id without client's address;
2. Similar table by types of revenue specifying the address of the client.
"""

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
rzd.set_index('client_id', inplace=True)
auto.set_index('client_id', inplace=True)
air.set_index('client_id', inplace=True)
client_base.set_index('client_id', inplace=True)

revenue_merged = rzd.join(auto, how='outer').join(air, how='outer')
revenue_address = revenue_merged.join(client_base, how='left')

print(revenue_merged.head(10))
print(revenue_address.head(10))
