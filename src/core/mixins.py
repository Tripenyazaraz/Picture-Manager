class ListMixin:
    model = None
    pydantic_model = None

    async def list(self):
        queryset = await self.get_queryset()
        return await self.pydantic_model.from_queryset(queryset)

    async def get_queryset(self):
        queryset = self.model.filter()
        return queryset


class RetrieveMixin:
    model = None
    pydantic_model = None

    async def retrieve(self, id):
        instance = await self.get_object(id)
        return await self.pydantic_model.from_tortoise_orm(instance)

    async def get_object(self, id):
        instance = await self.model.get(id=id)
        return instance


class CreateMixin:
    model = None
    pydantic_model = None

    async def create(self, body: dict):
        instance = await self.perform_create(body)
        return await self.pydantic_model.from_tortoise_orm(instance)

    async def perform_create(self, body: dict):
        instance = await self.model(**body)
        await instance.save()
        return instance


class UpdateMixin:
    model = None
    pydantic_model = None

    async def update(self, id, body: dict):
        instance = await self.perform_update(id, body)
        return await self.pydantic_model.from_tortoise_orm(instance)

    async def perform_update(self, id, body: dict):
        instance = await self.model.get(id=id)
        instance.update_from_dict(body)
        return instance


class DeleteMixin:
    model = None
    pydantic_model = None

    async def delete(self, id):
        await self.perform_delete(id)
        return "deleted"

    async def perform_delete(self, id):
        instance = self.model.get(id=id)
        await instance.delete()


class ModelViewSet(ListMixin, RetrieveMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass
