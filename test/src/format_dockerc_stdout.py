def format_dockerc_stdout(docker_comand: bytes) -> bytes:
    return b'\n> ' + docker_comand + b'\n\n'
