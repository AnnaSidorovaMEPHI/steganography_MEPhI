# Steganography

acupoftea.txt, onegin.txt - файлы, в которых просто много текста. Нужны для экспериментов.

functions.py - вспомогательные функции: приведение к бинарному представлению, парсинг бинарной строки для нахождения секрета

---
spaces_in_the_end.py - тут функции, которые прячут и достают текст по пробелам в конце строк.  

spaces_in_the_end_encode - берет на вход файл и секрет, на вызоде выдает массив, который нужно просто в файл записать.

spaces_in_the_end_decode - функция декодирования. На вход берет файл и выдает строку, которую смог извлечь.

---
spaces_after_point.py - тут функции, которые прячут и достают текст по пробелам после завершающего символа(.).  

spaces_after_point_encode - берет на вход файл и секрет, на вызоде выдает массив, который нужно просто в файл записать.

spaces_after_point_decode - функция декодирования. На вход берет файл и выдает строку, которую смог извлечь.


---

## Метод опечаток

Данная реализация метода основана на том, что по составленному словарю вносится опечатка путём вставки после первой буквы слова буквы, находящейся рядом на клавиатуре (заранее из списка составляется словарь).  
Опечатка вносится в слова, номера которых соответствуют номерам ненулевых битов в секретной фразе, таким образом секрет прячется в текст.  
При декодировании слова сравниваются с выводом функции spell(), примененной к ним, которая находит максимально похожее существующее слово (в случае, если слово не меняли, выдается то же слово), то есть исправляет ошибки.  
Для нормальной работы метода необходимо: убрать из начала текста, на которую приходится секрет, цифры,  стараться выбирать тексты с длинными словами, стараться убирать из текста нераспространённые слова из-за ограничений, связанных с функцией spell().

---

## Метод синонимов

В этом методе сообщение переводится в битовую последовательность. И слова, номеру которых в битовой последовательности соответствует единица, заменяются на синоним по словарю, заранее организованному для текста, в который прячется секрет. Словарь организован таким образом, чтобы не было неоднозначности при кодировании и декодировании.  
Процесс декодирования и получения битовой последовательности, из которой затем извлекается секрет, производится путем поиска по значениям(.values()) cловаря слов текста и определения, какие были заменены на синонимы, а какие - нет.   

---

## Метод пробелов после разделяющих символов и метод пробелов между словами

Методы основаны на помещении одного пробела на позициях после разделяющих символов(или между словами): 2-ух на той позиции, которой в бинарной последовательности сообщения соответствует единица, 1-го - на позиции, которой соответствует ноль. 


