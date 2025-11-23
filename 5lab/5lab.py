class User:
    def __init__(self, name,my_id) -> None:
        self.name = (name)
        self.my_id = my_id

class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    
    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        self.name = name if name is not None else self.anonymous_user().name

        if not isinstance(self.name, str):
            raise TypeError(f"Ім'я має бути рядком, отримано: {type(self.name).__name__}.")
        if any(char.isdigit() for char in self.name):
            raise ValueError("Ім'я може містити лише літери!")
        if not self.name.replace(' ', '').isalpha():
            raise ValueError("Ім'я може містити лише літери!")
        
        MyName.total_names += 1 
        self.my_id = MyName.total_names
        self.name = self.name.capitalize()
        
        
    
    @property
    def full_name(self) -> str:
        """Class property
        Повертає ім'я користувача, ID та email у заданому форматі.
        Формат: "User #<id>: <name> (<email>)"
        """
        user_id = self.my_id
        user_name = self.name
        user_email = self.create_email() 
        
        return f"User #{user_id}: {user_name} ({user_email})"
        
        
    def count_letters(self) -> int:
        """Instance method
        return: кількість літер в імені
        """
        return len(self.name)
    
    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"

    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл (за замовчуванням)
        """
        return self.create_email()

    def create_email(self, domain: str = "itcollege.lviv.ua") -> str:
        """Instance method
        return: створюємо емейл з можливістю модифікації домену
        """
        return f"{self.name}@{domain}"
    

    @classmethod
    def anonymous_user(cls):
        """Class method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello from static method!") -> str:
        
       print("----Static method says hello!----")
       print (f"----змінна message має {(message)}----")
       print("----hello" "," + " world----")
    
    def save_to_file(self, filename: str = "a.txt") -> None:
        """Instance method
        Додає рядок із повним записом користувача до вказаного файлу.
        """
        
        record_line = self.full_name
        record_line += f" | Letters: {self.count_letters()}"
        record_line += f" | Email: {self.create_email()}"
        record_line += f" | ID: {self.my_id}"
        record_line += f" | WhoAmI: {self.whoami}"
        
        try:
            with open(filename, 'a', encoding='utf-8') as f:
                # Додаємо рядок і символ нового рядка (\n)
                f.write(record_line + '\n')
            print(f"✅ Запис успішно додано до файлу: {filename}")
        except Exception as e:
            print(f"❌ Помилка при запису у файл: {e}")


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", "Ruslan", None,"Anastasia")
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
This Object haves : {me.count_letters()} letters
This full name is: {me.full_name}
{"<*>"*20}""")

me.save_to_file()

    
    

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")
