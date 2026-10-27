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