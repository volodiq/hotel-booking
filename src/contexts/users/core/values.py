import phonenumbers

from shared.core.value_object import ValueObject

from . import errors


class PhoneNumber(ValueObject[str]):
    def validate(self):
        # TODO Добавить обновление self.value в формате E164
        if not self.value:
            raise errors.PhoneNumberEmpty()

        try:
            parsed_number = phonenumbers.parse(self.value, "RU")
        except phonenumbers.NumberParseException:
            raise errors.PhoneNumberInvalid()
        if not phonenumbers.is_possible_number(parsed_number):
            raise errors.PhoneNumberInvalid()
        if not phonenumbers.is_valid_number(parsed_number):
            raise errors.PhoneNumberInvalid()
        if not phonenumbers.is_valid_number_for_region(parsed_number, "RU"):
            raise errors.PhoneNumberUnsupportedRegion()


class FirstName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise errors.FirstNameEmpty()

        if len(self.value) > 50:
            raise errors.FirstNameTooLong()


class LastName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise errors.LastNameEmpty()

        if len(self.value) > 50:
            raise errors.LastNameTooLong()
