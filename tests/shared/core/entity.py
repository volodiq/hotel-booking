from dataclasses import dataclass

from faker import Faker

from seedwork.entity import Entity


@dataclass(eq=False, frozen=True)
class SomeEntity(Entity):
    text: str


def test_entity_success(faker: Faker):
    text = faker.text()
    entity = SomeEntity(text=text)
    assert entity.text == text
    assert entity == entity
    assert entity.oid
    assert entity.created_at

    entity_changed = SomeEntity(oid=entity.oid, text=faker.text())
    assert entity == entity_changed

    entity2 = SomeEntity(text=entity.text)
    assert entity != entity2
