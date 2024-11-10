class Student:
   
    def __init__(self, name="Невідомий", rating=0, height=0):
        self.__name = name         
        self.__rating = rating     
        self.__height = height     
    
    def get_name(self):
        return self.__name
    
    def get_rating(self):
        return self.__rating
    
    def get_height(self):
        return self.__height

    def set_rating(self, rating):
        self.__rating = rating
    
    def set_height(self, height):
        self.__height = height
    
    def __str__(self):
        return f"Student: {self.__name}, Rating: {self.__rating}, Height: {self.__height}"
    
    def __repr__(self):
        return f"Student({self.__name}, {self.__rating}, {self.__height})"
    
    def __del__(self):
        print(f"Deleting student {self.__name}")


def remove_low_rated_students(students):
    return [student for student in students if student.get_rating() >= 50]

if __name__ == "__main__":
    students = [
        Student("Іван Іванов", 85, 180),
        Student("Петро Петренко", 45, 175),
        Student("Марія Марієнко", 78, 168),
        Student("Олександр Олександров", 30, 172),
        Student("Анна Антонова", 95, 165)
    ]

   
    print("Перед видаленням:")
    for student in students:
        print(student)
    
  
    students = remove_low_rated_students(students)
    
    
    print("\nПісля видалення:")
    for student in students:
        print(student)
        