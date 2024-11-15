from test.src.TestDirContext import TestDirContext

def get_help_stdout(dockerc_path: str):
    return (
        b'Usage: ' + dockerc_path.encode() + b' [options] [context] [...args]\n'
        b'  args: Arguments passed to docker compose\n'
        b'  context syntax: [first] | [first]-[second] | "-" | "--"\n'
        b'    first   First part of the context\n'
        b'    second  Second part of the context\n'
        b'    "-"     Use default docker compose files ("override" if it exists)\n'
        b'    "--"    Use docker compose without file arguments\n'
        b'  options:\n'
        b'    -h, --help     Print this help and exit\n'
        b'    -v, --version  Print version and exit\n'
        b'    --update       Update DockerC and exit\n'
        b'    -f             Force, for example ignores abstract contexts\n'
        b'    -n             Dry run, print docker compose command without running it\n'
        b'    -q             Quiet, do not print docker compose command\n'
    )

def test_help(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--help',
        )
        dockerc.assert_context_ok(
            get_help_stdout(dockerc.dockerc_path),
        )

def test_help_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-h',
        )
        dockerc.assert_context_ok(
            get_help_stdout(dockerc.dockerc_path),
        )
