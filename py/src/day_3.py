from utils import read_data_file


class Day3:
    def __init__(self):
        print("Hello from Day 3 ...")

    def find_largest_pair(self, lst: list[str]):
        list_int = list(map(lambda x: int(x), lst))
        length = len(list_int)
        pairs = []

        for i in range(0, length):
            for j in range(i+1, length):
                pairs.append(int(f"{list_int[i]}{list_int[j]}"))

        return max(pairs)

    def part_1(self):
        ratings = read_data_file("day3_2.txt", "\n")
        lgst = []

        for rating in ratings:
            lgst.append(self.find_largest_pair(list(rating)))

        print(sum(lgst))


if __name__ == "__main__":
    Day3().part_1()
