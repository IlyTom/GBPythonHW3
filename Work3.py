# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

points = 0
print(f'На каком языке будет слово?(ru- русский, eng - английский)')
language = input()
try:

    print(f'Введите 1 слово:',end=" ")
    word = input()
    word=list(word.upper())
    if language == "eng":
        for element in word:
            if element in 'AEIOULNSTR':
                points += 1
            elif element in 'DG':
                points += 2
            elif element in "BCMP":
                points += 3
            elif element in "FHVWY":
                points += 4
            elif element == "K":
                points += 5
            elif element in "JX":
                points += 8
            elif element in "QZ":
                points += 10
    elif language == "ru":
        for element in word:
            if element in 'АВЕИНОРСТ':
                points += 1
            elif element in 'ДКЛМПУ':
                points += 2
            elif element in "БГЁЬЯ":
                points += 3
            elif element in "ЙЫ":
                points += 4
            elif element in "ЖЗХЦЧ":
                points += 5
            elif element in "ШЭЮ":
                points += 8
            elif element in "ФЩЪ":
                points += 10
    print(points)
except:
    print("Ошибка")










