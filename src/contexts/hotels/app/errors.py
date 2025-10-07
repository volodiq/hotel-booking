from shared.app.errors import ApplicationError


class ActionForbidden(ApplicationError):
    @property
    def details(self) -> str:
        return "Вы не можете выполнить это действие"


class HotelNotFound(ApplicationError):
    @property
    def details(self) -> str:
        return "Отель не найден"


class RoomNotFound(ApplicationError):
    @property
    def details(self) -> str:
        return "Комната не найдена"


class RoomPhotosLimitExceeded(ApplicationError):
    @property
    def details(self) -> str:
        return "Максимальное количество фотографий в комнате достигнуто"
