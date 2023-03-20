USE db;

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY auto_increment NOT NULL ,
	name varchar(100),
	cpf varchar(14) UNIQUE,
	email varchar(100),
	phone_number varchar(15),
	created_at DATETIME,
	updated_at DATETIME
);

CREATE TABLE IF NOT EXISTS orders (
	id INT PRIMARY KEY auto_increment NOT NULL,
	user_id INT NOT NULL,
	item_description varchar(300) ,
	item_quantity INT ,
	item_price varchar(100) ,
	total_value varchar(100) ,
	created_at DATETIME ,
	updated_at DATETIME,
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

