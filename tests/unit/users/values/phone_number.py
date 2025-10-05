from faker import Faker
import phonenumbers
import pytest

from contexts.users.app.values import phone_number as phone_number_value


def generate_valid_phone_number(region: str) -> str:
    parsed_number = phonenumbers.example_number(region)
    if parsed_number is None:
        raise ValueError("Invalid test")
    return phonenumbers.format_number(
        parsed_number,
        phonenumbers.PhoneNumberFormat.E164,
    )


def test_phone_number():
    phone_number = phone_number_value.PhoneNumber(generate_valid_phone_number("RU"))
    assert phone_number.value


def test_phone_number_invalid(faker: Faker):
    with pytest.raises(phone_number_value.PhoneNumberEmpty):
        phone_number = ""
        phone_number_value.PhoneNumber(phone_number)
    with pytest.raises(phone_number_value.PhoneNumberUnsupportedRegion):
        phone_number = generate_valid_phone_number("US")
        phone_number_value.PhoneNumber(phone_number)
    with pytest.raises(phone_number_value.PhoneNumberInvalid):
        phone_number_value.PhoneNumber(faker.text())
    with pytest.raises(phone_number_value.PhoneNumberInvalid):
        phone_number_value.PhoneNumber("+719999999999")
