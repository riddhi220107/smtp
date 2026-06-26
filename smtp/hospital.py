import psycopg2
conn = psycopg2.connect(
    host ="localhost",
    database="postgres",
    user="postgres",
    password="riddhi22",
    port = "5432",
)

cur = conn.cursor()

cur.execute("SELECT version();")


print(cur.fetchone())




# cur.execute("""
# CREATE TABLE Patients (
#     Patient_id SERIAL PRIMARY KEY,
#     Patient_name VARCHAR(100),
#     age INT,
#     gender VARCHAR(10),
#     phone VARCHAR(10)
#  );
# """)

# conn.commit()


cur.execute("""
INSERT INTO Patients (Patient_name, age,  gender,   phone) VALUES
('parth',20,'male','9734592463'),
('vedika',25,'female','9234561776'),
('shivansh',45,'male','9086153745'),
('aditi',20,'male','9734553689'),
('rutuja',25,'female','9235677884'),
('suhani',45,'male','9082444322') 
;
""")

conn.commit()




# cur.execute("""
# CREATE TABLE Doctor(
#     Doctor_id SERIAL PRIMARY KEY,
#     Doctor_name VARCHAR(100),
#     specialization VARCHAR(100),
#     phone VARCHAR(10)
#  );
# """)

# conn.commit()

cur.execute("""
INSERT INTO Doctor (Doctor_name, specialization, phone) VALUES
('Dr. Shah','Neurology','9000000002'),
('Dr. Rao','Orthopedics','9000000003'),
('Dr. Patel','Dermatology','9000000004'),
('Dr. Khan','Pediatrics','9000000005'),
('Dr. Mehta','Cardiology','9000000001')
;
""")

conn.commit()



# cur.execute("""
# CREATE TABLE Department(
#     Department_id SERIAL PRIMARY KEY,
#     Department_name VARCHAR(100)
#  );
# """)

# conn.commit()


cur.execute("""
INSERT INTO Department(Department_name) VALUES
('Neurology'),
('Orthopedics'),
('Dermatology'),
('Pediatrics')
;
""")
conn.commit()

# cur.execute("""
# CREATE TABLE Nurse(
#     Nurse_id SERIAL PRIMARY KEY,
#     Nurse_name VARCHAR(100),
#     Shift  VARCHAR(100)
#  );
# """)

# conn.commit()

cur.execute("""
INSERT INTO Nurse(Nurse_name, Shift) VALUES
('sheetal','day'),
('poonam','day'),
('riya','night'),
('priya','day')
;
""")

conn.commit()


# cur.execute("""
# CREATE TABLE Medicine(
#     Medicine_id SERIAL PRIMARY KEY,
#     Medicine_name VARCHAR(50),
#     price DECIMAL(10,2)
#  );
# """)

# conn.commit()

cur.execute("""
INSERT INTO Medicine(Medicine_name, price) VALUES
('Paracetamol',20),
('Aspirin',25),
('Crocin',30),
('Amoxicillin',50),
('Ibuprofen',40)
;
""")

conn.commit()

# cur.execute("""
# CREATE TABLE Room(
#     Room_id SERIAL PRIMARY KEY,
#     Room_type VARCHAR(50),
#     charges INT
#  );
# """)

# conn.commit()

cur.execute("""
INSERT INTO Room(Room_type, charges) VALUES
('general',20000),
('s-private',50000),
('private',30000),
('ICU',50000),
('deluxe',100000)
;
""")

conn.commit()

# cur.execute("""
# CREATE TABLE Bill(
#     Bill_id SERIAL PRIMARY KEY,
#     Bill_amount INT,
#     Payment_status VARCHAR(50)
#  );
# """)

# conn.commit()


cur.execute("""
INSERT INTO Bill(Bill_amount, payment_status) VALUES
(40000,'online'),
(70000,'cash'),
(60000,'cheque'),
(100000,'online'),
(80000,'cash')
;
""")

conn.commit()

# cur.execute("""
# ALTER TABLE Doctor
# ADD COLUMN department_id INT;
# """)          
# conn.commit()

# cur.execute("""
# ALTER TABLE Doctor
# ADD CONSTRAINT fk_doctor_department
# FOREIGN KEY (department_id) REFERENCES Department(department_id);
# """)

# conn.commit()


# cur.execute("""
# ALTER TABLE Nurse
# ADD COLUMN department_id INT;
# """)          
# conn.commit()

# cur.execute("""
# ALTER TABLE Nurse
# ADD CONSTRAINT fk_Nurse_department
# FOREIGN KEY (department_id) REFERENCES Department(department_id);
# """)

# conn.commit()

# cur.execute("""
# ALTER TABLE Doctor
# ADD COLUMN Patients_id INT;
# """)          
# conn.commit()

# cur.execute("""
# ALTER TABLE Doctor
# ADD CONSTRAINT fk_doctor_
# FOREIGN KEY (patients_id) REFERENCES Patients(patients_id);
# """)

# conn.commit()

# cur.execute("""
# ALTER TABLE room
# ADD COLUMN doctor_id INT;
# """)

# conn.commit()
# cur.execute("""
# ALTER TABLE room
# ADD CONSTRAINT fk_room_doctor
# FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id);
# """)

# conn.commit()

# cur.execute("""
# ALTER TABLE Bill
# ADD COLUMN Patient_id INT;
# """)
# conn.commit()

# cur.execute("""
# ALTER TABLE Bill
# ADD CONSTRAINT fk_Bill_Patients
# FOREIGN KEY (Patient_id) REFERENCES Patients(Patient_id);

# """)

# conn.commit()


# cur.execute("""
# ALTER TABLE Medicine
# ADD COLUMN Patient_id INT,
# ADD COLUMN Doctor_id INT;
# """)

# conn.commit()
# cur.execute("""
# ALTER TABLE Medicine
# ADD CONSTRAINT fk_Medicine_Patients
# FOREIGN KEY (Patient_id) REFERENCES Patients(Patient_id);
# """)

# conn.commit()
# cur.execute("""
# ALTER TABLE Medicine
# ADD CONSTRAINT fk_Medicine_Doctor
# FOREIGN KEY (Doctor_id) REFERENCES Doctor(Doctor_id);
# """)

# conn.commit()
# cur.execute("""
# ALTER TABLE room
# ADD COLUMN  Nurse_id INT;
# """)

# conn.commit()
# cur.execute("""
# ALTER TABLE room
# ADD CONSTRAINT fk_room_Nurse
# FOREIGN KEY (Nurse_id) REFERENCES Nurse(Nurse_id);
# """)

# conn.commit()



