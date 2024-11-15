def format_dockerc_stdout(docker_command: bytes) -> bytes:
    return b'\n> ' + docker_command + b'\n\n'
