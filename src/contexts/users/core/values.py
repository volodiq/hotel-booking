from system.seedwork.value_object import ValueObject

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
