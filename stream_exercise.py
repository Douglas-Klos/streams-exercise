#!/usr/bin/env python3
""" Class to process IOString.  See StreamProcessor.process docstring for more info """


class StreamProcessor(object):
    """ Process an input """

    def __init__(self, stream):
        self._stream = stream

    def process(self):
        """
            1. Reads two digits at a time from the beginning of the stream
               While not stated, if only a single digit remains, it is not added to
               count nor total (based on results from tests.py)
            2. Converts the two digits into a number, and adds that number
               to a running total.
            3. Once this number reaches 200 or more, the method returns how
               many two digit numbers it had to add together to reach its
               total.
            4. If `process` reaches the end of the stream BEFORE it has
               reached a sum of 200, then it will return how many two
               digit numbers it found before reaching the end of the
               stream.
            5. The method will add AT MOST 10 of these two digit numbers
               together: if it reaches the 10th two digit number and the
               sum has not yet reached 200, then the method will stop and
               return 10.
        """

        count = 0  # How many two-digit numbers the `process` method has added together.
        total = 0  # The running total of sums.

        # I did this before looking at the solution.  Works the same, perhaps not as
        #   clean as the other, but thought I'd leave it as I wrote it.

        for block in iter(lambda: self._stream.read(2), ""):

            # Because in his test file, if there's only a single digit left, it's ignored.
            if len(block) < 2:
                return count
            count += 1
            total += int(block)
            if total >= 200 or count == 10:
                return count
        return count


def main():
    """ We Wuz Main """
    import io 
    my_stream_processor = StreamProcessor(io.StringIO("234761640930110349378289194"))
    print(my_stream_processor.process())


if __name__ == "__main__":
    main()
