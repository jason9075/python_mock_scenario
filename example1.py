import time


def run_very_long_func(input_value):

    print("I will run very long.")
    time.sleep(5)
    return 1 if input_value == 42 else 0


def main(input_value):
    print("program start.")

    result = run_very_long_func(input_value)

    if result == 1:
        return "good"
    else:
        return "bad"


if __name__ == "__main__":
    main(42)
