from {{ cookiecutter.project_slug }} import fields

def get_rfm(search_result):
    if search_result[0].get("remote_file_manifest"):
        return [search_result[0]["remote_file_manifest"]]
    else:
        return []


SEARCH_INDEXES = {
    "fema": {
        "uuid": "{{ cookiecutter.globus_search_index }}",
        "name": "Tutorial",
        "fields": [
            "files",
            "project_metadata",
            ("date", fields.date),
            ("title", fields.title),
            ("detail_general_metadata", fields.detail_general_metadata),
            ("file_metadata", fields.file_metadata),
            ("https_url", fields.https_url),
            ("copy_to_clipboard_link", fields.https_url),
            ("globus_app_link", fields.globus_app_link),
        ],
        "facets": [
            {
                "name": "Dates",
                "field_name": "year",
                "size": 10,
            },
            {
                "name": "Survey",
                "field_name": "survey",
            },
            {
                "name": "Altitude (m)",
                "field_name": "gps_alt",
                "type": "numeric_histogram",
                "histogram_range": {"low": 0, "high": 1000},
                "filter_type": "range",
                "size": 10,
            },
        ],
        "sort": [{"field_name": "year", "order": "desc"}],
    }
}
