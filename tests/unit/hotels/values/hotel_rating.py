from faker import Faker
import pytest

from contexts.hotels.app.values.hotel_rating import (
    HotelRating,
    HotelRatingInvalidError,
    HotelRatingInvalidReason,
)


faker = Faker()


def test_hotel_rating():
    rating = HotelRating(faker.random_int(min=1, max=5))
    assert rating.value


@pytest.mark.parametrize(
    "rating, reason",
    [
        (faker.random_int(max=0), HotelRatingInvalidReason.TOO_SMALL),
        (faker.random_int(min=6), HotelRatingInvalidReason.TOO_BIG),
    ],
)
def test_hotel_rating_invalid(rating, reason):
    with pytest.raises(HotelRatingInvalidError) as e:
        HotelRating(rating)

    assert e.value.reason == reason
