from faker import Faker
import pytest

from contexts.users.core.values import first_name as first_name_value


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
