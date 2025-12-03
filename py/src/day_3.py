from utils import read_data_file
# from itertools import combinations


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
    
    def find_largest_by_removing(self, lst: list[str], to_remove: int) -> int:
        stack = []
        removals_left = to_remove
        
        for digit in lst:
            while stack and removals_left > 0 and stack[-1] < digit:
                stack.pop()
                removals_left -= 1
            stack.append(digit)
        
        if removals_left > 0:
            stack = stack[:-removals_left]
        
        return int(''.join(stack))
    
    def omit_at_indexes(self, lst, indexes_to_omit):
        return int(''.join(str(item) for i, item in enumerate(lst) if i not in indexes_to_omit))
    
    def find_largest_num(self, lst: list[str]):
        length = len(lst)

        # skippables = []
        # for combo in combinations(range(length), length - 12):
        #     # print(combo)
        #     skippables.append(list(combo))
            
        # nums = []
        # for skips in skippables:
        #     nums.append(self.omit_at_indexes(lst, skips))

        return self.find_largest_by_removing(lst, length - 12)

    def part_1(self):
        ratings = read_data_file("day3_2.txt", "\n")
        lgst = []

        for rating in ratings:
            lgst.append(self.find_largest_pair(list(rating)))

        print(sum(lgst))

    def part_2(self):
        ratings = read_data_file("day3_2.txt", "\n")
        lgst = []

        for rating in ratings:
            lgst.append(self.find_largest_num(list(rating)))

        print(sum(lgst))


if __name__ == "__main__":
    # Day3().part_1()
    Day3().part_2()
