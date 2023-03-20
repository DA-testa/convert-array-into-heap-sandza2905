def build_heap(data):
    swap = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        heapify(data, i, swap)
    return swap

def heapify(data, swap, i):
    lielums = len(data)
    lielakais = i
    kreisais = 2 * i + 1
    labais = 2 * i + 2

    if kreisais < n and data[kreisais] > data[lielakais]:
        lielakais = kreisais

    if labais < n and data[labais] > data[lielakais]:
        lielakais = labais

    if lielakais != i:
        data[i], data[lielakais] = data[lielakais], data[i]
        heapify(data, lielakais, swap)


def main():
    input_type = input("I or F: ")

    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif input_type == "F":
        filename = input("File name: ")
        with open(f"tests/{filename}", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    swap = build_heap(data)
    print(len(swap))
    for i,j in swap:
        print(i, j)

if __name__ == "__main__":
    main()
