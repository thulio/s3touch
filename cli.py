import json
import time

import click
from awscli.clidriver import create_clidriver


def validate_s3path(ctx, param, value):
    if not value.startswith('s3://'):
        raise click.BadParameter('needs to be in format s3://PATH/TO/BUCKET')

    return value


@click.command()
@click.option('--path', required=True,
              help='Path to S3 bucket (ex.: s3://PATH/TO/BUCKET', callback=validate_s3path)
def main(path):
    driver = create_clidriver()
    metadata = {'touched': str(int(time.time()))}
    args = ['s3', 'cp', '--metadata', json.dumps(metadata), '--recursive', path, path]
    driver.main(args)


if __name__ == '__main__':
    main()
