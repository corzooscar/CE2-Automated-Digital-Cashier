# 🏦 Basic ATM Simulator

A simple program to simulate basic ATM operations using a single shared balance.

---

## ⚙️ Initial Setup

Upon starting, the program can establish the following parameters:
* **Initial Balance:** Set automatically to **$1000**.
* **Operation Cycle:** Ask the user how many operations they wish to perform during the session.

> **Note:** The system doesn't handle multiple accounts or complex accumulators. It only works with a single, shared balance throughout the execution.

---

## 📋 Transaction Menu

For each transaction, the system can display the following menu and prompt the user to select an option:

| Option | Action | Description |
| :---: | :--- | :--- |
| **1** | Check Balance | Displays the current available funds. |
| **2** | Withdraw Money | Allows the user to extract funds, validating the current balance. |
| **3** | Deposit Money | Allows the user to add new funds to the account. |

---

## 📜 Option Rules & Logic

### Option 1: Check Balance
* Display the current balance.

### Option 2: Withdraw Money
* Prompt the user for the amount to withdraw.
* **Validations:**
  * If the amount is **greater than the balance** 👉 display: *"Insufficient funds"*.
  * If the amount is **less than or equal to the balance** 👉 process the withdrawal and display the new balance.
  * If the amount is **negative** 👉 keep prompting for the amount (in a loop) until a valid value is entered.

### Option 3: Deposit Money
* Prompt the user for the amount to deposit.
* **Validations:**
  * If the amount is **negative** 👉 keep prompting for the amount until a valid value is entered.
  * If the amount is **valid (positive)** 👉 add it to the balance and display the new balance.
