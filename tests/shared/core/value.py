from faker import Faker
import pytest

from kernel.seedwork.errors import DomainError
from kernel.seedwork.value_object import ValueObject


class SomeValueTooLong(DomainError):
    def details(self) -> str:
        return "Value is too long"


class SomeValue(ValueObject[str]):
    def validate(self):
        if len(self.value) > 10:
            raise SomeValueTooLong()


def test_value_object_success(faker: Faker):
    text = faker.text(max_nb_chars=10)
    some_value = SomeValue(text)
    assert some_value._value == text


def test_value_object_validation(faker: Faker):
    text = faker.text() * 11
    with pytest.raises(SomeValueTooLong):
        SomeValue(text)
