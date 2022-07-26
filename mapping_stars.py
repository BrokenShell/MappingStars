""" Mapping the Stars """
from datetime import datetime
from itertools import starmap, count
from typing import Dict

from IteratorAlgorithms import generate


def timestamp(data: Dict, label: str = "created") -> Dict:
    data.update({label: datetime.now()})
    return data


def dict_to_str(data: Dict) -> str:
    return "\n" + "\n".join(f"{k}: {v}" for k, v in data.items())


counter = count(1)
first_names = ("John", "Jane", "Bill", "Jill")
last_names = generate(lambda: "Star")
ages = range(36, 0, -2)

array = (
    {"index": next(counter), "firstName": first, "lastName": last, "age": age}
    for first, last, age in zip(first_names, last_names, ages)
)

creates = map(timestamp, array)
updates = generate(lambda: "updated")
results = starmap(timestamp, zip(creates, updates))

for astronaut in results:
    print(dict_to_str(astronaut))
