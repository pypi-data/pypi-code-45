import click
import pkg_resources
from mdk.utils import DockerCommand

VERSION = pkg_resources.require("mdk")[0].version


def mdk(*args, **kwargs):
    @click.group()
    @click.version_option(version=VERSION)
    @click.pass_context
    def cli(ctx, prog_name="mdk"):
        ctx.obj = DockerCommand()

    pass_docker = click.make_pass_decorator(DockerCommand)

    @cli.command(name="bash")
    @pass_docker
    def mdk_bash(docker):
        docker.exec(["bash"])

    @cli.command(name="down")
    @pass_docker
    def mdk_down(docker):
        docker.down()

    @cli.command(name="lsc")
    @click.option("-v", "--verbose", is_flag=True)
    @pass_docker
    def mdk_lsc(docker, verbose):
        cmd = ["ps", "-a"]
        if not verbose:
            cmd.extend([
                "--format",
                "table {{.Names}}\t{{.Image}}\t{{.Status}}"])
        docker(cmd)

    @cli.command(name="lsi")
    @click.option("-v", "--verbose", is_flag=True)
    @pass_docker
    def mdk_lsi(docker, verbose):
        cmd = ["images"]
        if not verbose:
            cmd.extend([
                "--format",
                "table {{.ID}}\t{{.Tag}}\t{{.Size}}"])
        docker(cmd)

    @cli.command(name="lsv")
    @pass_docker
    def mdk_lsv(docker):
        docker(["volume", "ls"])

    @cli.command(name="pause")
    @pass_docker
    def mdk_pause(docker):
        docker.container_cmd("pause")

    @cli.command(name="run")
    @click.argument("command", nargs=-1, type=click.STRING)
    @click.option("-interactive", "-it", default=True, is_flag=True)
    @pass_docker
    def mdk_run(docker, command, interactive):
        docker.run(list(command), interactive)

    @cli.command(name="sh")
    @pass_docker
    def mdk_sh(docker):
        docker.exec(["sh"])

    @cli.command(name="start")
    @pass_docker
    def mdk_start(docker):
        docker.container_cmd("start")

    @cli.command(name="stop")
    @pass_docker
    def mdk_stop(docker):
        docker.container_cmd("stop")

    @cli.command(name="status")
    @pass_docker
    def mdk_status(docker):
        docker.status()

    @cli.command(name="unpause")
    @pass_docker
    def mdk_unpause(docker):
        docker.container_cmd("unpause")

    @cli.command(name="up")
    @pass_docker
    def mdk_up(docker):
        docker.up()

    @cli.command(name="zsh")
    @pass_docker
    def mdk_zsh(docker):
        docker.exec(["zsh"])

    cli(*args, **kwargs)
