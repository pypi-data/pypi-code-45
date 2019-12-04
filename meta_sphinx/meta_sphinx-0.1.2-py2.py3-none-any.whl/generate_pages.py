from pathlib import Path

import sphinx

from .configuration import load_conf, parse_languages
from .jinja import env
from slugify import slugify

PAGE_TEMPLATE = env.get_template("page.jinja")


INDEX_TEMPLATE = """
Libraries
=========

This is an index of all the libraries:

.. meta_sphinx_toc:: Libraries

"""


def generate_page_files(app: sphinx.application.Sphinx):
    # app.config.html_static_path.append(str(static_path()))
    pages_from_config(
        load_conf(app, *app.config.meta_sphinx_generate_stubs_from)
    )
    # page_parent_dir = Path("libraries")
    # page_parent_dir.mkdir(exist_ok=True)
    # # clean the page directory
    # for file_ in page_parent_dir.glob("*"):
    #     file_.unlink()

    # conf = parse_languages(conf)

    # (page_parent_dir / "index.rst").write_text(INDEX_TEMPLATE)

    # for item in conf:
    #     page_content = PAGE_TEMPLATE.render(item=item)

    #     (page_parent_dir / f"{item['name']}.rst").write_text(page_content)


def pages_from_config(conf):
    page_parent_dir = Path("libraries")
    page_parent_dir.mkdir(exist_ok=True)
    # clean the page directory
    for file_ in page_parent_dir.glob("*.rst"):
        file_.unlink()

    conf = parse_languages(conf)

    (page_parent_dir / "index.rst").write_text(INDEX_TEMPLATE)

    for item in conf:
        page_content = PAGE_TEMPLATE.render(item=item)

        (page_parent_dir / f"{item['name']}.rst").write_text(page_content)
