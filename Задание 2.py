while True:
    sec_inp = input("Введите время в секундах: ")
    if sec_inp.isdigit():
        sec_inp = int(sec_inp)
        break
    else:
        print('Ошибка ввода, это не число')



hour = sec_inp // 3600
min = (sec_inp - hour * 3600) // 60
sec = sec_inp - hour*3600 - min*60

print(f'{hour:>02}:{min:>02}:{sec:>02}')
