import io
import time

number = 0
while not number==100:
    number += 2
    output = io.StringIO()
    output.write('Next Even Number is  ' + str(number) + '\n')
    contents = output.getvalue()
    output.close()
    time.sleep(10)
