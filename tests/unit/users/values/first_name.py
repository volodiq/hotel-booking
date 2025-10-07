from faker import Faker
import pytest

from contexts.users.app.values.first_name import (
    FirstName,
    FirstNameInvalidError,
    FirstNameInvalidReason,
)


def test_first_name(faker: Faker):
    first_name = FirstName(faker.first_name())
    assert first_name.value


@pytest.mark.parametrize(
    "first_name, reason",
    [
        ("1" * 51, FirstNameInvalidReason.TOO_LONG),
        ("", FirstNameInvalidReason.EMPTY),
    ],
)
def test_first_name_invalid(first_name, reason):
    with pytest.raises(FirstNameInvalidError) as e:
        FirstName(first_name)

    assert e.value.reason == reason
