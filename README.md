Проект по автоматизации UI-тестов для сервиса Stellar Burgers

Спринт 5, UI - тестирование
Ссылка на сервис - https://stellarburgers.nomoreparties.site

В корневой директории проекта содержатся вспомогательные инструменты для тестирования и набор тестов:
1. Папка tests - тесты, для каждой функциональности;
2. Файл conftest - фикстуры, необходимые для запуска тестов;
3. Файл gen_date - функции для генерации тестовых данных;
4. Файл locators - локаторы, которые используются в тестах;
5. Файл test_data - тестовые данные для полей входа;
6. Файл test_url - содержит ссылку тестируемого сервиса Stellar Burgers.

В рамках проекта было необходимо проверить лишь определённую функциональность сервиса:
1. test_registration проверяет 2 позитивных и 4 негативных сценария регистрации пользователя;
2. test_authentication проверяет 4 позитивных сценария аутентификации пользователя;
3. test_logout проверяет 1 позитивный сценарий выхода из аккаунта;
4. test_constructor_navigate проверяет 2 позитивных сценария навигации в Конструктор;
5. test_navigating_sections_constructor проверяет 12 позитивных сценариев навигации в Конструкторе между разделами "Булки","Соусы" и "Начинки";
6. test_personal_account_navigate проверяет 1 позитивный сценарий перехода в Личный кабинет

Для запуска всех тестов необходимо в терминал ввести команду: pytest -v.
