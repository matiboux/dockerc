from test.src.TestDirContext import TestDirContext

def test_help_docker_presets(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '@',
        )
        dockerc.assert_context_found(
            (
                b'Usage: ' + dockerc.dockerc_path.encode() + b' [options] [@preset] [...args]\n'
                b'  args: Arguments passed to docker\n'
                b'  @preset:\n'
                b'    @rfc   Remove unused containers\n'
                b'    @rfca  Remove all unused containers\n'
                b'    @rfi   Remove unused images\n'
                b'    @rfia  Remove all unused images\n'
                b'    @rf    Remove unused containers, networks and images\n'
                b'    @rfa   Remove all unused containers, networks and images\n'
                b'    @rfav  Remove all unused containers, networks, images and volumes\n'
                b'  options:\n'
                b'    -n  Dry run, print docker command without running it\n'
                b'    -q  Quiet, do not print docker command\n'
            ),
        )
