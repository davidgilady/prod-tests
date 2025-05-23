#!/usr/bin/env python3
import os

import aws_cdk as cdk

from s3_config.s3_config_stack import S3ConfigStack

print ('hello')
print(os.path.expandvars(os.environ['CDK_CONFIG_FILE']))

cfg_path = os.environ['CONFIG_REPO_PATH']
with open(os.path.join(cfg_path, 'config'), 'r') as config:
    bucket_name=config.readline().rstrip('\n')
app = cdk.App()
S3ConfigStack(app, "S3ConfigStack", bucket_name=bucket_name,
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
