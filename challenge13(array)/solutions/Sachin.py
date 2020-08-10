# function must be named solution
# function must take a list argument
# no libraries/imports allowed
def solution(inputArray):
    total = 0

    if len(inputArray) > 1:
        # Set `previous` as 1st element
        previous = inputArray[0]

        # Start from 2nd element
        for i in range(1,len(inputArray)):
            current = inputArray[i]

            # Work out `delta` needed to make `current` 1 unit higher than `previous`
            delta = previous - current + 1 if previous >= current else 0

            # Accumulate `total`
            total += delta

            # Update `previous` to new height for next iteration
            previous = current + delta

# function must return an integer
    return total