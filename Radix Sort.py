# Array contains elements we are sorting by a certain digit
# index represents the digit we are sorting it by (0 = ones, 1 = tens, 2 = hundreds...)
# bucketSort() sorts the array based on the index
def bucketSort(Array,index,base):

    # creates blank array to store numbers
    buckets = [[] for i in range(base)]

    x = 1
    # multiplies x depending on index we are trying to find
    for i in range(index):
        x *= base

    # finds digit of each element and places it in buckets accordingly
    for element in Array:
        digit = int(element/x % base)
        (buckets[digit]).append(element)

    # initialize and concatenate all elements to output Array
    ArrayOutput = []
    for element in buckets:
        ArrayOutput.extend(element)

    return ArrayOutput

def sortArray(Array):
    # finds base and max
    n = len(Array)
    maxInt = max(Array)

    # x determines if there are still digits left
    x = 1
    i = 0
    # runs bucketSort while there are still digits in the largest element
    while maxInt/x > 1:
        Array = bucketSort(Array,i,n)
        x *= n
        i += 1

    # moves negative elements to front, if there are any
    for i in range(len(Array)):
        if Array[i] < 0:
            Array = Array[i:] + Array[:i]
            break

    return Array

# driver code
Array = [-470,1911,120,-314,-4,1871,1749,1588,195,1097]
print(sortArray(Array))
