import traceback
try:
    a = 2/0
except ZeroDivisionError as e:
    # print(e.__traceback__)
    # traceback.print_tb(e.__traceback__)
    s = traceback.format_exc()
    print(s)