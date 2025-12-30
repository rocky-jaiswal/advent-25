import math
import re
from utils import read_data_file

DATASET_1 = read_data_file("day6_1.txt", "\n")
DATASET_2 = read_data_file("day6_2.txt", "\n")


class Day6:
    def __init__(self):
        print("Hello from Day 6 ...")

    def part_1(self):
        all_items = [re.split(r"\s+", elems.strip()) for elems in DATASET_2]

        cols = {}
        res = []

        for i in range(0, len(all_items[0])):
            elems = []
            for items in all_items:
                elems.append(items[i])
            cols[i] = elems

        for _key, vals in cols.items():
            op = vals[len(vals) - 1]
            data = [int(x) for x in vals[: len(vals) - 1]]

            if op == "+":
                res.append(sum(data))
            if op == "*":
                res.append(math.prod(data))

        print(sum(res))


if __name__ == "__main__":
    Day6().part_1()
