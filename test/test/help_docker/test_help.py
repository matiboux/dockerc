from test.src.TestDirContext import TestDirContext

def get_help_stdout(dockerc_path: str):
    return (
        b'Usage: ' + dockerc_path.encode() + b' [options] [@preset] [...args]\n'
        b'  args: Arguments passed to docker\n'
        b'  @preset:\n'
        b'    @rfc   Remove unused containers\n'
        b'    @rfi   Remove dangling images\n'
        b'    @rfia  Remove all unused images\n'
        b'    @rf    Remove unused containers, networks and images\n'
        b'    @rfa   Remove all unused containers, networks and images\n'
        b'    @rfav  Remove all unused containers, networks, images and volumes\n'
        b'    @sa    Stop all running containers\n'
		b'    @rmf   Remove running containers, force\n'
		b'    @rms   Remove stopped containers\n'
        b'    @rmsf  Remove stopped containers, force\n'
        b'      (aliases: @rmfs)\n'
		b'    @rma   Remove all containers\n'
		b'    @rmaf  Remove all containers, force\n'
        b'      (aliases: @rmfa)\n'
        b'  options:\n'
        b'    -f  Force, for example ignores abstract contexts\n'
        b'    -n  Dry run, print docker command without running it\n'
        b'    -q  Quiet, do not print docker command\n'
    )

def test_help_docker_presets(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '@',
        )
        dockerc.assert_context_found(
            get_help_stdout(dockerc.dockerc_path),
        )
