from faker import Faker
import pytest

from src.contexts.users.core.values.last_name import (
    LastName,
    LastNameInvalidError,
    LastNameInvalidReason,
)


def test_last_name(faker: Faker):
    last_name = LastName(faker.last_name())
    assert last_name.value


@pytest.mark.parametrize(
    "last_name, reason",
    [
        ("1" * 51, LastNameInvalidReason.TOO_LONG),
        ("", LastNameInvalidReason.EMPTY),
    ],
)
def test_last_name_invalid(last_name, reason):
    with pytest.raises(LastNameInvalidError) as e:
        LastName(last_name)

    assert e.value.reason == reason
