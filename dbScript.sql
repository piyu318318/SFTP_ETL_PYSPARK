CREATE DATABASE IF NOT EXISTS loan;
USE loan;
CREATE TABLE IF NOT EXISTS loan_details (
    loan_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    loan_amount DECIMAL(15,2),
    interest_rate DECIMAL(5,2),
    loan_type VARCHAR(50),
    tenure_months INT,
    start_date DATE,
    emi_amount DECIMAL(12,2),
    emi_paid_till_date INT,
    next_due_date DATE,
    status VARCHAR(20)
);
