from utils import read_data_file

RANGE_1 = """
3-5
10-14
16-20
12-18
""".strip().split("\n")

IDS_1 = """
1
5
8
11
17
32
""".strip().split("\n")

RANGE_2 = read_data_file("day5_1.txt", "\n")
IDS_2 = read_data_file("day5_2.txt", "\n")


class Day5:
    def __init__(self):
        print("Hello from Day 5 ...")

    def _in_any_range(self, id, ranges):
        for range in ranges:
            if id in range:
                return True
        return False

    def part_1(self):
        ids = [int(id) for id in IDS_2]
        # print(ids)

        ranges = [
            range(int(r.split("-")[0]), int(r.split("-")[1]) + 1) for r in RANGE_2
        ]
        # print(ranges)

        valid = [id for id in ids if self._in_any_range(id, ranges)]

        print(len(valid))

    def part_2(self):
        intervals = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in RANGE_2]

        intervals.sort()

        merged = []
        for start, end in intervals:
            if merged and start <= merged[-1][1] + 1:
                # Overlapping or adjacent, merge with previous interval
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                # Non-overlapping, add as new interval
                merged.append((start, end))

        total = sum(end - start + 1 for start, end in merged)
        print(total)


if __name__ == "__main__":
    Day5().part_1()
    Day5().part_2()
