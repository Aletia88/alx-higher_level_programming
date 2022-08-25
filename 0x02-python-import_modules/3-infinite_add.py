#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for integer in range(1, len(sys.argv)):
        sum += int(sys.argv[integer])
    print(f"{sum}")

