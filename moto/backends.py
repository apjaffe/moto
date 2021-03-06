from __future__ import unicode_literals
from moto.autoscaling import autoscaling_backend
from moto.cloudwatch import cloudwatch_backend
from moto.dynamodb import dynamodb_backend
from moto.dynamodb2 import dynamodb_backend2
from moto.ec2 import ec2_backend
from moto.elb import elb_backend
from moto.emr import emr_backend
from moto.glacier import glacier_backend
from moto.kinesis import kinesis_backend
from moto.kms import kms_backend
from moto.rds import rds_backend
from moto.redshift import redshift_backend
from moto.s3 import s3_backend
from moto.s3bucket_path import s3bucket_path_backend
from moto.ses import ses_backend
from moto.sqs import sqs_backend
from moto.sts import sts_backend
from moto.route53 import route53_backend

BACKENDS = {
    'autoscaling': autoscaling_backend,
    'cloudwatch': cloudwatch_backend,
    'dynamodb': dynamodb_backend,
    'dynamodb2': dynamodb_backend2,
    'ec2': ec2_backend,
    'elb': elb_backend,
    'emr': emr_backend,
    'glacier': glacier_backend,
    'kinesis': kinesis_backend,
    'kms': kms_backend,
    'redshift': redshift_backend,
    'rds': rds_backend,
    's3': s3_backend,
    's3bucket_path': s3bucket_path_backend,
    'ses': ses_backend,
    'sqs': sqs_backend,
    'sts': sts_backend,
    'route53': route53_backend
}


def get_model(name):
    for backend in BACKENDS.values():
        models = getattr(backend.__class__, '__models__', {})
        if name in models:
            return list(getattr(backend, models[name])())
