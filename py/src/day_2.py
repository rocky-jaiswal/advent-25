from utils import read_data_file


class Day2:
    def __init__(self):
        print("Hello from Day 2 ...")

    def is_invalid(self, some_id: str) -> bool:
        invalid = True
        
        lst = list(some_id)
        length = len(lst)

        if length % 2 != 0:
            return False

        half = int(length/2)
        
        if lst[0:half] != lst[half:]:
            invalid = False

        return invalid
    
    def has_repeating_pattern(self, s: str) -> bool:
        for chunk_size in range(1, len(s) // 2 + 1):
            chunks = [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]
            if len(set(chunks)) == 1:
                return True
        return False

    def part_1(self):
        product_id_ranges = read_data_file("day2_2.txt", ",")
        invalids = []

        for product_id_range in product_id_ranges:
            [start, end] = product_id_range.split("-")
            for id in range(int(start), int(end)+1):
                if self.is_invalid(str(id)):
                    invalids.append(id)

        # print(invalids)
        print(sum(invalids))

    def part_2(self):
        product_id_ranges = read_data_file("day2_2.txt", ",")
        invalids = []

        for product_id_range in product_id_ranges:
            [start, end] = product_id_range.split("-")
            for id in range(int(start), int(end)+1):
                if self.has_repeating_pattern(str(id)):
                    invalids.append(id)

        # print(invalids)
        print(sum(invalids))


if __name__ == "__main__":
    # Day2().part_1()
    Day2().part_2()
