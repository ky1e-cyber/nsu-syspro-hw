def count_on_bits(x: int) -> int:
    loop: int = 0 if x >= 0 else -1
    counter: int = x & 1
    x >>= 1
    while x != loop:
        counter += x & 1
        x >>= 1    
    return counter + (x & 1)


if __name__ == "__main__":
    x: int = int(input())
    print(count_on_bits(x))