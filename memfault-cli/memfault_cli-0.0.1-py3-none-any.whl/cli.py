import logging
from typing import Type

import click

from memfault_cli.upload import (BugreportUploader, SymbolUploader, Uploader,
                                 upload_all)


def main():
    @click.group()
    @click.option("--email", required=True, help="Account email to authenticate with")
    @click.password_option(
        "--password",
        required=True,
        prompt=False,
        help="Account password or user API key to authenticate with",
    )
    @click.option("--org", required=True, help="Organization slug")
    @click.option("--project", required=True, help="Project slug")
    @click.pass_context
    def cli(ctx: click.Context, **kwargs):
        ctx.ensure_object(dict)
        ctx.obj.update(kwargs)

    def _do_upload_all(ctx: click.Context, path: str, uploader_cls: Type[Uploader]):
        upload_all(
            ctx.obj["org"],
            ctx.obj["project"],
            path,
            (ctx.obj["email"], ctx.obj["password"]),
            uploader_cls,
        )

    @cli.command(name="upload-bugreport")
    @click.argument("path")
    @click.pass_context
    def upload_bugreport(ctx: click.Context, path: str):
        _do_upload_all(ctx, path, BugreportUploader)

    @cli.command(name="upload-symbols")
    @click.argument("path")
    @click.pass_context
    def upload_symbols(ctx: click.Context, path: str):
        _do_upload_all(ctx, path, SymbolUploader)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    cli()


if __name__ == "__main__":
    main()
