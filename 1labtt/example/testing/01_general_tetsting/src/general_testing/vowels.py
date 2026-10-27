def count_vowels(text: str) -> int:
    """Рахує кількість голосних літер (українських та англійських) у рядку."""
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком")
    
    # Список голосних (маленькі та великі, укр. і англ.)
    vowels = "аеєиіїоуюяaeiouyАЕЄИІЇОУЮЯAEIOUY"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_symbols(text: str) -> int:
    return len(text)