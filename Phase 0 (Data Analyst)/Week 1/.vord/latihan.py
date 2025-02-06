if __name__ == "__main__":
    a = int(input())
    b = int(input())

def calories_burned(duration, exercise):
    # dictionary untuk menyimpan kegiatan olahraga
    exercise_calories = {
        'berlari': 10,
        'bersepeda': 8,
        'berenang': 12
    }
    
    # kalori terbakar
    if exercise in exercise_calories:
        calories_per_minute = exercise_calories[exercise]
        total_calories = calories_per_minute * duration
        return total_calories
    else:
        return "Jenis kegiatan tidak diketahui"

# contoh:
print(calories_burned(duration=60, exercise='berenang'))  
print(calories_burned(duration=15, exercise='berlari'))   
print(calories_burned(duration=20, exercise='bersepeda')) 
print(calories_burned(duration=30, exercise='yoga'))      
