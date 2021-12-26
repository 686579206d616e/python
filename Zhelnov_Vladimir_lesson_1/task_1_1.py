import math


def convert_time(duration: int) -> str:
    function_result = ""
    buffer = duration / 86400

    if math.floor(buffer) > 0:
        function_result = "{} дн ".format(math.floor(buffer))

    for idx, x in enumerate([24, 60, 60]):
        buffer = (buffer % 1) * x
        if math.floor(buffer) > 0:
            function_result += "{} {} ".format(math.floor(buffer), ('час', 'мин', 'сек')[idx])

    return function_result.strip()


duration = 400153
result = convert_time(duration)
print(result)
