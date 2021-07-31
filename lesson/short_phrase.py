class TestShortPhrase:

    def test_check_len(self):
        phrase = input("Введите любую фразу меньше 15 символов: ")
        assert len(phrase) < 15, "Количество символов больше 15!"
