import pygame, pygame_gui


class SortingAlgorithm:
    # Compares two adjacent elements and swaps them until they are in chronological order.
    def bubble_sort(array: list) -> list:
        # Loop from 0 to length of array
        for i in range(0, len(array)):
            swapped = False

            # Loop from 0 to length of list - index of left side - 1
            for j in range(0, len(array) - i - 1):
                left_side = array[j]
                right_side = array[j + 1]

                # Swap left and right sides if left side > right side
                if left_side > right_side:
                    array[j] = right_side
                    array[j + 1] = left_side
                    swapped = True
            if not swapped:
                break

        return array
