For this project, I used the AWS S3 bucket for storing static files. If you would like to also do the same or create a new one please follow my instructions to create an S3 bucket. I wouldn't consider the AWS console to be the most user-friendly tool so follow my instructions carefully.

1. Sign in to [AWS](https://aws.amazon.com/console/).

![AWS](documentation/img/aws/sign-into-aws-console.png)

2. If you don't have an AWS account create one and add your credit card details

Be mindful of charges on your account. Use free-tier products and don't go overboard. You can check your account in the top right corner of the screen by clicking on the username you chose when creating an account. There you will see multiple options to check your account and billing information

3. Once you have successfully logged in navigate to the top left corner of the page where the AWS logo and services are located

![AWS](documentation/img/aws/aws-logo-and-services.png)

4. You'll see a search bar. Type in S3 and select the one called S3 from the list of options

![AWS](documentation/img/aws/select-s3-bucket.png)

5. You'll be brought to the main dashboard for AWS S3 and you can create a bucket here. The button to create a bucket is located on the right-hand side of the screen

![AWS](documentation/img/aws/create-s3-bucket.png)

6. Click the button and enter the information I have below and change the name of the bucket to your preferred chosen bucket name (usually made identifiable by your project name). Choose your preferred location also. To access the bucket publicly you need to allow access

![AWS](documentation/img/aws/create-bucket-1.png)

![AWS](documentation/img/aws/create-bucket-2.png)

![AWS](documentation/img/aws/create-bucket-3.png)

7. On this page, those are the only settings that need configuration so click 'create bucket' at the end of the page

![AWS](documentation/img/aws/create-bucket.png)

8. You'll be brought to your AWS S3 buckets page. Click on the bucket you just created

![AWS](documentation/img/aws/buckets.png)

9. Navigate to the properties tab of your bucket and find you should find static hosting in the list (at the time of writing it is at the bottom of the page) so click edit

![AWS](documentation/img/aws/bucket-properties.png)

![AWS](documentation/img/aws/static-web-hosting.png)

10. Enable static hosting and add in index.html and error.html (these don't matter but need a config for this project) and click save changes at the bottom of the screen

![AWS ](documentation/img/aws/edit-static-hosting.png)

11. You'll be brought back to the bucket dashboard for your bucket the next thing to do is to configure permissions. We have three tasks to do in the permissions tab

![AWS](documentation/img/aws/bucket-permissions.png)

12. We need to add a bucket policy so click edit here and then let's use the policy generator

![AWS](documentation/img/aws/edit-policy.png)

![AWS](documentation/img/aws/policy-generator.png)

13. You'll be brought to a new tab to create your policy.

- The type of policy is the S3 Bucket policy
- The principal is a * symbol so we can access everything in our bucket
- We only need to perform one action and its 'GetObject' the mp4 recorder requires all permissions
- The ARN can be found on the previous tab at the top of the page
- Click add statement
- Then click Generate Policy
- We have no special conditions to add to this project

![AWS](documentation/img/aws/policy-1.png)

![AWS](documentation/img/aws/policy-2.png)

- Copy the policy generated using Ctrl + a and Ctrl + c or using your mouse

![AWS](documentation/img/aws/policy-3.png)

14. Switch tabs back to your edit bucket policy page and paste the generated policy into the text editor area. We want to use all the resources in the bucket so we're not finished yet here.

In the policy you can see a key for "Resource" and at the end of the value add /* so we can access all items inside the bucket then click save changes at the bottom of the screen

![AWS](documentation/img/aws/policy-config.png)

15. The second task we need to complete here in the permissions tab of the bucket is configuring the Access control list. It allows users to access the bucket. Click edit

![AWS](documentation/img/aws/access-control-list.png)

- You only need to change one setting here for Everyone to have public access and you only want to change the list

![AWS](documentation/img/aws/access-control-1.png)

- Accept that you understand these changes for granting access and click save changes

![AWS](documentation/img/aws/access-control-2.png)

16. The last step for the S3 bucket is to go to the very end of this tab section under permissions and add a CORS configuration. Click edit and paste the following code block

![AWS](documentation/img/aws/cors.png)

    [

    {

    "AllowedHeaders": [

    "Authorization"

    ],

    "AllowedMethods": [

    "GET"

    ],

    "AllowedOrigins": [

    "*"

    ],

    "ExposeHeaders": []

    }

    ]

17. We've finished everything we need to do inside our bucket the next thing we need to do is configure our identity and access management settings for accessing our AWS resources. In the search bar enter IAM and select the first option called IAM

![AWS](documentation/img/aws/iam.png)

18. Click on User groups and create a new user group

![AWS](documentation/img/aws/user-groups.png)

![AWS](documentation/img/aws/create-group.png)

![AWS](documentation/img/aws/create-group-1.png)

- You don't need to do anything yet so just click create a group at the end of the page after you create a name for your user group

19. You'll be brought to the dashboard for your user groups, click on the user group you created

and navigate to permissions

![AWS](documentation/img/aws/group-permissions-1.png)

- Click on add permissions and click attach policies

![AWS](documentation/img/aws/group-permissions-2.png)

- You will be brought to another page to create your policy, navigate to the JSON tab

![AWS](documentation/img/aws/group-permissions-3.png)

- Click on the import-managed policy

![AWS](documentation/img/aws/group-permissions-4.png)

- Type in S3 and select the option for full access, when you return the JSON text will have changed

![AWS](documentation/img/aws/group-permissions-5.png)

- Remove the value for the Resource key and replace it with your ARN for your S3 Bucket.

Open a separate tab and navigate to the S3 dashboard and then to your bucket and get the ARN as we did in a previous step. create an array for the Resource key and paste in your ARN twice but for the second value in the array put a /* at the end so we can access the bucket and the contents of the bucket.

![AWS](documentation/img/aws/group-permissions-6.png)

![AWS](documentation/img/aws/group-permissions-7.png)

- When completed click next and next again skipping the tag section as it's irrelevant to this project and add a name and description for the policy you created

![AWS](documentation/img/aws/group-permissions-8.png)

20. Navigate back to user groups and click on your group go to the permissions tab and let's attach the policy we created

![AWS](documentation/img/aws/group-permissions-9.png)

21. The last thing we need to do to complete our setup and access our S3 bucket is to create a user for our user group so they can use the permissions we created

- Navigate to the user sections of our IAM

![AWS](documentation/img/aws/user-permissions-1.png)

- Click on add a user.

![AWS](documentation/img/aws/user-permissions-2.png)

- Create a user for our user group and allow programmatic access so we can use it in our Django project, click next and skip the tag section and click on create user

![AWS](documentation/img/aws/user-permissions-3.png)

22. We have now completed our set-up for our S3 bucket and we need to download the .csv file for our access key and secret access key. You can also copy those from here to put in your project

![AWS](documentation/img/aws/user-permissions-4.png)

23. As a final mention, you must install boto3 and django-storages to use your S3 bucket with Python. Example below.

- In the settings.py file of your project directory paste this and also change the bucket name and region that you chose for your S3 bucket

  # static file config heroku

  # Cache control

  AWS_S3_OBJECT_PARAMETERS = {

  'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',

  'CacheControl': 'max-age=94608000',

  }

  # Bucket Config

  AWS_STORAGE_BUCKET_NAME = 'fine-chop2'

  AWS_S3_REGION_NAME = 'eu-west-1'

  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')

  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

  # Static and media files

  STATICFILES_STORAGE = 'custom_storages.StaticStorage'

  STATICFILES_LOCATION = 'static'

  DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

  MEDIAFILES_LOCATION = 'media'
- You will also need to configure Django to use your S3 bucket so create a file as below and place it in the main project directory

![AWS](documentation/img/aws//custom-storage.png)
