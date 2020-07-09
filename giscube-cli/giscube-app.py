#! /data/uwsgi/giscube-app-venv/bin/python3

from pathlib import Path
import shutil

import click


@click.group()
@click.pass_context
def giscube(ctx):
    pass


@giscube.command()
@click.option('--deploy-user', default='www-data',
              help='user used to deploy the code')
@click.option('--app-folder', default='',
              help='folder in src directory that contains the app')
@click.argument('path', default='.', required=False)
@click.pass_context
def init(ctx, path, app_folder, deploy_user):
    """Init app structure"""
    modified = False
    path = Path(path).resolve()
    click.echo('path: %s' % path)
    modified |= create_dirs(path, deploy_user)
    modified |= create_app_link(path, app_folder)
    copy_files(path)

    if modified:
        ctx.exit(1)


def create_dirs(path, deploy_user):
    modified = False
    modified |= create_dir(path, 'root', 'root')
    modified |= create_dir(path / 'static', 'www-data', 'www-data')
    modified |= create_dir(path / 'src', deploy_user, 'www-data')
    return modified


def create_dir(path, user, group):
    modified = False
    if path.is_dir():
        click.echo('[ok] dir %s' % path)
    else:
        click.echo('create dir %s' % path)
        path.mkdir(mode=0o775, exist_ok=True)
        modified = True

    if path.owner() != user and path.group() != group:
        click.echo('fix user and group')
        shutil.chown(path, user=user, group=group)
        modified = True

    return modified


def create_app_link(path, app_folder):
    modified = False
    app = path / 'app'
    app_target = path.resolve() / 'src' / app_folder

    if app.is_symlink():
        if str(app.resolve()) != str(app_target.resolve()):
            click.echo('remove previous app link %s' % app)
            app.unlink()

    if app.exists():
        click.echo('[ok] app link present %s -> %s' % (app, app_target))
    else:
        click.echo('create app link to %s' % app_target)
        app.symlink_to(app_target.relative_to(path), target_is_directory=True)
        modified = True

    return modified


def copy_files(path):
    template = Path(__file__).resolve().parent.absolute() / 'template'
    for template_file in template.iterdir():
        click.echo('copy %s to %s' % (template_file, path/template_file.name))
        shutil.copy(template_file, path)


if __name__ == '__main__':
    giscube()
