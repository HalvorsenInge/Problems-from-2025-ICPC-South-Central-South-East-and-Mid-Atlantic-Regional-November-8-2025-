def algorithm(k: int, s: int) -> int:
    trips = s // k
    return trips + (s % k)


def main():
    k, s = map(int, input().split())
    # where k is the number of possible pages stambed on a single trip and s is the total number of pages in the passport
    # k might also be 1
    # the algoritme here will be something where we take the total number of pages, anfd divides it on the stamps, and the floor the result
    print(algorithm(k, s))

if __name__ == "__main__":
    main()