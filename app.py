#!/usr/bin/env python3
import aws_cdk as cdk
from devops_pipeline.devops_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
    env=cdk.Environment(account="30611989741", region="eu-north-")
)

app.synth()