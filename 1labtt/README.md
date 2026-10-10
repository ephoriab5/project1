# Звіт до роботи
## Тема: Тестування
### Мета роботи: Дізнаватись про види тестування,а також як і коли ними користуватись

---
### Виконання роботи
#### classic tests
* 
    1. 01_general_testing
    2. app.py and test_app.py
    3. Passed
    4. Навчились користуватись класичними unit-тестами
       
     ![01](/pictures/tt01.png)



  #### tests by library "pytest"
    1. 02_pytest
    2. app.py and test_app.py
    3. Passed
    4. Навчились користуватись бібліотекою pytest

    ![02](/pictures/tt02.png)



    #### code coverage
    1. 03_coverage
    2. app.py and test_app.py
    3. Passed
    4. Навчились користуватись бібліотекою coverage

    ![03](/pictures/tt03.png)
    ![03](/pictures/tt03s.png)



    #### integration testing
    1. 04_integration_tests
    2. app.py and test_app.py
    3. Passed
    4. Навчились користуватись інтеграційним методом тестування

    ![04](/pictures/tt04.png)



* вставлений код / текстовий або числовий результат / інші результати:
    ```python
    app.py
    class Figure:
    def __init__(self, figure_type: str, length: float):
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль!")
        
        self.figure_type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.figure_type

    @property
    def get_figure_length(self) -> float:
        return self.length

    @property
    def get_angles(self) -> int:
        """Метод, який повертає кількість кутів залежно від типу фігури."""
        fig_type = self.figure_type.lower()
        if fig_type in ["квадрат", "прямокутник"]:
            return 4
        elif fig_type in ["трикутник"]:
            return 3
        else:
            raise ValueError(f"Невідомий тип фігури: {self.figure_type}")

    test.py
    import pytest
    from app import Figure

    def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.type == "трикутник"

    def test_invalid_length():
    with pytest.raises(AssertionError):
        Figure("квадрат", 0)


    ```
    
  
    

---
### Висновок:
> у висновку потрібно відповісти на запитання:

- Методи тестування;
- Yes;
- Дізнався про методи тестування та як ними користуватись,а також про бібліотеки для полегшення роботи при тестуванні;
- Так;
- Так;
- Ні;
- Так;
- Все на вищому рівні.

---
