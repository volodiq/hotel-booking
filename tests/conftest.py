import faker
import pytest


@pytest.fixture()
def get_faker() -> faker.Faker:
    return faker.Faker(locale="ru_RU")
