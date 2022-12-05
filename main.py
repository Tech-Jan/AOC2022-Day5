from dataclass import Storage, MovePlan
from Crane import Crane
from pprint import pprint
import time

storage = Storage("day5crates")
storage2 = Storage("day5crates")
move_list = MovePlan("day5moves")
crane9000 = Crane(storage, "9000")

for move in move_list.movelist:
    amount = int(move[0])
    fromwhere = int(move[1]) - 1
    towhere = int(move[2]) - 1
    crane9000.movebox(amount, fromwhere, towhere)
    pprint(storage.shelf)
    print("!##############################################!")
    time.sleep(0.5)

storage2 = Storage("day5crates")
crane9001 = Crane(storage2, "9001")
move_list9001 = MovePlan("day5moves")

for move in move_list9001.movelist:
    amount = int(move[0])
    fromwhere = int(move[1]) - 1
    towhere = int(move[2]) - 1
    crane9001.movebox(amount, fromwhere, towhere)
    pprint(storage2.shelf)
    print("!##############################################!")
    time.sleep(0.5)

# pprint(storage2.shelf)
# print(crane9001.move_box)
