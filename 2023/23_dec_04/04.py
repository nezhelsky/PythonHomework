film = input("Введите название фильма: ")
name_cinema = input("Введите название кинотеатра: ")
time = input("Введите время: ")

message = "Билет на %s в %s на %s забронирован" % (film, name_cinema, time)
print(message)