import sys
import dataskema
import dataskema.lang
from dataskema.data_types import DataTypes as t


def test_incoming_params(pat_value):
    args2 = dataskema.Args({'pat_value': pat_value})
    args2.validate({'pat_value': {
        'label': 'Valor del PAT',
        'min-size': 8,
        'max-size': 64,
        'regexp': '^[A-Za-z0-9+/]+\\={0,2}$',
    }})
    print(f"pat_value={str(pat_value)}")


if __name__ == '__main__':
    args = sys.argv[1:]
    dataskema.lang.DEFAULT = 'fr'
    test_incoming_params(pat_value="MTM5M!jQwMzkwNTg2OkHPKja/jsXVAFSSeFEEwHk5oLvA")
