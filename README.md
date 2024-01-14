# SBHacksX
Jim Wang, Jason Wang, Vincent Cheong

# AWS CLI
To get the calls to the Amazon Comprehend API to actually work, you need to first install the AWS CLI.
If using MacOS, you can use brew to install it by running `brew install awscli`. 

I think `pip3 install awscli --upgrade --user` should also work using Python's package installer. 

Then, run `aws configure` in the command prompt/terminal. It will prompt you for an access key, secret access key, region, and output format.

The key and secret keys can be accessed through the AWS IAM (Identity Access Management) console where we created a user and generated the keys. For the region, we use "us-west-2", and for the output format, we use "text". 

Once all of this is set up, the code can make calls to the API. 
