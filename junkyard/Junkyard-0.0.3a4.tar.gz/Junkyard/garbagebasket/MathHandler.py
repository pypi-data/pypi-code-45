def is_float(number):
    """
    function to determine if the input value can be converted into a float
    by using the try/except technique, filtering out True and 'NaN' (which can be converted to floats)

    :param number: the value to test
    :return: True/False
             if True, the value can be converted to a float
             if False, the value cannot be converted to a float
    """
    # return False if input is NaN as it can be converted to a float.
    try:
        n = str(number)
    except ValueError:
        return False
    except TypeError:
        return False

    false_floats = (str(True), str(False), str(None), "Nan")
    if n in false_floats:
        return False

    # try/except block to attempt converting the input into a float and then  returning True
    # or return False if there is an exception
    try:
        float(number)
        return True
    except ValueError:
        return False
    except TypeError:
        return False


def safe_sum(*numbers):
    """
    function to safely get the sum value of an input
    at its core it can average ints, floats, and strings while ignoring bad data types
    it can also process recursion loops of nested lists and tuples

    this is a safer and more capable substitute for python's built in sum() function

    :param numbers: the numbers to sum
    :return: returns the sum of the numbers argument
    """
    # name function for error reporting
    function_name = f"safe_sum()"

    # reusable subfunction to do all the work
    def sum_recursion(nums):
        """
        a helper subfunction used by safe_sum to do all of the lifting including counting, number string handling,
        recursion loops through nested loops and tuples by calling itself
        when hitting tuples or lists inside of its input, and filtering bad value/data types

        :param nums: number data to sum, seperated by comma
        :return: returns the sum of nums input
        """
        # name subfunction for error reporting
        subfunction_name = f"{function_name}.sum_recursion()"

        # check that the nums variable is not empty and begin work
        if nums is not None:
            # set counter
            s_of_nums = 0

            # start for loop to process the subfunction input
            for num in nums:
                # check if num in nums is an int or a float and count
                if isinstance(num, int) or isinstance(num, float):
                    if is_float(num):
                        s_of_nums += num

                # check if num in nums is a string and that it can be converted to a float
                # using is_float(num) and converting it to a float if it has a '.' present or an int otherwise
                # and then adding it to the sum
                elif isinstance(num, str):
                    if is_float(num):
                        if "." in num:
                            s_of_nums += float(num)
                        else:
                            s_of_nums += int(num)

                # check if the num in nums is a tuple or list, and that the list is not empty
                elif isinstance(num, tuple) or isinstance(num, list):
                    # try/except block to catch recursion errors and pass if the subfunction excepts
                    try:
                        # attempt to add the output of a recursion loop
                        s_of_nums += sum_recursion(num)

                    # if the subfunction hits the python recursion limit announce and return 0
                    except RecursionError:
                        print(f"{subfunction_name}: Recursion limit reached during nested tuple/list loop!")

            # return the final sum output of the subfunction
            return s_of_nums

        # if input is None return 0
        else:
            return 0

    # begin function code
    # make sure the numbers variable isn't empty
    if len(numbers) > 0:
        # catch potential recursion errors for extreme depth nested lists or tuples
        # call the recursive summing subfunction and place its return into numbers_sum
        # and return the sum of the input numbers
        try:
            numbers_sum = sum_recursion(numbers)
            return numbers_sum

        # if the function hits the python recursion limit announce and return 0
        except RecursionError:
            print(f"{function_name}: recursion limit reached during nested recursion loop!")
            return 0

    # if the length of the numbers(*args) is empty
    # return a sum of 0
    else:
        return 0


def safe_average(*numbers):
    """
    function used to average an input safely by filtering bad value/data types
    and handling int, float, number string, list, and tuples
    including the ability to do recursion loops through nested lists/tuples
    when hitting additional lists/tuples inside of lists/tuples.

    :param numbers: the numbers to get the average / mean of
    :return: returns the average / mean of the numbers input
    """
    # name function for error reporting
    function_name = f"safe_average()"

    # create a sub function to handle the bulk of the work
    def avg_recursion(nums):
        # set up sub-function help string
        """
        a helper subfunction used by safe_average to do all of the lifting and counting
        and even do recursion loops through nested loops and tuples by calling itself when
        hitting tuples or lists inside of its input.
        
        :param nums: the tuple/list to do a recursion loop through
        :return: returns the sum of numbers and total number of numbers on index [0] and [1]
                 respectfully
        """
        # name subfunction for error reporting
        subfunction_name = f"{function_name}.safe_recursion()"
        # check that the subfunction input is not empty and begin work
        if len(nums) > 0:
            # set up the counter variables
            s_of_nums = 0
            l_of_nums = 0
            
            # start for loop to cycle through contents of nums and build the sum and length
            for num in nums:
                # check if num is an int or a float and count if so
                if isinstance(num, int) or isinstance(num, float):
                    if is_float(num):
                        s_of_nums += num
                        l_of_nums += 1

                # check if num in nums is a string and that it can be converted to a float
                # using is_float(num) and converting it to a float if it has a '.' present or an int otherwise
                # and then adding the sum and l_of_nums
                elif isinstance(num, str):
                    if is_float(num):
                        if '.' in num:
                            s_of_nums += float(num)
                        else:
                            s_of_nums += int(num)
                        l_of_nums += 1

                # check if num is a nested tuple or list
                elif isinstance(num, tuple) or isinstance(num, list):
                    # catch block to catch recursion errors and pass if the subfunction excepts
                    try:
                        # and get the sum and length returns by doing a recursion loop through the tuple/list
                        # using the safe_recursion subfunction
                        _n1, _n2 = avg_recursion(num)
                        s_of_nums += _n1
                        l_of_nums += _n2

                    # if the subfunction hit the python recursion limit announce and return 0
                    except RecursionError:
                        print(f"{subfunction_name}: Recursion limit reached during nested tuple/list loop!")
            
            # return the sums and the lengths of all the numbers
            return s_of_nums, l_of_nums

    # begin function code
    # make sure the numbers variable isn't empty
    if len(numbers) > 0:
        # catch potential recursion errors for extreme depth nested lists or tuples
        # call the recursive averaging subfunction and place index 0 and 1 into numbers_sum and numbers_length
        # and return the average of the input by dividing sum by the number of numbers
        try:
            numbers_sum, numbers_length = avg_recursion(numbers)
            return numbers_sum / numbers_length

        # if the function hit the python recursion limit announce and return 0
        except RecursionError:
            print(f"{function_name}: recursion limit reached during nested recursion loop!")
            return 0
    
    # if the length of the numbers(*args) is empty
    # return an average of 0
    else:
        return 0


def get_horizon(vantage_height, h_constant=1.5):
    """
    gets the viewing distance to the horizon on earth by height of the eyes

    :param vantage_height: in feet
    :param h_constant: horizon constant :shrug:
    :return: returns horizon in miles
    """
    return (h_constant * vantage_height) ** 0.5


def emc2(mass):
    """
    function that gets the energy equivalence of a given mass in kilograms using Einstein's e=mc2 equation
    and returns the energy equivalence (e) in joules

    :param mass: mass is the mass of the object in kilograms
    :return: returns e, as mass energy equivalence measured in joules
    """
    # return mass times c squared
    return mass * (299_792_458 ** 2)


# TESTING
if __name__ == '__main__':
    help(is_float)
    help(safe_sum)
    help(safe_average)

    # sample should return 2.5 / 10 respectfully
    calibration_sample_clean = [1, 2, 3, 4]
    calibration_sample_easy = [1, [2, (3, 4)]]
    calibration_sample_hard = [1, "two", True, ["2", ("3.0", 4)]]
    # impossible? sum: 1231 and avg: 49.24"
    crash_test_sample = (1, 2, "lol", [1, 2, "buckle my shoe", 3, 4, 5.0, "6", "7.0"],
                         (10, 20, [30, 40, (1, 2, 3, 4, 5, 1000, ("lol", "25", 50))]), 1, 2, 3, 4)

    print("TESTING MathHandler")
    print("Calibration tests, should return a sums of 10 and averages of 2.5")
    print(f"Clean: {calibration_sample_clean}")
    print(f"Easy: {calibration_sample_easy}")
    print(f"Hard: {calibration_sample_hard}")
    print("'Impossible' test should return sums of 1231 and averages of 49.24")
    print(f"Impossible: {crash_test_sample}")

    print("")

    print("TESTING safe_sum() and safe_average() FUNCTIONS")
    print("calibration test (easy mode), should return sum: 10 and avg: 2.5")
    print(f"sum: {safe_sum(calibration_sample_easy)}")
    print(f"avg: {safe_average(calibration_sample_easy)}")

    print("")

    print("calibration test (hard mode), should return sum: 10 and avg: 2.5")
    print(f"sum: {safe_sum(calibration_sample_hard)}")
    print(f"avg: {safe_average(calibration_sample_hard)}")

    print("")

    print("impossible test: should return sum: 1231 and avg: 49.24")
    try:
        print(f"sum: {safe_sum(crash_test_sample)}")
        print(f"avg: {safe_average(crash_test_sample)}")
    except TypeError:
        print("Crash Test Failed! TypeError")
    except ValueError:
        print("Crash Test Failed! TypeError")
    except ZeroDivisionError:
        print("Crash Test Failed! ZeroDivisionError")

    print("")
    print("TEST BUILT-IN PYTHON 'sum()' FUNCTION")
    print("Python's native sum() function can handle clean passes, but its robustness ends there.")
    print("The sum() function is very fast, but it cannot process dirty/convoluted data, and it cannot")
    print("recurse through nested lists or tuples")
    print("")
    try:
        print(f"clean test: {sum(calibration_sample_clean)}")
    except TypeError:
        print("Clean Test Failed! TypeError")
    except ValueError:
        print("Clean Test Failed! TypeError")

    try:
        print(f"easy test: {sum(calibration_sample_easy)}")
    except TypeError:
        print("Easy Test Failed! TypeError")
    except ValueError:
        print("Easy Test Failure: TypeError")

    try:
        print(f"hard test: {sum(calibration_sample_hard)}")
    except TypeError:
        print("Hard Test Failed! TypeError")
    except ValueError:
        print("Hard Test Failed! TypeError")

    try:
        print(f"impossible test: {sum(crash_test_sample)}")
    except TypeError:
        print("Impossible Test Failed! TypeError")
    except ValueError:
        print("Impossible Test Failed! TypeError")

    print("")
    print("")

    print("e=mc2")
    help(emc2)
    print("testing ecm2()")
    print(f"1Kg of mas is equivalent to {emc2(1)/1000/1000/1000/1000/1000} Petajoules of energy.")
