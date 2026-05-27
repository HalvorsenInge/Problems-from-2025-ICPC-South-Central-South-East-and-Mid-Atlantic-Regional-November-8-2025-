def algorithm(inputArray, r, c):
    string = ""
    for i in range(c):
        for j in range(r):
            if inputArray[j][i] != ".":
                string+=inputArray[j][i]
    return string

def main():
    inputArray = []
    r, c = map(int, input().split())
    for _ in range(r):
        inputArray.append(list(input()))
    print(algorithm(inputArray, r, c))

if __name__ == "__main__":
    main()
    