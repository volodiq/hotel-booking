from faker import Faker
import pytest

from contexts.users.app.values import last_name as last_name_value


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
