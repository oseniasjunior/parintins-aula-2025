#!/usr/bin/env python
import sys
import asyncio
from datetime import datetime
import telnetlib3


async def _try_connect(server: str, port: int, connect_timeout: float = 1.0) -> bool:
    """
    Tenta abrir uma conexão Telnet usando telnetlib3 com um timeout curto.
    Retorna True se conectou, False em caso de erro/timeout.
    """
    try:
        # Usa asyncio.wait_for para limitar o tempo da tentativa de conexão
        reader, writer = await asyncio.wait_for(
            telnetlib3.open_connection(host=server, port=port),
            timeout=connect_timeout,
        )
        # Conectou — fecha imediatamente
        writer.close()
        # Aguarda fechamento do transporte (ignora erro se não suportado)
        try:
            await writer.wait_closed()
        except AttributeError:
            pass
        return True
    except Exception:
        return False


def wait_net_service(server, port, timeout=1):
    """
    Wait for network service to appear
    @return: True or False; if timeout is None or 0, waits forever
    :type timeout: seconds
    :param port: port
    :param server: server address
    """
    first = datetime.now()

    # Constrói um loop de tentativas assíncronas até conectar ou estourar timeout
    async def _runner():
        while True:
            diff = (datetime.now() - first).total_seconds()

            # Se timeout é 0 ou None, espera indefinidamente
            if timeout and timeout > 0 and diff >= timeout:
                return False

            ok = await _try_connect(server, port, connect_timeout=1.0)
            if ok:
                print("Connected after {} seconds".format(diff))
                return True

            # Pequena espera antes da próxima tentativa
            await asyncio.sleep(1.0)

    return asyncio.run(_runner())


if __name__ == '__main__':
    server = sys.argv[1]
    port = int(sys.argv[2])
    # suporta passar None? Na prática vem string; tratamos "0" como 0 (espera infinita), qualquer valor positivo como timeout.
    timeout = int(sys.argv[3])
    wait_net_service(server, port, timeout)
