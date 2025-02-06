--basic query
select * from students;

--mengambil column name dan age

SELECT name, age FROM students;

--mengambil semua data dari table students dengan alias
SELECT * FROM students AS s;


SELECT * 
FROM students s;

--menampilkan colomn name dengan alias
SELECT name AS full_name
FROM students s;

-- mengurutkan student yang memiliki usia termuda hingga usia tertua
SELECT *
FROM students
ORDER BY age;
--mengurutkan dari yang terkecil
SELECT *
FROM students
ORDER BY age ASC;

SELECT *
FROM students
ORDER BY age ASC, id ASC;


--mengurutkan dari yang terbesar
SELECT *
FROM students
ORDER BY age DESC;

select * from campus;


--mengurutkan daftar campus 
--dari waktu terkini ke waktu yang lebih lampau
SELECT *
FROM campus
ORDER BY start_date DESC;


--mencari daftar usia yang unik disticnt disini unik 
--bisa mencari nilai yg tidak sama
SELECT DISTINCT age
FROM students;

--mencari students yang unik berdasarkan age dan campus_id
SELECT DISTINCT age, campus_id
FROM students
ORDER BY age;

--Mencari nama students yang berusia 20 tahun
SELECT name
FROM students
WHERE age=20;

--mencari nama students yang bukan 
--berusia 20 tahun (menggunakanlebih dari)
SELECT name, age
FROM students
WHERE age<>20;

--mencari nama students yang memiliki 
--total grade lebih besar dari 80
SELECT name,total_grade
FROM students
WHERE total_grade > 80;

--mencari student yang tidak berusia 20 tahun 
--dan memiliki total grade lebih besar dari 80
SELECT name, total_grade
FROM students
WHERE age <> 20 AND total_grade > 80;

--mencari nama students yang memiliki campus id 
-- =1 ATAU memiliki total grade diatas 90
SELECT name,campus_id, total_grade
FROM students
WHERE campus_id=1 OR total_grade=90;

--mencari nama students yang memiliki umur 18,19,20
SELECT name, age
	FROM students
	WHERE age=18 OR age=19 OR age= 20;

SELECT name, age
	FROM students
	WHERE age IN (18,19,20);

SELECT name, age
	FROM students
	WHERE age BETWEEN 18 AND 20;

SELECT name, age
	FROM students
	WHERE age > 17 and < 21;

-- mencari nama students yang memiliki nama DAVID HARTONO
SELECT *
FROM students
WHERE name='David Hartono';

-- mencari students yang memiliki karakter 
--pertama huruf R pada nama nya
SELECT *
FROM students
WHERE name LIKE 'R%';

SELECT *
FROM students
WHERE name ILIKE 'r%';

--mencari students yang memiliki 
--karakter terakhir huruf N pada nama nya
SELECT *
FROM students
WHERE name LIKE '%n';

--mencari Student yang memiliki "AR" ditengah namanya"
SELECT *
FROM students
WHERE name ILIKE '%ar%';


--AGREGASI
--mencari banyaknya data di table students
SELECT COUNT (*) AS jumlah_data
FROM students;

--mencari rata rata total_grade dari table students
SELECT AVG(total_grade)
FROM students;

-- mencari rata rata total grade dengan kampus id =1 dari table students
SELECT AVG(total_grade)
FROM students
WHERE campus_id=1;

-- mencari rata rata total grade per masing masing campus id
SELECT campus_id, AVG(total_grade)
FROM students
GROUP BY campus_id
---ini diurutkan setelah diatas
SELECT campus_id, AVG(total_grade)
FROM students
GROUP BY campus_id
ORDER BY campus_id ASC;

--mencari campus id yang nilai rata rata total grade nya diatas 85
SELECT campus_id, AVG(total_grade)
FROM students
GROUP BY campus_id
HAVING AVG (total_grade) > 85

-- mencari jumlah student per masing masing campus id
SELECT campus_id, COUNT(name) AS jumlah_students
FROM students
GROUP BY campus_id;

--join table antara table students dengan table campus
SELECT *
FROM students
INNER JOIN campus ON students.campus_id=campus.id;

--menampilkan nama usia, campus name, batch dari hasil join 
--table antara students dengan campus
SELECT t1.name, t1.age, t2.campus_name, t2.batch
FROM students t1
INNER JOIN campus t2 ON t1.campus_id=t2.id;



-- Create the students table
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


--join 3 table
SELECT *
FROM students
INNER JOIN campus ON students.campus_id=campus.id
INNER JOIN assignment_scores ON students.id=assignment_scores.students_id


select * from students;