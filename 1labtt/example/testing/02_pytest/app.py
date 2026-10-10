class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: float):
        # Використовуємо AssertionError, як вимагається в прикладі pytest
        if length <= 0:
            raise AssertionError("Довжина має бути більшою за нуль!")
        self.type = figure_type
        self.length = length

    @property
    def get_figure_length(self) -> float:
        return self.length