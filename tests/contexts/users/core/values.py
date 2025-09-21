from faker import Faker
import phonenumbers
import pytest

from contexts.users.core import errors as exc
from contexts.users.core.values import FirstName, LastName, PhoneNumber


def test_first_name(faker: Faker):
    first_name = FirstName(faker.first_name())
    assert first_name.value


def test_first_name_invalid():
    with pytest.raises(exc.FirstNameTooLong):
        first_name = "1" * 51
        FirstName(first_name)
    with pytest.raises(exc.FirstNameEmpty):
        first_name = ""
        FirstName(first_name)


def test_last_name(faker: Faker):
    last_name = LastName(faker.last_name())
    assert last_name.value


def test_last_name_invalid():
    with pytest.raises(exc.LastNameTooLong):
        last_name = "1" * 51
        LastName(last_name)
    with pytest.raises(exc.LastNameEmpty):
        last_name = ""
        LastName(last_name)


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


def test_phone_number_invalid(faker: Faker):
    with pytest.raises(exc.PhoneNumberEmpty):
        phone_number = ""
        PhoneNumber(phone_number)
    with pytest.raises(exc.PhoneNumberUnsupportedRegion):
        phone_number = generate_valid_phone_number("US")
        PhoneNumber(phone_number)
    with pytest.raises(exc.PhoneNumberInvalid):
        PhoneNumber(faker.text())
    with pytest.raises(exc.PhoneNumberInvalid):
        PhoneNumber("+719999999999")
