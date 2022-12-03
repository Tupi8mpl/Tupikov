import statistics
import sorting_table

if __name__ == "__main__":
    is_input = False
    while not is_input:
        input = input('Для таблиц введите "Вакансии" без кавычек.\n'
                           'Для графика введите "Статистика" без кавычек.\n')
        if input == "Вакансии":
            sorting_table.main()
            is_input = True
        elif input == "Статистика":
            statistics.main()
            is_input = True
        else:
            print("Введите корректное значение.")