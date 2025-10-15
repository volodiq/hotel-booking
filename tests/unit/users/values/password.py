from functools import partial

from faker import Faker
import pytest

from src.contexts.users.core.values.password import (
    Password,
    PasswordInvalidError,
    PasswordInvalidReason,
)


faker = Faker()
valid_password = partial(
    faker.password,
    length=10,
    special_chars=True,
    digits=True,
    upper_case=True,
    lower_case=True,
)


def test_password():
    password = Password(valid_password())
    assert password.value


@pytest.mark.parametrize(
    "password, reason",
    [
        ("", PasswordInvalidReason.EMPTY),
        (valid_password(length=31), PasswordInvalidReason.TOO_LONG),
        (valid_password(length=7), PasswordInvalidReason.TOO_SHORT),
        (valid_password(digits=False), PasswordInvalidReason.NOT_CONTAINS_DIGIT),
        (valid_password(upper_case=False), PasswordInvalidReason.NOT_CONTAINS_UPPERCASE),
        (valid_password(lower_case=False), PasswordInvalidReason.NOT_CONTAINS_LOWERCASE),
        (valid_password(special_chars=False), PasswordInvalidReason.NOT_CONTAINS_SPECIAL_SYMBOL),
    ],
)
def test_invalid_password(password, reason):
    with pytest.raises(PasswordInvalidError) as e:
        Password(password)

    assert e.value.reason == reason
