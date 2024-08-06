# pylint: skip-file
from validation_rules.scripts_sql import check_consistency, check_totalization_of_records, validacao_teste


MAPPING_VALIDATION_FIELDS = {
    'C100': [
        {'register_code':'C100','func': check_consistency,'key_field': 'Campo9', 'fields': 'ALL'},
        {'register_code':'C100','func': check_totalization_of_records, 'key_field': None, 'fields': None},
        {'register_code':'C100','func': validacao_teste, 'key_field': None, 'fields': ['Campo1', 'Campo2', 'Campo3']}
    ],
    'C101': [
        {'register_code':'C101','func': check_consistency,'key_field': 'Campo9', 'fields': 'ALL'},
        ],
    'C110': [
        {'register_code':'C110','func': check_consistency,'key_field': 'Campo9', 'fields': 'ALL'},
        ],
    'C113': [
        {'register_code':'C113','func': check_consistency,'key_field': 'Campo9', 'fields': 'ALL'},
        ],
    'C170': [
        {'register_code':'C170','func': check_consistency,'key_field': 'Campo9', 'fields': 'ALL'},
        ],
      
}