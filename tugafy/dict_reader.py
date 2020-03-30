# dict_reader.py

import csv
import io
import urllib.request as request
import functools
from typing import Dict


@functools.lru_cache(maxsize=2)
def get_dictionary() -> Dict[str, str]:
    url = "https://raw.githubusercontent.com/joaopalmeiro/en-pt-dict-DS-ML/master/data/dict.csv"

    response = request.urlopen(url)

    csv_file = list(csv.reader(io.StringIO(
        response.read().decode("utf-8")), delimiter=','))

    dictionary_dict = {term[0]: term[1] for term in csv_file[1:]}

    return dictionary_dict
