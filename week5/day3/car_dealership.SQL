CREATE TABLE IF NOT EXISTS customer(
	customer_id SERIAL PRIMARY KEY, 
	first_name VARCHAR(100),
	last_name VARCHAR(100),
    phone INT,
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS vehicle(
	vehicle_id SERIAL PRIMARY KEY, 
	VIN VARCHAR(100),
	make VARCHAR(100),
    model VARCHAR(100),
    car_year INT,
    color VARCHAR(100),
    engine_type VARCHAR(100),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE IF NOT EXISTS employee(
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS service_ticket(
   ticket_id SERIAL PRIMARY KEY,
   FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
   FOREIGN KEY(vehicle_id) REFERENCES vehicle(vehicle_id),
   FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
   service_date DATE PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS invoice(
   invoice_id SERIAL PRIMARY KEY,
   FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
   FOREIGN KEY(vehicle_id) REFERENCES vehicle(vehicle_id),
   FOREIGN KEY(employee_id) REFERENCES employee(employee_id),
   FOREIGN KEY(service_date) REFERENCES service_ticket(service_date),
   FOREIGN KEY(ticket_id) REFERENCES service_ticket(ticket_id)
);


INSERT INTO customer(first_name,last_name,phone,email)
VALUES
('Barry','Brown','bbrown@aol.com'),
('Billy','Brooks','bbrooks@aol.com'),
('Bobby','Berry','bberry@outlook.com'),
('Brett','Boyd','bboyd@icloud.com'),
('Bailey','Bishop','bbishop@hotmail.com'),
('Benjamin','Burton','bburton@outlook.com'),
('Bennett','Barrett','bbarrett@icloud.org'),
('Beatrice','Bates','bbates@outlook.org'),
('Brooks','Beck','bbeck@hotmail.com'),
('Barbara','Byrd','bbyrd@yahoo.com'),
('Brandon','Barnes','bbarnes@aol.com');

INSERT INTO vehicle(VIN,make,model,car_year,color)
VALUES
('VQL567DJ38KH','toyota','prius','2011','yellow'),
('HEJ54JJKL23J','honda','insight','2004','black'),
('JDK67HJDJ23H','volkswagen','passat','2009','orange'),
('PLO2J456J2HJ','honda','accord','2015','black'),
('PW4IO678J3H2','honda','civic','2019','silver'),
('HDJ87JK23HJG','subaru','outback','2010','white'),
('NM32JK76OKU5','mclaren','f1','2020','black'),
('OPW57HJ5H23G','toyota','corolla','2015','white'),
('UY12TY4GHJH4','honda','civic','2011','blue'),
('HIUY67HJ5JKL','ford','focus','2020','silver'),
('VI69M3256NJ6','ford','f150','2006','gray');
