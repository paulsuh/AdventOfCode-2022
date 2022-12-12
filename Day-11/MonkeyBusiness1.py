import fileinput
import re
import queue
from pprint import pprint


class Monkey(object):

    def __init__(self, def_lines):
        # starting_items, operation_string, test_value, true_dest, false_dest
        items_temp = re.split(r'\W+', def_lines[1])[2:]
        self.items = queue.Queue()
        for one_item in items_temp:
            self.items.put(int(one_item))

        self.op_string = re.split(r'=', def_lines[2])[1].strip()

        self.test_val = int(re.split(r'\W+', def_lines[3])[-1])

        self.dest_true = int(re.split(r'\W+', def_lines[4])[-1])
        self.dest_false = int(re.split(r'\W+', def_lines[5])[-1])

        self.num_inspections = 0

    def eval_operation(self, old):
        result = eval(self.op_string)
        return result

    def receive_item(self, item_num):
        self.items.put(item_num)

    def inspect_item(self, obj_val):
        self.num_inspections += 1
        new_obj_val = self.eval_operation(obj_val) // 3
        if new_obj_val % self.test_val == 0:
            monkeys[self.dest_true].receive_item(new_obj_val)
        else:
            monkeys[self.dest_false].receive_item(new_obj_val)

    def inspect_all_items(self):
        while not self.items.empty():
            self.inspect_item(self.items.get())

templines = []
monkeys = []

for raw_line in fileinput.input():

    line = raw_line.strip()

    if len(line) == 0:
        continue

    templines.append(line)
    if len(templines) == 6:
        new_monkey = Monkey(templines)
        monkeys.append(new_monkey)
        templines = []


for round in range(20):
    for one_monkey in monkeys:
        one_monkey.inspect_all_items()

    pprint([list(m.items.queue) for m in monkeys])

insp_list = sorted([m.num_inspections for m in monkeys], reverse=True)

print(insp_list)
print( insp_list[0] * insp_list[1] )