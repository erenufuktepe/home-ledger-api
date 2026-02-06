CREATE SCHEMA IF NOT EXISTS finance;

DROP TABLE IF EXISTS finance.credit_cards;

DROP TABLE IF EXISTS finance.loans;

DROP TABLE IF EXISTS finance.incomes;

DROP TABLE IF EXISTS finance.recurring_payments;

DROP TABLE IF EXISTS finance.users;

CREATE TABLE finance.users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE finance.recurring_payments (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    purpose VARCHAR(10) NOT NULL CHECK (
        purpose IN ('need', 'want', 'saving')
    ),
    frequency VARCHAR(20) NOT NULL CHECK (
        frequency IN (
            'monthly',
            'yearly',
            'weekly',
            'biweekly'
        )
    ),
    amount NUMERIC(12, 2) NOT NULL,
    due_day INT NULL,
    due_month INT NULL,
    payer_user_id BIGINT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT ck_due_day_range CHECK (
        due_day IS NULL
        OR due_day BETWEEN 1 AND 31
    ),
    CONSTRAINT ck_due_month_range CHECK (
        due_month IS NULL
        OR due_month BETWEEN 1 AND 12
    ),
    FOREIGN KEY (payer_user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.incomes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    owner_user_id BIGINT NOT NULL,
    amount NUMERIC(12, 2) NOT NULL,
    income_type VARCHAR(10) NOT NULL CHECK (
        income_type IN ('primary', 'secondary')
    ),
    frequency VARCHAR(20) NOT NULL CHECK (
        frequency IN (
            'monthly',
            'yearly',
            'weekly',
            'biweekly'
        )
    ),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (owner_user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.loans (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    payer_user_id BIGINT NOT NULL,
    monthly_payment NUMERIC(12, 2) NOT NULL,
    due_day INT NOT NULL CHECK (due_day BETWEEN 1 AND 31),
    end_date DATE NULL,
    FOREIGN KEY (payer_user_id) REFERENCES finance.users (id)
);

CREATE TABLE IF NOT EXISTS finance.credit_cards (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    owner_user_id BIGINT NOT NULL,
    current_balance NUMERIC(12, 2) NOT NULL,
    FOREIGN KEY (owner_user_id) REFERENCES finance.users (id)
);