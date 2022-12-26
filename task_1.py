# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# 
# Примеры:
# 
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


new_list, find = ["qwe", "asd", "zxc", "qwe", "ertqwe"], "qwe"
index = -1 if new_list.count(find) < 2 else list(filter(lambda x: x[1] == find, enumerate(new_list)))[1][0]
print(f'позиция второго вхождения "{find}" -> {index}')

def find_second_string_enter(string_list: list[str], search_string:str) -> int:
    for index, string in enumerate(string_list):
      if string == search_string:
          list_indexes.append(index)
