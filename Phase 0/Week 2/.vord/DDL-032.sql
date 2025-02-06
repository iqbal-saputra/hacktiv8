CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    campus_id INTEGER,
    total_grade FLOAT
);

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Rafif Iman', 20, 1, 85.5),
    ('Hana Arisona', 21, 2, 90.2),
    ('Raka Purnomo', 19, 1, 78.9),
    ('Danu Irfansyah', 20, 3, 92.7),
    ('Rachman Ardhi', 22, 2, 88.1);

-- Create the campus table
CREATE TABLE campus (
    id SERIAL PRIMARY KEY,
    campus_name VARCHAR(50),
    batch VARCHAR(10),
    start_date DATE
);

-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');

-- Insert new data into the students table
INSERT INTO students (name, age, campus_id, total_grade)
VALUES
    ('Amir Nasution', 20, 1, 97.5),
    ('David Hartono', 21, 2, 83.2),
    ('Putri Ineke', 18, 2, 86.3),
    ('Tiara NIngrum', 17, 3, 84.4),
    ('Bayu Setiawan', 20, 2, 70.8);