import sys
import ../dataskema
from ../dataskema.data_types import DataTypes as t


@dataskema.args(param1=t.positive, param2=t.negative, param3=t.email)
def test_incoming_params(param1, param2, param3):
    print(f"Param1={strparam1}")
    print(f"Param2={str(param2)}")
    print(f"Param3={str(param3)}")


if __name__ == '__main__':
    args = sys.argv[1:]
    test_incoming_params(**args)
