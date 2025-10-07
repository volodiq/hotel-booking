from shared.app.errors import ApplicationError


class RoomPhotosLimitExceeded(ApplicationError):
    @property
    def details(self) -> str:
        return "Максимальное количество фотографий в комнате достигнуто"
