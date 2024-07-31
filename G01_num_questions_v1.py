
def num_check():
    error = "Please Enter a Number That is More Than 0"

    try:
        response = int(input("Choose a Number: "))

        if response <= 0:
            print(error)

        else:
            return response

    except ValueError:
        print(error)

while True:
    to_check = num_check()
