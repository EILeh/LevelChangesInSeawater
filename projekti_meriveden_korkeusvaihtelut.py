"""
Level Changes in Seawater

The program will analyze the changes in the seawater level in some measuring
station. The user will enter the measurements (i.e. sea levels) to the program
after which the program will calculate some statistical characteristics and
display them to the user. When the program starts it first prints an instruction
for user and then the program starts reading input lines and continues doing
that until the user enters an empty line. The values entered must be numbers,
both integers and real numbers are acceptable. If the user enters less than two
numbers, an error message is printed and the program ends. Otherwise the
program calculates and prints on the screen some characteristic values based on
the data. The characteristics which are calculated and printed are:
- the smallest measurement
- the largest measurement
- median
- mean
- standard deviation
The results are printed with two decimal accuracy.

COMP.CS.100 Project 2; inflaatiolaskin
Writer of the program 1: Margarita N......a
Writer of the program 2: EILeh

"""

def calculate_min_value(smallest):
    """
    Calculate_min_value function returns the item with the lowest value.

    :param smallest: list, either int or float.
    :return: (float) min value of smallest.
    """
    return min(smallest)

def calculate_max_value(greatest):
    """
    Calculate_max_value function returns the item with the highest value.

    :param greatest: list, either int or float.
    :return: (float) max value of greatest.
    """
    return max(greatest)


def calculate_median(med):
    """
    Calculate_median function return the value of median from med list.

    :param med: list, either int or float.
    :return: (float) median of med.
    """
    list_sorted = med.sort()
    list_lenght = len(med)
    if list_lenght % 2 != 0:
        m = int((list_lenght + 1) / 2 - 1)
        return med[m]
    else:
        m1 = int(list_lenght / 2 - 1)
        m2 = int(list_lenght / 2)
        return (med[m1] + med[m2]) / 2


def calculate_average(avg):
    """
    The function calculates average for avg list.

    :param avg: list, either int or float.
    :return: (float) mean of avg.
    """
    average = sum(avg)/len(avg)
    return average

def calculate_deviation(dev):
    """
    The function calculates deviation of dev list.
    :param dev: list, either int or float
    :return: (float) deviation of dev
    """
    mean = calculate_average(dev)
    dev_lenght = len(dev)
    difference = 0

    for i in range(dev_lenght):
        difference += (dev[i] - mean) ** 2

    variance = difference / (dev_lenght - 1)
    deviation = variance ** 0.5

    return deviation


def main():
    list = []
    is_user_input_number = True

    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")

    input_number = 0.0
    repetition_counter = 0

    while is_user_input_number:
        user_input = input("")

        # Print error if under 2 values have been input
        if repetition_counter < 2 and user_input == "":
            print("Error: At least two measurements must be entered!")
            return

        # Break loop if two or more values have been input
        # and most recent is empty
        elif repetition_counter >= 2 and user_input == "":
            is_user_input_number = False

        # Convert input to float and add it to the list
        else:
            input_number = float(user_input)
            list.append(input_number)

        repetition_counter += 1

    print(f"{'Minimum:':11}{calculate_min_value(list):.2f} cm")
    print(f"{'Maximum:':11}{calculate_max_value(list):.2f} cm")
    print(f"{'Median:':11}{calculate_median(list):.2f} cm")
    print(f"{'Mean:':11}{calculate_average(list):.2f} cm")
    print(f"{'Deviation:':11}{calculate_deviation(list):.2f} cm")

if __name__ == "__main__":
    main()