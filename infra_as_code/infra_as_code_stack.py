from aws_cdk import Stack, aws_lambda, aws_apigateway
from constructs import Construct

class InfraAsCodeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        
        random_drink_function = aws_lambda.Function(
            self, # the scope
            "random_drink_function_v1", # just give this a name
            code = aws_lambda.Code.from_asset("./compute/"), # specify where to look
            handler = "random_drink.lambda_handler", # refer to the 1. package and then 2. the lambda handler to run when triggered
            runtime = aws_lambda.Runtime.PYTHON_3_8) # specify which runtime to use, just use python. 
        
        api = aws_apigateway.RestApi(
            self,
            "random_drink_api",
            rest_api_name="random drink api test cdk",
            description="clearly im testing things out here"
        )
        
        random_drink_integration = aws_apigateway.LambdaIntegration(handler=random_drink_function)
        api_resource = api.root.add_resource("my_random_drink")
        api_resource.add_method("GET", random_drink_integration)