import email_validator
import phonenumbers

from kernel.seedwork.value_object import ValueObject

from . import errors


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


class MiddleName(ValueObject[str | None]):
    def validate(self):
        if self.value is None:
            return

        if len(self.value) > 50:
            raise errors.MiddleNameTooLong()


class PhoneNumber(ValueObject[str]):
    def validate(self):
        if not self._value:
            raise errors.PhoneNumberEmpty()

        try:
            parsed_number = phonenumbers.parse(self._value, "RU")
        except phonenumbers.NumberParseException:
            raise errors.PhoneNumberInvalid()
        if not phonenumbers.is_possible_number(parsed_number):
            raise errors.PhoneNumberInvalid()
        if not phonenumbers.is_valid_number(parsed_number):
            raise errors.PhoneNumberInvalid()
        if not phonenumbers.is_valid_number_for_region(parsed_number, "RU"):
            raise errors.PhoneNumberUnsupportedRegion()

    @property
    def value(self):
        """
        Возвращает номер телефона в формате E164
        """

        parsed_number = phonenumbers.parse(self._value, "RU")
        return phonenumbers.format_number(
            parsed_number,
            phonenumbers.PhoneNumberFormat.E164,
        )


class Email(ValueObject[str]):
    def validate(self):
        if not self._value:
            raise errors.EmailEmpty()
        try:
            normalized_email = email_validator.validate_email(self._value)
        except email_validator.EmailNotValidError:
            raise errors.EmailInvalid()

        if normalized_email.domain not in ["yandex.ru", "mail.ru", "gmail.com"]:
            raise errors.EmailUnsupportedDomain()

    @property
    def value(self):
        return email_validator.validate_email(self._value).normalized
