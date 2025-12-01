from utils import read_data_file


class Dial:
    def __init__(self):
        self.position = 50
        self.zero_hits = 0
        self.total_zero_hits = 0

    def move(self, direction: str, steps: int):
        if direction == "L":
            for step in range(steps):
                if self.position != 0:
                    self.position = self.position - 1
                else:
                    self.position = 99
                if self.position == 0:
                    self.total_zero_hits += 1
        else:
            for step in range(steps):
                if self.position != 99:
                    self.position = self.position + 1
                else:
                    self.position = 0
                if self.position == 0:
                    self.total_zero_hits += 1

        if self.position == 0:
            self.zero_hits += 1


class Day1:
    def __init__(self):
        print("Hello from Day 1 ...")
        self.dial = Dial()

    def part_1(self):
        instructions = read_data_file("day1_1.txt", "\n")
        for instruction in instructions:
            self.dial.move(instruction[:1], int(instruction[1:]))

        print(self.dial.position)
        print(self.dial.zero_hits)

    def part_2(self):
        instructions = read_data_file("day1_2.txt", "\n")
        for instruction in instructions:
            self.dial.move(instruction[:1], int(instruction[1:]))

        print(self.dial.position)
        print(self.dial.total_zero_hits)


if __name__ == "__main__":
    # Day1().part_1()
    Day1().part_2()
