from dataclasses import dataclass
import uuid

import magic
from types_aiobotocore_s3.client import S3Client

from ..core.interfaces import PhotoStorage


@dataclass
class S3PhotoStorage(PhotoStorage):
    endpoint_url: str
    access_key: str
    secret_key: str

    bucket_name: str
    bucket_url: str

    session: S3Client

    def get_file_name(self, photo_as_bytes: bytes) -> str:
        _, file_ext = magic.from_buffer(photo_as_bytes, mime=True).split("/")
        return f"{str(uuid.uuid4())}.{file_ext}"

    async def upload(self, photo_as_bytes: bytes) -> str:
        filename = self.get_file_name(photo_as_bytes)
        await self.session.put_object(
            Bucket=self.bucket_name,
            Key=filename,
            Body=photo_as_bytes,
        )
        return f"{self.bucket_url}/{filename}"


class MockPhotoStorage(PhotoStorage):
    async def upload(self, photo_as_bytes: bytes) -> str:
        return "http://mock.url"
