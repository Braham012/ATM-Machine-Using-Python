# 🏦 ATM Machine (Bank Management System) — Python & MySQL
This project simulates the functionality of an Automated Teller Machine (ATM) by combining Python’s programming capabilities with an SQL database for data storage and management. The system allows users to create accounts, authenticate using a PIN, and perform common banking operations such as checking balance, depositing money , withdrawing cash.
## 📌 Overview
The ATM Machine (Bank Management System) is a console-based Python application that simulates essential banking operations while storing and retrieving customer data from a MySQL database.

It allows customers to:

Register for a new account

Authenticate with a PIN

Deposit and withdraw funds

Check account balance

This project demonstrates Python–MySQL integration using the mysql-connector-python library and is a great example for beginners learning database-driven applications.

## ✨ Features
#### ✅ User Registration — Create a new account with name, customer ID, PIN, and initial deposit.
#### ✅ Secure Login — Authenticate using customer ID and PIN.
#### ✅ Deposit — Add funds to your account.
#### ✅ Withdraw — Withdraw funds with insufficient balance validation.
#### ✅ Balance Inquiry — Check current account balance.
#### ✅ Database Persistence — All data stored securely in MySQL.

## 🛠️ Tech Stack
Programming Language: Python 

Database: MySQL

Connector: mysql-connector-python

## 📂 Database Schema

| Column         | Type         | Description                  |
| -------------- | ------------ | ---------------------------- |
| CUSTOMER\_NAME | VARCHAR(20)  | Name of the customer         |
| CUSTOMER\_ID   | INT          | Unique customer ID (Primary) |
| PIN            | INT          | 4-digit ATM PIN              |
| AMOUNT         | INT          | Account balance              |


## 🖼️ Screenshots
### Balance Enquiry
![Balanceenquiry](https://github.com/Braham012/Bank-Management-Using-Python/blob/main/Working%20Screenshot/Screenshot%202025-08-13%20213959.png?raw=true)
![database](https://github.com/Braham012/Bank-Management-Using-Python/blob/main/Working%20Screenshot/Screenshot%202025-08-13%20214435.png?raw=true)

### User Registration
![registration](https://github.com/Braham012/Bank-Management-Using-Python/blob/main/Screenshot/Screenshot%202025-08-13%20214502.png?raw=true)
![database](https://github.com/Braham012/Bank-Management-Using-Python/blob/main/Screenshot/Screenshot%202025-08-13%20214605.png?raw=true)

### Withdraw
![withdraw](https://github.com/Braham012/Bank-Management-Using-Python/blob/main/Screenshot/Screenshot%202025-08-13%20222531.png?raw=true)
![database](https://github.com/Braham012/Bank-Management-Using-Python/blob/main/Screenshot/Screenshot%202025-08-13%20222722.png?raw=true)
4. Database View
