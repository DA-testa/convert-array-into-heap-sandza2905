#221RDB004

def build_heap(data):
    swap = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        heap(data, swap, i, n)
    return swap

def heap(data, swap, i, n):
    lielakais = i
    kreisais = 2 * i + 1
    labais = 2 * i + 2

    if kreisais < n and data[kreisais] > data[lielakais]:
        lielakais = kreisais

    if labais < n and data[labais] > data[lielakais]:
        lielakais = labais

    if lielakais != i:
        swap.append((i, lielakais))
        data[i], data[lielakais] = data[lielakais], data[i]
        heap(data, swap, lielakais)


def main():
    input_type = input().strip()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == "F":
        test_nr = input().strip()
        filename = input()
        source = './tests/'
        destination = source + filename
        with open(destination, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    else:
        print("Invalid input type")
        return
    
    assert len(data) == n    
    swap = build_heap(data)
    print(len(swap))
    for i,j in swap:
        print(i, j)

if __name__ == "__main__":
    main()
