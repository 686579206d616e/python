def convert_time(duration: int) -> str:
    function_result = ""
    days = duration // 86400
    hours = duration // 3600 - (days * 24)
    minutes = duration // 60 - (days * 1440) - (hours * 60)
    seconds = duration - (days * 86400) - (hours * 3600) - (minutes * 60)

    if days > 0:
        function_result += f"{days} дн "
    if hours > 0 or len(function_result) > 0:
        function_result += f"{hours} час "
    if minutes > 0 or len(function_result) > 0:
        function_result += f"{minutes} мин "
    if seconds > 0 or len(function_result) > 0:
        function_result += f"{seconds} сек"

    return function_result


duration = 400153
result = convert_time(duration)
print(result)
# print(convert_time(120))
# print(convert_time(153))
# print(convert_time(3615))
# print(convert_time(90061))
# print(convert_time(9000))
# print(convert_time(1))
# print(convert_time(60))
