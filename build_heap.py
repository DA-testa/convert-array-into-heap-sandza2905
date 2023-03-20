#221RDB004
#python3

def build_heap(data):
    n = len(data)
    swap = []
    for i in range(n // 2, -1, -1):
        heap(data, swap, i, n)
    return swap

def heap(data, swap, i, n):
    min = i
    kreisais = 2 * i + 1
    labais = 2 * i + 2

    if kreisais < n and data[kreisais] < data[min]:
        min = kreisais

    if labais < n and data[labais] < data[min]:
        min = labais

    if i != min:
        swap.append((i, min))
        data[i], data[min] = data[min], data[i]
        heap(data, swap, min, n)


def main():
    input_type = input().strip()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == "F":
        test_nr = input().strip()
        with open(f"tests/{test_nr}", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
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
