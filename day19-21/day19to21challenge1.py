from itertools import cycle
import sys
import time

traffic_signal_colours = cycle('RED YELLOW GREEN'.split())


def traffic_light_rotation():
    while True:
        active_signal = next(traffic_signal_colours)

        if active_signal == 'YELLOW':
            for i in range(1, 4):
                sys.stdout.write('\r' + 'START ENGINE!!!! '+active_signal)
                sys.stdout.flush()
                time.sleep(1)
                sys.stdout.write('\r')
                sys.stdout.flush()
                time.sleep(1)
        elif active_signal == 'RED':
            sys.stdout.write('\r' + 'STOP! ' + active_signal)
            sys.stdout.flush()
            time.sleep(2)
        else:
            sys.stdout.write('\r' + 'YOU CAN GO!! ' + active_signal)
            sys.stdout.flush()
            time.sleep(3)


def main():
    traffic_light_rotation()


if __name__ == '__main__':
    main()
