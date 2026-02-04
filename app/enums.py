import enum


class IncomeType(str, enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class Frequency(str, enum.Enum):
    MONTHLY = "monthly"
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
