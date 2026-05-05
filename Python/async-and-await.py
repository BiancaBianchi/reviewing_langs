import asyncio
import httpx   # pip install httpx — versão async do requests

# Função assíncrona — retorna uma coroutine
async def buscar_usuario(id: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.exemplo.com/users/{id}")
        response.raise_for_status()
        return response.json()

# await suspende a coroutine e libera o event loop
# enquanto espera a resposta, outras coroutines podem rodar

# Executar uma coroutine
asyncio.run(buscar_usuario(1))   # ponto de entrada

# Rodar múltiplas coroutines em paralelo
async def buscar_varios():
    # ❌ sequencial — cada um espera o anterior
    u1 = await buscar_usuario(1)
    u2 = await buscar_usuario(2)
    u3 = await buscar_usuario(3)

    # ✅ paralelo — dispara os três ao mesmo tempo
    u1, u2, u3 = await asyncio.gather(
        buscar_usuario(1),
        buscar_usuario(2),
        buscar_usuario(3)
    )

# Tasks — para controle mais fino
async def processar():
    task1 = asyncio.create_task(buscar_usuario(1))
    task2 = asyncio.create_task(buscar_usuario(2))

    # faz outras coisas enquanto espera...
    await asyncio.sleep(0)   # cede controle ao event loop

    u1 = await task1
    u2 = await task2

# Timeout
async def com_timeout():
    try:
        resultado = await asyncio.wait_for(
            buscar_usuario(1),
            timeout=5.0    # segundos
        )
    except asyncio.TimeoutError:
        print("Requisição demorou mais de 5s")

# FastAPI usa async nativamente — você vai ver muito isso:
# @app.get("/usuarios/{id}")
# async def get_usuario(id: int):
#     return await buscar_usuario(id)