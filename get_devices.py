import json
import pandas as pd


def read_query():
    with open('query.json') as q:
        q_txt = q.read()
    query_dict = json.loads(q_txt)
    return query_dict


def strip_string(existing_value):
    new_value = existing_value[1:-2]
    return new_value


def create_dataframe(logger):
    query_dict = read_query()

    devices_df = pd.read_excel("second-watch-devices.xlsx")
    name_col = devices_df['Name']
    name_col_edited = name_col.apply(strip_string)
    devices_df['Name'] = name_col_edited

    # print(devices_df.head(5))

    guids_df = pd.DataFrame(columns=['Name', 'GUID'])

    for entity in query_dict['data']['actor']['entitySearch']['results']['entities']:
        name = entity['name']
        guid = entity['guid']

        row = [name, guid]
        guids_df.loc[len(guids_df)] = row

    all_df = pd.merge(devices_df, guids_df, on='Name', how='outer')

    # print(len(all_df))
    # print(all_df.head(5))

    all_df.dropna(inplace=True)
    all_df_drop = all_df[all_df.Team != 'Legacy']

    # print(len(all_df))
    # print(all_df.head(3))
    # logger.info(all_df_drop['Team'].value_counts())

    logger.info(f'\nDataframe created successfully. {len(all_df_drop)} 2W devices with ownership found.')

    return all_df_drop
