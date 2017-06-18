# Bubble Sort Algorithm
def bubble_sort(elements):
    swapped = True
    # going through all elements until no swaps were made
    while swapped:
        swapped = False
        for i in range(0, len(elements) - 1, 1):
            # comparing adjacent elements
            if elements[i] > elements[i+1]:
                # if the previous elements is bigger than the next element, shift their values
                value = elements[i+1]
                elements[i+1] = elements[i]
                elements[i] = value
                swapped = True
    return elements


# Insertion Sort Algorithm
def insertion_sort(elements):
    # going through all elements, except the first one, we assume it is ordered
    for i in range(1, len(elements)):
        j = i
        # comparing each element with the previous ones and adjusting it's position
        while j > 0 and elements[j] < elements[j-1]:
            value = elements[j]
            elements[j] = elements[j-1]
            elements[j-1] = value
            j -= 1
    return elements


# Selection Sort Algorithm
def selection_sort(elements):
    # going through all elements
    for i in range(0, len(elements)):
        # finding the minimum element
        min_index = i
        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_index]:
                min_index = j
        # shifting the current element with the minimum element
        value = elements[i]
        elements[i] = elements[min_index]
        elements[min_index] = value
    return elements


# Quick Sort Algorithm
def quick_sort(elements):
    # calling the helper method partition_quick_sort with left index the beginning of the collection and right
    # index the end of the collection
    return partition_quick_sort(elements, 0, len(elements)-1)


# a helper method, which sorts a partition of elements
def partition_quick_sort(elements, left_end_index, right_end_index):
    if left_end_index < right_end_index:
        # choosing the pivot the be the leftmost element of the partition
        pivot = elements[left_end_index]
        left_index = left_end_index + 1
        right_index = right_end_index

        # sorting the partition in such a way that all elements that are less than the pivot value are before it and
        # all elements greater than the pivot value are after it
        while True:
            while left_index <= right_index and elements[left_index] <= pivot:
                left_index += 1

            while right_index >= left_index and elements[right_index] >= pivot:
                right_index -= 1

            if left_index > right_index:
                break
            else:
                value = elements[left_index]
                elements[left_index] = elements[right_index]
                elements[right_index] = value

        elements[left_end_index] = elements[right_index]
        elements[right_index] = pivot

        # separating the partition into smaller collections, asuming that the pivot is sorted;
        # recursively calling the method to the smaller collections
        partition_quick_sort(elements, left_end_index, right_index-1)
        partition_quick_sort(elements, right_index+1, right_end_index)

        return elements

    else:
        return elements


# Merge Sort Algorithm
def merge_sort(elements):
    # if the list has no elements or just one element, return the list
    if len(elements) == 1 or len(elements) == 0:
        return elements
    else:
        # slicing the elements into halves
        left_half = merge_sort(elements[: int(len(elements)/2): 1])
        right_half = merge_sort(elements[int(len(elements)/2):: 1])

        # merging the left and the right half
        left_half_index = 0
        right_half_index = 0
        merged_list = []

        # comparing elements from both halves, while one the indices reaches the end of the list
        while left_half_index != len(left_half) and right_half_index != len(right_half):
            # if the element from the left half is less the the element from the right half, append the left element to
            # the merged sorted list and increment the left_half_index
            if left_half[left_half_index] < right_half[right_half_index]:
                merged_list.append(left_half[left_half_index])
                left_half_index += 1

            # else if the element from the left half is greater than the element from the right half, append the right
            # element to the merged sorted list and increment the right_half_index
            elif left_half[left_half_index] > right_half[right_half_index]:
                merged_list.append(right_half[right_half_index])
                right_half_index += 1

            # else if the elements are equal, append both elements to the merged sorted list and increment both indices,
            # keep in mind that some implementations append only one of the elements to avoid repetition in the list
            else:
                merged_list.append(left_half[left_half_index])
                merged_list.append(right_half[right_half_index])
                left_half_index += 1
                right_half_index += 1

        # a check if there are elements left in the left half that weren't appended; if there are, we append them all
        while left_half_index != len(left_half):
            merged_list.append(left_half[left_half_index])
            left_half_index += 1

        # a check if there are elements left in the right half that weren't appended; if there are, we append them all
        while right_half_index != len(right_half):
            merged_list.append(right_half[right_half_index])
            right_half_index += 1

        # returning the sorted merged_list
        return merged_list
