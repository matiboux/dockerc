from test.src.TestDirContext import TestDirContext

def get_help_stdout(dockerc_path: str):
    return (
        b'Usage: ' + dockerc_path.encode() + b' [options] [context] [@preset] [...args]\n'
        b'  args: Arguments passed to docker compose\n'
        b'  @preset:\n'
        b'    @u     up -d\n'
        b'    @ua    up\n'
        b'    @ub    up --build -d\n'
        b'    @uba   up --build\n'
        b'    @ubf   up --build -d --force-recreate\n'
        b'    @ubfa  up --build --force-recreate\n'
        b'    @ubfp  up --build -d --force-recreate --pull always\n'
        b'    @ubfap up --build --force-recreate --pull always\n'
        b'    @ubr   up --build -d --remove-orphans\n'
        b'    @ubar  up --build --remove-orphans\n'
        b'    @ubfr  up --build -d --force-recreate --remove-orphans\n'
        b'    @ubfar up --build --force-recreate --remove-orphans\n'
        b'    @uf    up -d --force-recreate\n'
        b'    @ufa   up --force-recreate\n'
        b'    @ur    up -d --remove-orphans\n'
        b'    @uar   up --remove-orphans\n'
        b'    @ufr   up -d --force-recreate --remove-orphans\n'
        b'    @ufar  up --force-recreate --remove-orphans\n'
        b'    @d     down --remove-orphans\n'
        b'    @dr    down --remove-orphans --rmi local\n'
        b'    @dra   down --remove-orphans --rmi all\n'
        b'    @drav  down --remove-orphans --rmi all -v\n'
        b'    @r     run --rm\n'
        b'    @ri    run --rm -it\n'
        b'    @l     logs\n'
        b'    @rf    rm -f\n'
        b'    @rfv   rm -f -v\n'
        b'  context syntax: [first] | [first]-[second] | "-" | "--"\n'
        b'    first   First part of the context\n'
        b'    second  Second part of the context\n'
        b'    "-"     Use default docker compose files ("override" if it exists)\n'
        b'    "--"    Use docker compose without file arguments\n'
        b'  options:\n'
        b'    -n  Dry run, print docker compose command without running it\n'
        b'    -q  Quiet, do not print docker compose command\n'
    )

def test_help_args_presets(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@',
        )
        dockerc.assert_context_found(
            get_help_stdout(dockerc.dockerc_path),
        )
