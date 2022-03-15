CREATE DATABASE sneakerstore_database;
CREATE USER order_app WITH PASSWORD 'P@ss1234';
GRANT ALL PRIVILEGES ON DATABASE sneakerstore_database to order_app;
\c sneakerstore_database

CREATE TABLE customers (
  customer_id     INTEGER NOT NULL,
  first_name      VARCHAR(32) NOT NULL,
  last_name       VARCHAR(32) NOT NULL,
  email_address   VARCHAR(32) NOT NULL,
  street_address  VARCHAR(32) NOT NULL,
  city            VARCHAR(32) NOT NULL,
  state           VARCHAR(16) NOT NULL,
  zip             VARCHAR(16) NOT NULL,
  phone           VARCHAR(16) NOT NULL,
  PRIMARY KEY     ( customer_id )
);

CREATE TABLE employees (
  employee_id     INTEGER NOT NULL,
  first_name      VARCHAR(32) NOT NULL,
  last_name       VARCHAR(32) NOT NULL,
  position        VARCHAR(32) NOT NULL,
  lvl             VARCHAR(16) NOT NULL,
  PRIMARY KEY     ( employee_id )
);

CREATE TABLE inventory (
  style_id        INTEGER NOT NULL,
  brand           VARCHAR(128) NOT NULL,
  name            VARCHAR(256) NOT NULL,
  color           VARCHAR(64) NOT NULL,
  cost            VARCHAR(32) NOT NULL,
  retail          VARCHAR(16) NOT NULL,
  PRIMARY KEY     ( style_id )
);

CREATE TABLE orders (
  order_id        INTEGER NOT NULL,
  quantity        INTEGER NOT NULL,
  payment_method  VARCHAR(16) NOT NULL,
  total           VARCHAR(16) NOT NULL,
  style_id        INTEGER NOT NULL,
  customer_id     INTEGER NOT NULL,
  employee_id     INTEGER NOT NULL,
  PRIMARY KEY ( order_id, customer_id, style_id ),
  CONSTRAINT fk_style FOREIGN KEY (style_id) REFERENCES inventory(style_id),
  CONSTRAINT fk_emp FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
  CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

GRANT ALL PRIVILEGES ON customers, employees, inventory, orders TO order_app;
