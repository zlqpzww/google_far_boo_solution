def is_prime(n):
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

def solution(i):
    whole_str = ""
    j = 1
    while len(whole_str) < i + 5:
        while True:
            j += 1
            if is_prime(j):
                whole_str += str(j)
                break
    return whole_str[i: i + 5]

if __name__ == "__main__":
    import sys
    print(f"input is {sys.argv[1]}")
    print(f"output is {solution(int(sys.argv[1]))}")