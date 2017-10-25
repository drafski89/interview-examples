def foobar(number):
    output_string = ""
    if number % 5 == 0:
        output_string = output_string + "foo"
    if number % 7 == 0:
        output_string = output_string + "bar"
    return output_string

if __name__ == "__main__":
    for x in range(1,100,3):
        result = foobar(x)
        if len(result) > 0:
            print "" + str(x) + ": \t" + str(foobar(x))