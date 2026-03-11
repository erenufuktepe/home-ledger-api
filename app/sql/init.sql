CREATE SCHEMA IF NOT EXISTS finance;

DROP TABLE IF EXISTS finance.transactions;

DROP TABLE IF EXISTS finance.recurring_payments;

DROP TABLE IF EXISTS finance.cashback_rates;

DROP TABLE IF EXISTS finance.credit_cards;

DROP TABLE IF EXISTS finance.loans;

DROP TABLE IF EXISTS finance.incomes;

DROP TABLE IF EXISTS finance.account_snapshots;

DROP TABLE IF EXISTS finance.accounts;

DROP TABLE IF EXISTS finance.users;

CREATE TABLE finance.users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS finance.accounts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL,
    name VARCHAR(120) NOT NULL,
    account_type VARCHAR(50) NOT NULL,
    balance NUMERIC(12, 2) NOT NULL,
    apy NUMERIC(5, 2) NULL,
    is_joint BOOLEAN NOT NULL DEFAULT FALSE,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_accounts_user_id
        FOREIGN KEY (user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.account_snapshots (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_id BIGINT NOT NULL,
    balance NUMERIC(12, 2) NOT NULL,
    snapshot_datetime TIMESTAMP NOT NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_account_snapshots_account_id
        FOREIGN KEY (account_id) REFERENCES finance.accounts (id)
);

CREATE TABLE IF NOT EXISTS finance.incomes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    income_type VARCHAR(10) NOT NULL,
    frequency VARCHAR(20) NOT NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_incomes_user_id
        FOREIGN KEY (user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.loans (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    user_id BIGINT NOT NULL,
    monthly_payment NUMERIC(12, 2) NOT NULL,
    remaining_amount NUMERIC(12, 2) NOT NULL,
    apr NUMERIC(5, 2) NULL,
    due_day INT NOT NULL CHECK (due_day BETWEEN 1 AND 31),
    end_date DATE NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_loans_user_id
        FOREIGN KEY (user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.credit_cards (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    user_id BIGINT NOT NULL,
    current_balance NUMERIC(12, 2) NOT NULL,
    apr NUMERIC(5, 2) NULL,
    credit_limit NUMERIC(12, 2) NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_credit_cards_user_id
        FOREIGN KEY (user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.cashback_rates (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    card_id BIGINT NOT NULL,
    category VARCHAR(50) NOT NULL,
    percentage NUMERIC(5, 2) NOT NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_cashback_rates_card_category UNIQUE (card_id, category),
    CONSTRAINT fk_cashback_rates_card_id
        FOREIGN KEY (card_id) REFERENCES finance.credit_cards (id)
);

CREATE TABLE finance.recurring_payments (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    purpose VARCHAR(10) NOT NULL,
    frequency VARCHAR(20) NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    due_day INT NULL,
    due_month INT NULL,
    user_id BIGINT NOT NULL,
    account_id BIGINT NULL,
    credit_card_id BIGINT NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_recurring_payments_user_id
        FOREIGN KEY (user_id) REFERENCES finance.users (id),
    CONSTRAINT fk_recurring_payments_account_id
        FOREIGN KEY (account_id) REFERENCES finance.accounts (id),
    CONSTRAINT fk_recurring_payments_credit_card_id
        FOREIGN KEY (credit_card_id) REFERENCES finance.credit_cards (id)
);

CREATE TABLE IF NOT EXISTS finance.transactions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    amount NUMERIC(12, 2) NOT NULL,
    recurring_payment_id BIGINT NULL,
    transaction_datetime TIMESTAMP NOT NULL,
    created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_transactions_recurring_payment_id
        FOREIGN KEY (recurring_payment_id) REFERENCES finance.recurring_payments (id)
);
