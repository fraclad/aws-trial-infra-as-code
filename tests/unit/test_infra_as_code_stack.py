import aws_cdk as core
import aws_cdk.assertions as assertions

from infra_as_code.infra_as_code_stack import InfraAsCodeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in infra_as_code/infra_as_code_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InfraAsCodeStack(app, "infra-as-code")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
