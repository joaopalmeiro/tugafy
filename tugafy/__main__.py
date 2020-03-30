# __main__.py

from tugafy import dict_reader
from typing import Dict


def main() -> Dict[str, str]:
    return dict_reader.get_dictionary()


if __name__ == "__main__":
    main()
