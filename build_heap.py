def heap_sort(data):
    def heapify(data, n, i):
        lielakais = i
        kreisais = 2 * i + 1
        labais = 2 * i + 2

        if kreisais < n and data[kreisais] > data[lielakais]:
            lielakais = kreisais

        if labais < n and data[labais] > data[lielakais]:
            lielakais = labais

        if lielakais != i:
            data[i], data[lielakais] = data[lielakais], data[i]
            heapify(data, n, lielakais)

    n = len(data)

    
    for i in range((n // 2) - 1, -1, -1):
        heapify(data, n, i)

    
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)

    return data

def main():
    input_type = input("I or F: ")

    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == "F":
        filename = input("File name: ")
        with open(f"tests/{filename}", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    assert len(data) == n

    sorted_data = heap_sort(data)

    for element in sorted_data:
        print(element)

if __name__ == "__main__":
    main()
