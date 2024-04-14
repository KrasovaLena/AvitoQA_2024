## Инструкция ##
### Навигация по файлам: ###
#### Задание №1 ####
[Task_1](./Task_1.md) - Список найденных в Задании №1 багов;
<br/>[Task_1_Bugs](./Task_1_Bugs) - Папка со скриншотами найденных в Задании №1 багов;
#### Задание №2 ####
[TESTCASES.md](./TESTCASES.md) - Тест-кейсы к модулю Эковклад из Задания №2;
<br/>[BUGS.md](./BUGS.md) - Список найденных в Задании №2 багов;
<br/>[output](./output) - Папка со скриншотами найденных в Задании №2 багов;
<br/>[Tests.py](./Tests.py) - Код с автоматизацией тест-кейсов из файла TESTCASES.md;
<br/>[json_data.py](./json_data.py) - Файл содержащий JSON с тестовыми данными для подмены ответа от сервера;
<br/>[requirements.txt](./requirements.txt) - список пакетов необходимых для работы тестов.

### Как можно заново получить все скриншоты в папке «output»: ###
* #### Откройте предпочтительную среду разработки (VSCode/PyCharm/IDE) ####
* #### Создайте новый проект ####
* #### Разверните виртуальное окружение если требуется (В PyCharm создается автоматически) ####
  * Создание виртуального окружения:
  <br/> ```python3 -m venv venv``` (MacOs)
  <br/> ```virtualenv venv``` (Windows)
  * Активация виртуального окружения:
  <br/> ```source venv/bin/activate``` (MacOs)
  <br/> ```venv\Scripts\activate``` (Windows)
* #### Инициализируйте гит репозиторий в папке проекта ####
  * ```git init```
  * Если требуется установка git: [Инструкция по установке](https://git-scm.com/book/ru/v2/Введение-Установка-Git)
* #### Клонируйте проект в свой репозиторий ####
  * ```git clone https://github.com/KrasovaLena/AvitoQA_2024```
* #### Установите необходимые для работы пакеты: ####
  * Установите Pytest: <br/> ```pip install pytest```
  * Установите Playwright: <br/> ```pip install playwright```
  * Установите плагин Pytest: <br/> ```pip install pytest-playwright```
  * Установите браузеры для пакета playwright: <br/> ```playwright install```
* #### Удалите все скриншоты из папки «output» перед запуском тестов ####
* #### Запустите тесты ####
  * ```pytest -s -v Tests.py```

#### <br/><br/> P.S. спасибо Avito за интересные задания и возможность попрактиковаться! ####

