from fastapi import APIRouter


class ViewSetRouter(APIRouter):

    def __init__(self,
                 prefix=None,
                 view=None,
                 response_model=None,
                 tags=None,
                 dependencies=None
                 ):
        super().__init__()
        route_view = view()
        if hasattr(route_view, 'list'):
            super().add_api_route(
                response_model=response_model,
                path=f'/{prefix}/',
                endpoint=route_view.list,
                methods=['GET'],
                tags=tags,
                dependencies=dependencies
            )
        if hasattr(route_view, 'retrieve'):
            super().add_api_route(
                response_model=response_model,
                path=f'/{prefix}/' + '{id}',
                endpoint=route_view.retrieve,
                methods=['GET'],
                tags=tags
            )
        if hasattr(route_view, 'create'):
            super().add_api_route(
                response_model=response_model,
                path=f'/{prefix}/',
                endpoint=route_view.create,
                methods=['POST'],
                tags=tags
            )
        if hasattr(route_view, 'update'):
            super().add_api_route(
                response_model=response_model,
                path=f'/{prefix}/' + '{id}',
                endpoint=route_view.update,
                methods=['PUT'],
                tags=tags
            )
        if hasattr(route_view, 'delete'):
            super().add_api_route(
                response_model=response_model,
                path=f'/{prefix}/' + '{id}',
                endpoint=route_view.delete,
                methods=['DELETE'],
                tags=tags
            )
