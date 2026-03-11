import enum


class IncomeType(str, enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class AccountType(str, enum.Enum):
    SAVINGS = "savings"
    CHECKING = "checking"
    IRA_TRADITIONAL = "ira traditional"
    IRA_ROTH = "ira roth"
    K401 = "401k"
    INVESTMENT = "investment"
    CRYPTO = "crypto"
    HSA = "hsa"


class Frequency(str, enum.Enum):
    MONTHLY = "monthly"
    SEMIMONTHLY = "semimonthly"
    YEARLY = "yearly"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"


class PaymentPurpose(str, enum.Enum):
    NEED = "need"
    WANT = "want"
    SAVING = "saving"


class SpendingCategory(str, enum.Enum):
    FINANCE = "finance"
    ENTERTAINMENT = "entertainment"
    HOUSING = "home & utilities"
    HEALTH = "health"
    GROCERIES = "groceries"
    DINING = "restaurants & dining"
    TRANSPORTATION = "transportation"
    INSURANCE = "insurance"
    LOAN = "loan"
    ONLINE = "online shopping"
    OTHER = "other"
