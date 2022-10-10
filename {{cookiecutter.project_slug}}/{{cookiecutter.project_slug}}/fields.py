from dateutil.parser import isoparse
from urllib.parse import urlsplit, urlunsplit, urlunparse, urlencode

import os

FEMA_DATA_COLLECTION_UUID = 'a6f165fa-aee2-4fe5-95f3-97429c28bf82'


def make_table_data(input_obj: dict, skip: list = None) -> list:
    skip = skip or []
    def generate_name(field_name):
        return ' '.join([w.capitalize() for w in field_name.split('_')])
    fields = [
        {'field_name': k, 'value': v, 'name': generate_name(k)}
        for k, v in input_obj.items() if k not in skip
    ]
    return fields


def title(result):
    return result[0]['files'][0]['filename']


def date(result):
    return isoparse(result[0]['year'])


def https_url(result):
    return result[0]['files'][0]['url']


def detail_general_metadata(result):
    return make_table_data(result[0], skip=['files'])


def file_metadata(result):
    return make_table_data(result[0]['files'][0])


def globus_app_link(result):
    url = result[0]['files'][0]['url']
    parsed = urlsplit(url)
    query_params = {'origin_id': FEMA_DATA_COLLECTION_UUID,
                    'origin_path':  os.path.dirname(parsed.path)}
    return urlunsplit(('https', 'app.globus.org', 'file-manager',
                      urlencode(query_params), ''))
