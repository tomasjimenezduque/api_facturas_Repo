"""
factura_controller.py — Controller específico para la tabla factura.

Endpoints:
- GET    /api/factura/              → Listar facturas
- GET    /api/factura/{numero}      → Obtener factura por número
- POST   /api/factura/              → Crear factura
- PUT    /api/factura/{numero}      → Actualizar factura
- DELETE /api/factura/{numero}      → Eliminar factura
"""

from fastapi import APIRouter, HTTPException, Query, Response

from models.factura import Factura
from servicios.fabrica_repositorios import crear_servicio_crud


router = APIRouter(prefix="/api/factura", tags=["Factura"])


# =========================================================================
# GET /api/factura/ — Listar todas las facturas
# =========================================================================

@router.get("/")
async def listar_facturas(
    esquema: str | None = Query(default=None),
    limite: int | None = Query(default=None)
):
    """Lista todas las facturas."""
    try:
        servicio = crear_servicio_crud()
        filas = await servicio.listar("factura", esquema, limite)

        if len(filas) == 0:
            return Response(status_code=204)

        return {
            "tabla": "factura",
            "total": len(filas),
            "datos": filas
        }

    except ValueError as ex:
        raise HTTPException(status_code=400, detail={
            "estado": 400, "mensaje": "Parámetros inválidos.", "detalle": str(ex)
        })
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "estado": 500, "mensaje": "Error interno del servidor.", "detalle": str(ex)
        })


# =========================================================================
# GET /api/factura/{numero} — Obtener factura por número
# =========================================================================

@router.get("/{numero}")
async def obtener_factura(
    numero: int,
    esquema: str | None = Query(default=None)
):
    """Obtiene una factura por su número."""
    try:
        servicio = crear_servicio_crud()
        filas = await servicio.obtener_por_clave("factura", "numero", str(numero), esquema)

        if len(filas) == 0:
            raise HTTPException(status_code=404, detail={
                "estado": 404,
                "mensaje": f"No se encontró factura con numero = {numero}"
            })

        return {
            "tabla": "factura",
            "total": len(filas),
            "datos": filas
        }

    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "estado": 500, "mensaje": "Error interno del servidor.", "detalle": str(ex)
        })


# =========================================================================
# POST /api/factura/ — Crear factura
# =========================================================================

@router.post("/")
async def crear_factura(
    factura: Factura,
    esquema: str | None = Query(default=None)
):
    """Crea una nueva factura. Valida con el modelo Pydantic."""
    try:
        datos = factura.model_dump(exclude_none=True)
        servicio = crear_servicio_crud()
        creado = await servicio.crear("factura", datos, esquema)

        if creado:
            return {
                "estado": 200,
                "mensaje": "Factura creada exitosamente.",
                "datos": datos
            }
        else:
            raise HTTPException(status_code=500, detail={
                "estado": 500, "mensaje": "No se pudo crear la factura."
            })

    except HTTPException:
        raise
    except ValueError as ex:
        raise HTTPException(status_code=400, detail={
            "estado": 400, "mensaje": "Datos inválidos.", "detalle": str(ex)
        })
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "estado": 500, "mensaje": "Error interno del servidor.", "detalle": str(ex)
        })


# =========================================================================
# PUT /api/factura/{numero} — Actualizar factura
# =========================================================================

@router.put("/{numero}")
async def actualizar_factura(
    numero: int,
    factura: Factura,
    esquema: str | None = Query(default=None)
):
    """Actualiza una factura existente."""
    try:
        datos = factura.model_dump(exclude={"numero"}, exclude_none=True)
        servicio = crear_servicio_crud()
        filas = await servicio.actualizar("factura", "numero", str(numero), datos, esquema)

        if filas > 0:
            return {
                "estado": 200,
                "mensaje": "Factura actualizada exitosamente.",
                "filtro": f"numero = {numero}",
                "filasAfectadas": filas
            }
        else:
            raise HTTPException(status_code=404, detail={
                "estado": 404,
                "mensaje": f"No existe factura con numero = {numero}"
            })

    except HTTPException:
        raise
    except ValueError as ex:
        raise HTTPException(status_code=400, detail={
            "estado": 400, "mensaje": "Datos inválidos.", "detalle": str(ex)
        })
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "estado": 500, "mensaje": "Error interno del servidor.", "detalle": str(ex)
        })


# =========================================================================
# DELETE /api/factura/{numero} — Eliminar factura
# =========================================================================

@router.delete("/{numero}")
async def eliminar_factura(
    numero: int,
    esquema: str | None = Query(default=None)
):
    """Elimina una factura por su número."""
    try:
        servicio = crear_servicio_crud()
        filas = await servicio.eliminar("factura", "numero", str(numero), esquema)

        if filas > 0:
            return {
                "estado": 200,
                "mensaje": "Factura eliminada exitosamente.",
                "filtro": f"numero = {numero}",
                "filasEliminadas": filas
            }
        else:
            raise HTTPException(status_code=404, detail={
                "estado": 404,
                "mensaje": f"No existe factura con numero = {numero}"
            })

    except HTTPException:
        raise
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            "estado": 500, "mensaje": "Error interno del servidor.", "detalle": str(ex)
        })
