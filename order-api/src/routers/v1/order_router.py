from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from ...services.auth.tokenAuth import AuthHandler
from ...services.order_service import OrderService
from ...schemas.order_schema import orderBody, OrderResponse

_order_service = OrderService()
router = APIRouter(tags=["Orders"])
_AuthHandler = AuthHandler()


@router.post("/order/create", response_model=list[OrderResponse], status_code=201)
async def create_order(body: orderBody, token = Depends(_AuthHandler.verify_token)):
    """cria o pedido para o usuario"""
    try:
        return _order_service.create_order(jsonable_encoder(body), token)
    except:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Falha ao Criar pedido")

@router.get("/order/get/user", response_model=list[OrderResponse])
async def get_order_user(token = Depends(_AuthHandler.verify_token)):
    """busca todas os pedidos por usuario"""
    order_get_by_user = _order_service.get_order_user(token)
    if order_get_by_user == None:
         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Pedidos do usuario não encontrado")
    return order_get_by_user

@router.get("/order/get/all-orders", response_model=list[OrderResponse])
async def get_all_orders(token = Depends(_AuthHandler.verify_token)):
    """busca todas os pedidos"""
    get_all_orders = _order_service.get_all_orders()
    if get_all_orders == None:
         raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Pedidos nao encontrados")
    return get_all_orders
     

@router.delete("/order/delete_all_order", response_model=list[OrderResponse])
async def delete_order_user(token = Depends(_AuthHandler.verify_token)):
    """Deleta todos os pedidos do usuario"""
    return _order_service.delete_all_order_user(token)

@router.delete("/order/delete_order", response_model=list[OrderResponse])
async def delete_user(id_order: int, token = Depends(_AuthHandler.verify_token)):
    """deleta o pedido pelo id"""
    return _order_service.delete_order(id_order)

@router.put("/order/delete_user", response_model=list[OrderResponse])
async def update_user(body: orderBody, id: int, token = Depends(_AuthHandler.verify_token)):
    return _order_service.update_order(jsonable_encoder(body), id)