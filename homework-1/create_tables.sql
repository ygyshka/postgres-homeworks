-- SQL-команды для создания таблиц

create table customers
(
	customer_id varchar(100) primary key,
	company_name varchar(100) not null,
	contact_name varchar(100)
);

create table employers
(
	employer_id int primary key,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title varchar(100) not null,
	birth_date date,
	notes text
);

create table orders
(
	order_id int primary key,
	customer_id varchar(100) references customers(customer_id),
	employer_id int not null references employers(employer_id),
	order_date date,
	ship_city varchar(100) not null
);

