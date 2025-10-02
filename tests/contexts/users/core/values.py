from faker import Faker
import phonenumbers
import pytest

from contexts.users.core.values import (
    first_name as first_name_value,
    last_name as last_name_value,
    phone_number as phone_number_value,
)


def test_first_name(faker: Faker):
    first_name = first_name_value.FirstName(faker.first_name())
    assert first_name.value


def test_first_name_invalid():
    with pytest.raises(first_name_value.FirstNameTooLong):
        first_name = "1" * 51
        first_name_value.FirstName(first_name)
    with pytest.raises(first_name_value.FirstNameEmpty):
        first_name = ""
        first_name_value.FirstName(first_name)


def test_last_name(faker: Faker):
    last_name = last_name_value.LastName(faker.last_name())
    assert last_name.value


def test_last_name_invalid():
    with pytest.raises(last_name_value.LastNameTooLong):
        last_name = "1" * 51
        last_name_value.LastName(last_name)
    with pytest.raises(last_name_value.LastNameEmpty):
        last_name = ""
        last_name_value.LastName(last_name)


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
