from viewer import Viewer
from movementModel import MovementModel
import time


def main():
    v = Viewer()
    m1 = MovementModel()
    while True: #this while loop replaces v.mainloop()
        v.pointsAndPath(m1.randomWalk(), 'r')
        time.sleep(0.5)

if __name__ == '__main__':
    main()



