from utils import read_data_file


class Day2:
    def __init__(self):
        print("Hello from Day 2 ...")

    def is_invalid_1(self, some_id: str) -> bool:
        invalid = True
        
        lst = list(some_id)
        length = len(lst)

        if length % 2 != 0:
            return False

        half = int(length/2)
        
        if lst[0:half] != lst[half:]:
            invalid = False

        return invalid

    def part_1(self):
        product_id_ranges = read_data_file("day2_2.txt", ",")
        invalids = []

        for product_id_range in product_id_ranges:
            [start, end] = product_id_range.split("-")
            for id in range(int(start), int(end)+1):
                if self.is_invalid_1(str(id)):
                    invalids.append(id)

        # print(invalids)
        print(sum(invalids))


if __name__ == "__main__":
    # Day1().part_1()
    Day2().part_1()
