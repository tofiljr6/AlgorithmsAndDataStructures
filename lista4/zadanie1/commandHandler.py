from queue import *


def main():
    q = Queue()
    lines = int(input())
    for line in range(lines):
        command = input()
        cmd = command.split()
        if cmd[0] == "insert":
            q.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            q.print()
        elif cmd[0] == "empty":
            print(q.empty())
        elif cmd[0] == "top":
            print(q.top())
        elif cmd[0] == "pop":
            print(q.pop())
        elif cmd[0] == "priority":
            q.priority(int(cmd[1]), int(cmd[2]))
        else:
            print("unregonized command")


if __name__ == '__main__':
    main()