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
        b'    @d     down\n'
        b'    @da    down --remove-orphans\n'
        b'    @dr    down --remove-orphans --rmi local\n'
        b'    @dra   down --remove-orphans --rmi all\n'
        b'    @drav  down --remove-orphans --rmi all -v\n'
        b'    @drv   down --remove-orphans -v\n'
        b'    @r     run --rm\n'
        b'    @rw    run -w /pwd -v $(pwd):/pwd --rm\n'
        b'    @rd    run -d\n'
        b'    @rk    run\n'
        b'    @rb    run --build --rm\n'
        b'    @rbw   run --build -w /pwd -v $(pwd):/pwd --rm\n'
        b'    @rbd   run --build -d\n'
        b'    @rbk   run --build\n'
        b'    @ri    run -i --rm\n'
        b'    @rwi   run -w /pwd -v $(pwd):/pwd -i --rm\n'
        b'    @rki   run -i\n'
        b'    @rbi   run --build -i --rm\n'
        b'    @rbwi  run --build -w /pwd -v $(pwd):/pwd -i --rm\n'
        b'    @rbki  run --build -i\n'
        b'    @sh    run -i --rm --entrypoint /bin/sh\n'
        b'    @shw   run -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/sh\n'
        b'    @$     run -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/sh\n'
        b'    $      run -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/sh\n'
        b'    @shb   run --build -i --rm --entrypoint /bin/sh\n'
        b'    @shbw  run --build -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/sh\n'
        b'    @bash  run -i --rm --entrypoint /bin/bash\n'
        b'    @bashw run -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/bash\n'
        b'    @bashb run --build -i --rm --entrypoint /bin/bash\n'
        b'    @bashbw run --build -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/bash\n'
        b'    @l     logs -n 100\n'
        b'    @lf    logs -n 100 -f\n'
        b'    @lt    logs -n 100 -t\n'
        b'    @ls    logs -n 100 --no-log-prefix\n'
        b'    @lft   logs -n 100 -f -t\n'
        b'    @lfs   logs -n 100 -f --no-log-prefix\n'
        b'    @lfts  logs -n 100 -f -t --no-log-prefix\n'
        b'    @lts   logs -n 100 -t --no-log-prefix\n'
        b'    @ll    logs\n'
        b'    @llf   logs -f\n'
        b'    @llt   logs -t\n'
        b'    @lls   logs --no-log-prefix\n'
        b'    @llft  logs -f -t\n'
        b'    @llfs  logs -f --no-log-prefix\n'
        b'    @llfts logs -f -t --no-log-prefix\n'
        b'    @llts  logs -t --no-log-prefix\n'
        b'    @pl    pull\n'
        b'    @rs    rm --stop\n'
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
