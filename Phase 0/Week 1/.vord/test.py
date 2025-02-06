import unittest

# Fungsi yang telah dibuat sebelumnya untuk menghitung kalori terbakar
def calories_burned(duration, exercise):
    exercise_calories = {
        'berlari': 10,
        'bersepeda': 8,
        'berenang': 12
    }
    
    if exercise in exercise_calories:
        calories_per_minute = exercise_calories[exercise]
        total_calories = calories_per_minute * duration
        return total_calories
    else:
        return "Jenis kegiatan tidak diketahui"

# Fungsi baru untuk menghitung total kalori terbakar dari beberapa sesi latihan
def total_session_burned_cal(*args, each_session_duration):
    total_calories = 0
    
    for exercise in args:
        calories = calories_burned(each_session_duration, exercise)
        # Pastikan fungsi calories_burned tidak mengembalikan error message
        if isinstance(calories, int):
            total_calories += calories
        else:
            return calories  # Jika ada jenis kegiatan tidak dikenal, kembalikan pesan error tersebut
    
    return total_calories

# Unit testing untuk fungsi-fungsi di atas
class TestCaloriesFunctions(unittest.TestCase):
    def test_calories_burned(self):
        self.assertEqual(calories_burned(60, 'berenang'), 720)
        self.assertEqual(calories_burned(15, 'berlari'), 150)
        self.assertEqual(calories_burned(20, 'bersepeda'), 160)
        self.assertEqual(calories_burned(10, 'yoga'), "Jenis kegiatan tidak diketahui")
    
    def test_total_session_burned_cal(self):
        self.assertEqual(total_session_burned_cal('berenang', 'bersepeda', each_session_duration=10), 200)
        self.assertEqual(total_session_burned_cal('berenang', 'berlari', 'bersepeda', each_session_duration=5), 150)
        self.assertEqual(total_session_burned_cal('berenang', 'yoga', each_session_duration=10), "Jenis kegiatan tidak diketahui")

# Menjalankan unit test
unittest.main(argv=[''], exit=False)
