import phonenumbers

from contexts.users.domain import exceptions as exc
from core.domain.value import ValueObject


class PhoneNumber(ValueObject[str]):
    def validate(self):
        # TODO Добавить обновление self.value в формате E164
        if not self.value:
            raise exc.PhoneNumberEmpty()

        try:
            parsed_number = phonenumbers.parse(self.value, "RU")
        except phonenumbers.NumberParseException:
            raise exc.PhoneNumberInvalid()
        if not phonenumbers.is_possible_number(parsed_number):
            raise exc.PhoneNumberInvalid()
        if not phonenumbers.is_valid_number(parsed_number):
            raise exc.PhoneNumberInvalid()
        if not phonenumbers.is_valid_number_for_region(parsed_number, "RU"):
            raise exc.PhoneNumberUnsupportedRegion()


class FirstName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise exc.FirstNameEmpty()

        if len(self.value) > 50:
            raise exc.FirstNameTooLong()


class LastName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise exc.LastNameEmpty()

        if len(self.value) > 50:
            raise exc.LastNameTooLong()
