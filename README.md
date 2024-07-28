## Автотесты на Android в BrowserStack, Emulator и Real Device

### Структура проекта
- `allure_results` - папка с результатами тестирования
- `tests` - пакет, с тестами
- `conftest.py` - фикстуры
- `utils` - пакет с утилитами
- `config.py` - конфигурация
- `app_release.apk` - приложение
- `requirements` - файл с необходимыми библиотеками

### Запуск автотестов

**Создание вертуальной среды**

> `python -m venv venv`  
> `venv\Scripts\activate`


**Установка зависимостей**
> `pip install -r requirements.txt`

**Запуск автотестов**

> `pytest tests/test_wikipedia_bstack.py --context=bstack` - BrowserStack  
> `pytest tests/test_wikipedia_real_device.py --context=real_device` - Real Device  
> `pytest tests/test_wikipedia_emulator.py --context=emulator` - Emulator

**Отчет о тестировании в Allure**

> `allure serve allure_results`
