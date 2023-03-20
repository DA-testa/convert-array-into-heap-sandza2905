def heap_sort(arr):
    swaps = []
    n = len(arr)

    def heapify(start, end):
        smallest = start
        left = 2 * start + 1
        right = 2 * start + 2

        if left < end and arr[left] < arr[smallest]:
            smallest = left

        if right < end and arr[right] < arr[smallest]:
            smallest = right

        if smallest != start:
            swaps.append((start, smallest))
            arr[start], arr[smallest] = arr[smallest], arr[start]
            heapify(smallest, end)

    for i in range((n // 2) - 1, -1, -1):
        heapify(i, n)

    return swaps


def main():
    input_type = input("Enter 'I' for input or 'F' for file: ")

    if input_type == "I":
        n = int(input("Enter the number of elements: "))
        arr = list(map(int, input("Enter space-separated integers: ").split()))
    elif input_type == "F":
        filename = input("Enter the filename: ")
        with open(f"tests/{filename}", "r") as f:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))

    assert len(arr) == n
    swaps = heap_sort(arr)

    print("Number of swaps:", len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
