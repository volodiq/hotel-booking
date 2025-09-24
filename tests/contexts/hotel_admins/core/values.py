from faker import Faker
import phonenumbers
import pytest

from contexts.hotel_admins.core import errors, values


def test_first_name(faker: Faker):
    first_name = values.FirstName(faker.first_name())
    assert first_name.value


def test_first_name_constraint(faker: Faker):
    with pytest.raises(errors.FirstNameTooLong):
        first_name = "1" * 51
        values.FirstName(first_name)
    with pytest.raises(errors.FirstNameEmpty):
        first_name = ""
        values.FirstName(first_name)


def test_last_name(faker: Faker):
    last_name = values.LastName(faker.last_name())
    assert last_name.value


def test_last_name_constraint(faker: Faker):
    with pytest.raises(errors.LastNameTooLong):
        last_name = "1" * 51
        values.LastName(last_name)
    with pytest.raises(errors.LastNameEmpty):
        last_name = ""
        values.LastName(last_name)


def generate_valid_phone_number(region: str, format: int) -> str:
    parsed_number = phonenumbers.example_number(region)
    if parsed_number is None:
        raise ValueError("Invalid test")

    return phonenumbers.format_number(
        parsed_number,
        format,
    )


def test_phone_number():
    phone_number_e164 = generate_valid_phone_number("RU", phonenumbers.PhoneNumberFormat.E164)
    values.PhoneNumber(phone_number_e164)

    phone_number_rfc = generate_valid_phone_number("RU", phonenumbers.PhoneNumberFormat.RFC3966)
    values.PhoneNumber(phone_number_rfc)


def test_phone_number_constraint():
    with pytest.raises(errors.PhoneNumberEmpty):
        values.PhoneNumber("")
    with pytest.raises(errors.PhoneNumberUnsupportedRegion):
        values.PhoneNumber(generate_valid_phone_number("US", phonenumbers.PhoneNumberFormat.E164))
    with pytest.raises(errors.PhoneNumberInvalid):
        values.PhoneNumber("123")
    with pytest.raises(errors.PhoneNumberInvalid):
        values.PhoneNumber("+719999999999")
