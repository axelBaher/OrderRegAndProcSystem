from enum import Enum


class PaymentType(Enum):
    PURCHASE = 1,
    REFUND = 2,
    CREDIT = 3,
    DEBIT = 4


class PaymentMethod(Enum):
    CASH_ON_DELIVERY = 1,
    CARD_ON_DELIVERY = 2,
    CARD_ONLINE = 3,


class CurrencyCode(Enum):
    USD = "USD"  # United States Dollar
    EUR = "EUR"  # Euro
    GBP = "GBP"  # British Pound Sterling
    JPY = "JPY"  # Japanese Yen
    CNY = "CNY"  # Chinese Yuan
    CAD = "CAD"  # Canadian Dollar
    AUD = "AUD"  # Australian Dollar
    CHF = "CHF"  # Swiss Franc
    RUB = "RUB"  # Russian Ruble
    INR = "INR"  # Indian Rupee
    BRL = "BRL"  # Brazilian Real
    MXN = "MXN"  # Mexican Peso
    KRW = "KRW"  # South Korean Won
    SEK = "SEK"  # Swedish Króna
    NZD = "NZD"  # New Zealand Dollar
    SGD = "SGD"  # Singapore Dollar
    HKD = "HKD"  # Hong Kong Dollar
    TWD = "TWD"  # New Taiwan Dollar
    ZAR = "ZAR"  # South African Rand
