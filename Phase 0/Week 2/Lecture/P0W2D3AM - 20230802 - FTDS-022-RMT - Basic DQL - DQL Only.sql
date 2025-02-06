-- Basic query
SELECT * FROM students;

-- Mengambil column name dan age
SELECT name, age FROM students;

-- Mengambil semua data dari table students dengan alias
SELECT * 
FROM students AS s;

SELECT *
FROM students s;

-- Menampilkan column name dengan nama alias
SELECT name AS full_name
FROM students s;

-- Mengurutkan students yang memiliki usia termuda hingga usia tertua
SELECT *
FROM students
ORDER BY age ASC, id ASC;

-- Mengurutkan daftar campus dari waktu terkini ke waktu yang lebih lampau
SELECT *
FROM campus
ORDER BY start_date DESC;

-- Mencari daftar usia yang unik
SELECT DISTINCT age
FROM students;

-- Mencari student yang unik berdasarkan age dan campus_id
SELECT DISTINCT age, campus_id
FROM students
ORDER BY age;

-- Mencari nama student yang berusia 20 tahun
SELECT name
FROM students
WHERE age=20;

-- Mencari nama student yang bukan berusia 20 tahun
SELECT name, age
FROM students
WHERE age<>20;

SELECT name, age
FROM students
WHERE age!=20;

-- Mencari nama student yang memiliki total_grade lebih besar dari 80
SELECT name, total_grade
FROM students
WHERE total_grade > 80;

-- Mencari nama student yang bukan berusia 20 tahun dan memiliki total_grade lebih besar dari 80
SELECT name, age, total_grade
FROM students
WHERE age <> 20 AND total_grade > 80;

-- Mencari nama student yang memiliki campus_id=1 ATAU memiliki total_grade diatas 90
SELECT name, campus_id, total_grade
FROM students
WHERE campus_id=1 OR total_grade>90;

-- Mencari nama student yang memiliki umur 18, 19, dan 20
SELECT name, age
FROM students
WHERE age=18 OR age=19 OR age=20;

SELECT name, age
FROM students
WHERE age IN (18, 19, 20);

SELECT name, age
FROM students
WHERE age BETWEEN 18 AND 20;

SELECT name, age
FROM students
WHERE age > 17 AND age < 21;

-- Mencari student yang memiliki nama David Hartono
SELECT *
FROM students
WHERE name='David Hartono';

-- Mencari student yang memiliki karakter pertama huruf R pada namanya
SELECT *
FROM students
WHERE name LIKE 'R%';

SELECT *
FROM students
WHERE name ILIKE 'r%';

-- Mencari student yang memiliki karakter terakhir huruf n pada namanya
SELECT *
FROM students
WHERE name LIKE '%n';

-- Mencari student yang memiliki karakter "ar" ditengah namanya
SELECT *
FROM students
WHERE name ILIKE '%ar%';

-- Mencari banyaknya data di table students
SELECT COUNT(*) AS jumlah_data
FROM students;

-- Mencari rata-rata total_grade dari table students
SELECT AVG(total_grade)
FROM students;

-- Mencari rata-rata total_grade dengan campus_id=1 dari table students
SELECT AVG(total_grade)
FROM students
WHERE campus_id=1;

-- Mencari rata-rata total_grade per masing-masing campus_id
SELECT campus_id, AVG(total_grade)
FROM students
GROUP BY campus_id
ORDER BY campus_id ASC;

-- Mencari campus_id yang nilai rata-rata total_gradenya diatas 85
SELECT campus_id, AVG(total_grade)
FROM students
GROUP BY campus_id
HAVING AVG(total_grade) > 85

-- Mencari jumlah student per masing-masing campus_id
SELECT campus_id, COUNT(name) AS total_student
FROM students
GROUP BY campus_id;

-- Join table antara table students dengan table campus
SELECT *
FROM students
INNER JOIN campus ON students.campus_id=campus.id;

-- Menampilkan name, age, campus_name, batch dari hasil join table antara students dengan campus
SELECT t1.name, t1.age, t2.campus_name, t2.batch
FROM students t1
INNER JOIN campus t2 ON t1.campus_id=t2.id;

-- Create the assignment_scores table
CREATE TABLE assignment_scores (
    id SERIAL PRIMARY KEY,
    students_id INTEGER,
    assignment_id INTEGER,
    score FLOAT
);

-- Insert data into the students table
INSERT INTO assignment_scores (students_id, assignment_id, score)
VALUES
    (1, 1, 90.0),
    (1, 2, 85.0),
    (2, 1, 92.5),
    (2, 2, 88.5),
    (3, 1, 80.0),
    (4, 2, 79.5),
    (4, 1, 95.0),
    (4, 2, 90.5),
    (5, 1, 88.0),
    (5, 2, 86.0),
    (6, 2, 86.0);

-- Join 3 table
SELECT *
FROM students
INNER JOIN campus ON students.campus_id=campus.id
INNER JOIN assignment_scores ON students.id=assignment_scores.students_id



