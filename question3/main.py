def find(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == sum:
                return ([arr[i],arr[j]])

def main():
    arr = input("Specify an array: ")
    arr = [int(n) for n in arr.split()]
    sum = int(input("Target sum: "))
    ans = find(arr, sum)
    print("Result: ", ans)

if __name__ == "__main__":
    main()
