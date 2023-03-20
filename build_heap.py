#221RDB004

def build_heap(data):
    swap = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        heapify(data, swap, i)
    return swap

def heapify(data, swap, i):
    lielums = len(data)
    lielakais = i
    kreisais = 2 * i + 1
    labais = 2 * i + 2

    if kreisais < lielums and data[kreisais] > data[lielakais]:
        lielakais = kreisais

    if labais < lielums and data[labais] > data[lielakais]:
        lielakais = labais

    if lielakais != i:
        swap.append((i, lielakais))
        data[i], data[lielakais] = data[lielakais], data[i]
        heapify(data, i, swap)


def main():
    input_type = input()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    elif input_type == "F":
        filename = input()
        source = './tests/'
        destination = source + filename
        with open(destination, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    swap = build_heap(data)
    print(len(swap))
    for i,j in swap:
        print(i, j)

if __name__ == "__main__":
    main()
