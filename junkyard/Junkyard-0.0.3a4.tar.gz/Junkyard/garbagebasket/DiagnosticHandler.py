import time


handler_name = "DiagnosticHandler"


def speed_test(subject=None, n_tests=100, float_precision=8, loop_time=0.1, *args):
    # setup help() return for the method
    """
    method for testing the speed of a function
    :param subject: function to test without ()'s
    :param n_tests: number of tests to run and average
    :param float_precision: floating point precision of the timer
    :param loop_time: break time between each test (in seconds)
    :param args: parameters for subject_1 and subject_2
    :return: returns nothing, just a way to break out of the function if subject is empty
    """

    # establish method name for print/debug statements
    function_name = f"{handler_name}.speed_test()"

    # subject = # None
    # n_tests = # 100
    # float_precision = # 8
    # loop_time = # 0.1

    # make sure subjects have values
    if subject is None:
        print(f"{function_name}: subject is empty")
        return

    # SUBJECT TEST LOOP
    print("TESTING SUBJECT 1")
    subject_times = []
    # start loop for n_tests times
    for x in range(n_tests):
        # start timer
        timer_start = time.perf_counter()

        # try to handle potential errors
        try:
            # call our first test subject from arguments
            subject(*args)
        except ValueError:
            print(f"{function_name}: ({subject}({args})) failed to run properly")
            break
        except TypeError:
            print(f"{function_name}: ({subject}({args})) failed to run properly")
            break
        except FileNotFoundError:
            print(f"{function_name}: ({subject}({args})) failed to run properly")
            break
        except OSError:
            print(f"{function_name}: ({subject}({args})) failed to run properly")
            break

        # stop timer
        timer_stop = time.perf_counter()

        # get total time
        subject_time = timer_stop - timer_start
        print(f"[Test {x+1}] {subject_time} seconds")
        # and append it to our times list
        subject_times.append(subject_time)
        # take a break
        time.sleep(loop_time)

    # get averages of tests
    subject_average = round(sum(subject_times) / len(subject_times), float_precision)

    # create a line space
    print("")

    # print Subject wins and average time
    print(f"Subject: average runtime of {subject_average} seconds")


def speed_comparison_test(subject_1=None, subject_2=None,
                          n_tests=100, float_precision=8, intermission_time=1, loop_time=0.1, *args):
    # setup help() return for the method
    """
    method for testing the speed difference of two functions

    :param subject_1: first function to test without ()'s
    :param subject_2: first function to test without ()'s
    :param n_tests: number of tests to run and average
    :param float_precision: floating point precision of the timer
    :param intermission_time: break time between the two sets of tests (in seconds)
    :param loop_time: break time between each test (in seconds)
    :param args: parameters for subject_1 and subject_2
    :return: returns nothing, just a way to break out of the function if subject 1 or 2 are empty
    """

    # establish method name for print/debug statements
    function_name = f"{handler_name}.speed_comparison_test()"

    # make sure subjects have values
    if subject_1 is None:
        print("subject_1 is empty")
        return
    if subject_2 is None:
        print("subject_2 is empty")
        return

    # SUBJECT 1 TEST LOOP
    print("TESTING SUBJECT 1")
    subject_1_times = []
    # start loop for n_tests times
    for x in range(n_tests):
        # start timer
        timer_start = time.perf_counter()

        # try to handle potential errors
        s1_failure_msg = f"{function_name}: ({subject_1}({args})) failed to run properly"
        try:
            # call our first test subject from arguments
            subject_1(*args)
        except ValueError:
            print(s1_failure_msg)
            break
        except TypeError:
            print(s1_failure_msg)
            break
        except FileNotFoundError:
            print(s1_failure_msg)
            break
        except OSError:
            print(s1_failure_msg)
            break

        # stop timer
        timer_stop = time.perf_counter()

        # get total time
        subject_1_time = timer_stop - timer_start
        print(f"[Test {x + 1}] {subject_1_time} seconds")
        # and append it to our times list
        subject_1_times.append(subject_1_time)
        # take a break
        time.sleep(loop_time)

    # TAKE A BREAK!
    print("")
    print("-- intermission --")
    print("")
    time.sleep(intermission_time)

    # SUBJECT 2 TEST LOOP
    print("TESTING SUBJECT 2")
    subject_2_times = []
    for x in range(n_tests):
        # start timer
        timer_start = time.perf_counter()

        # try to handle potential errors
        s2_failure_msg = f"{function_name}: ({subject_2}({args})) failed to run properly"
        try:
            # call our first test subject from arguments
            subject_2(*args)
        except ValueError:
            print(s2_failure_msg)
            break
        except TypeError:
            print(s2_failure_msg)
            break
        except FileNotFoundError:
            print(s2_failure_msg)
            break
        except OSError:
            print(s2_failure_msg)
            break

        # stop timer
        timer_stop = time.perf_counter()

        # get total time
        subject_2_time = timer_stop - timer_start
        print(f"[Test {x + 1}] {subject_2_time} seconds")
        # and append it to our times list
        subject_2_times.append(subject_2_time)
        # take a break
        time.sleep(loop_time)

    # get averages of tests
    subject_1_average = round(sum(subject_1_times) / len(subject_1_times), float_precision)
    subject_2_average = round(sum(subject_2_times) / len(subject_2_times), float_precision)

    # get win times for each subject using list comprehensions
    # subject 1
    subject_1_wins = [subject_1_times[index] for index, e in enumerate(subject_1_times)
                      if subject_1_times[index] < subject_2_times[index]]
    #
    # subject 2
    subject_2_wins = [subject_2_times[index] for index, e in enumerate(subject_2_times)
                      if subject_1_times[index] > subject_2_times[index]]

    # get number of wins
    subject_1_n_wins = len(subject_1_wins)
    subject_2_n_wins = len(subject_2_wins)

    # create a line space
    print("")

    # print Subject wins and average time
    print(f"Subject 1 Wins: {subject_1_n_wins} ({round((subject_1_n_wins / n_tests) * 100, 2)}%) with an "
          f"average time of {subject_1_average} seconds")
    print(f"Subject 2 Wins: {subject_2_n_wins} ({round((subject_2_n_wins / n_tests) * 100, 2)}%) with an"
          f" average time of {subject_2_average} seconds")

    # create a line space
    print("")

    # compare subject number of wins
    if subject_1_n_wins > subject_2_n_wins:
        print(f"SUBJECT 1 HAS THE MOST WINS ({subject_1_n_wins} / {n_tests})")
    elif subject_1_n_wins < subject_2_n_wins:
        print(f"SUBJECT 2 HAS THE MOST WINS ({subject_2_n_wins} / {n_tests})")
    elif subject_1_n_wins == subject_2_n_wins:
        print("SUBJECT 1 AND SUBJECT 2 HAVE THE SAME NUMBER OF WINS - TIE!")

    # compare subject average times
    if subject_1_average < subject_2_average:
        print(f"SUBJECT 1 HAD THE FASTEST AVERAGE @ {subject_1_average} SECONDS")
        print(f"or {subject_2_average / subject_1_average} times Subject 2's average")
    elif subject_1_average > subject_2_average:
        print(f"SUBJECT 2 HAD THE FASTEST AVERAGE @ {subject_2_average} SECONDS")
        print(f"or {subject_1_average / subject_2_average} times Subject 1's average")
    elif subject_1_average == subject_2_average:
        print(f"SUBJECT 1 AND SUBJECT 2 HAVE THE SAME AVERAGE @ {subject_1_average} SECONDS")
