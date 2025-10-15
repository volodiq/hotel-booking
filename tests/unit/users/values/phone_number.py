import phonenumbers
import pytest

from src.contexts.users.core.values.phone_number import (
    PhoneNumber,
    PhoneNumberInvalidError,
    PhoneNumberInvalidReason,
)


def generate_valid_phone_number(region: str) -> str:
    parsed_number = phonenumbers.example_number(region)
    if parsed_number is None:
        raise ValueError("Invalid test")
    return phonenumbers.format_number(
        parsed_number,
        phonenumbers.PhoneNumberFormat.E164,
    )


def test_phone_number():
    phone_number = PhoneNumber(generate_valid_phone_number("RU"))
    assert phone_number.value


@pytest.mark.parametrize(
    "phone_number, reason",
    [
        ("", PhoneNumberInvalidReason.EMPTY),
        (generate_valid_phone_number("US"), PhoneNumberInvalidReason.UNSUPPORTED_REGION),
        ("+719999999999", PhoneNumberInvalidReason.INVALID),
    ],
)
def test_phone_number_invalid(phone_number, reason):
    with pytest.raises(PhoneNumberInvalidError) as e:
        PhoneNumber(phone_number)

    assert e.value.reason == reason
