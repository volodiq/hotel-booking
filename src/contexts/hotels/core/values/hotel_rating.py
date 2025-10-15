from dataclasses import dataclass
from enum import StrEnum

from shared.core.errors import ApplicationError
from shared.core.value_object import ValueObject


class HotelRatingInvalidReason(StrEnum):
    TOO_SMALL = "hotel_rating.too_small"
    TOO_BIG = "hotel_rating.too_big"


HOTEL_RATING_INVALID_REASON_DESCRIPTIONS = {
    HotelRatingInvalidReason.TOO_SMALL: "Рейтинг отеля не может быть меньше 1",
    HotelRatingInvalidReason.TOO_BIG: "Рейтинг отеля не может быть больше 5",
}


@dataclass
class HotelRatingInvalidError(ApplicationError):
    reason: HotelRatingInvalidReason

    @property
    def details(self) -> str:
        return HOTEL_RATING_INVALID_REASON_DESCRIPTIONS[self.reason]


class HotelRating(ValueObject[int]):
    def validate(self):
        if self.value < 1:
            raise HotelRatingInvalidError(HotelRatingInvalidReason.TOO_SMALL)
        elif self.value > 5:
            raise HotelRatingInvalidError(HotelRatingInvalidReason.TOO_BIG)
