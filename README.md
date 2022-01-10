# sls-pizza-planner
A pizza-planning webapp built using the Serverless framework to run on AWS 

See it live at https://pizza.fireblend.com/

## Running this:

#### 0. Requirements

* An AWS account.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed & setup to use your AWS account.
* [Serverless](https://serverless.com/framework/docs/providers/aws/guide/quick-start/) installed & setup.
* A Python 3.8+ environment.

#### 1. Deploying

1. Check the `serverless.yaml` file for anything you might want to modify (mainly make sure the listed Python version matches your local Python version).
2. Install the required plugins into your cloned directory: `npm install --save serverless-wsgi serverless-python-requirements`.
3. Execute `sls deploy` and wait.

That should be it! The previous command should point you to the newly deployed application's URL.
