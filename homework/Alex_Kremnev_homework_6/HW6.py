#  Задание 1
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
text_t = text.split(" ")

for x in text_t:
    if x.endswith(",") or x.endswith("."):
        sign = x[-1]  # запоминаем знак
        x = x[:-1]  # убираем знак из слова
    else:
        sign = ""  # если знака нет — пусто

    x = x + "ing" + sign  # добавляем ing и возвращаем знак (если был)
    print(x)
