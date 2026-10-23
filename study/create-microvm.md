# Your first AWS Lambda MicroVM hands-on project

I recommend building a Hello World MicroVM first. It will help you understand the technology before adding AI agents.

[Isolated sandboxes. Near-instant launch and resume. Full lifecycle control. No infrastructure to manage. - AWS Lambda MicroVMs - AWS](https://images.openai.com/static-rsc-4/pfouPglbZoy_GcspthSYkErCpAk8PoIgYupi6y1TnvmvW2pGjm_8rqr7wBiOEf6XGiYh_xdyBAwthcUpBTW9z2R5VFuSXI9Q_e8qTmfVeMU6eqNybBC_Y9qdrhf5t9nBYEZFJRWN_q7McvyOUFvaeaC7J8hJ9b7T021as-HBDk0?purpose=inline)

Project: Run a web application inside a MicroVM

Difficulty: Beginner · Tools: AWS, Docker, S3, IAM, AWS CLI

What you'll learn

Build an image → launch an isolated VM → access it over HTTPS → suspend and resume it → terminate it.

## Step 1: Prepare your AWS environment

You'll need an AWS account, AWS CLI, Docker, an S3 bucket, and an IAM role for the image build process.

Use the Mumbai Region (`ap-south-1`), which AWS added to Lambda MicroVM availability in August 2026.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aws.amazon.com\&sz=32)

AWS



Set a billing alert before you begin. MicroVMs incur compute charges while running, and there are separate charges for snapshots, storage and data transfer.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://aws.amazon.com\&sz=32)

Amazon Web Services, Inc.



## Step 2: Create a simple application

Create a directory called `lambda-microvm-demo`.

Inside it, create `app.js`:

```
const http = require("http");

const server = http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "application/json"
    });

    res.end(JSON.stringify({
        message: "Hello from AWS Lambda MicroVM!",
        path: req.url
    }));
});

server.listen(8080, () => {
    console.log("Application running on port 8080");
});
```

Next, create a `Dockerfile`:

```
FROM node:24-alpine

WORKDIR /app

COPY app.js .

EXPOSE 8080

CMD ["node", "app.js"]
```

This is a normal Node.js application packaged using Docker. The Dockerfile packages your application; AWS supplies the MicroVM isolation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.aws.amazon.com\&sz=32)

AWS Lambda



## Step 3: Package and upload your application

Create an S3 bucket in your selected Region, then upload the application files as a ZIP archive.

From a terminal in your project directory:

```
zip app.zip app.js Dockerfile

aws s3 cp app.zip s3://YOUR-BUCKET-NAME/app.zip
```

Replace `YOUR-BUCKET-NAME` with your actual bucket name.

You'll also need a build role that Lambda can assume, with permission to download the ZIP from your bucket and write build logs to CloudWatch. Follow the permissions in the official guide rather than giving the role broad administrator access.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.aws.amazon.com\&sz=32)

AWS Lambda



## Step 4: Build the MicroVM image

Use the AWS CLI command below after creating the build role:

```
aws lambda-microvms create-microvm-image \
  --name my-first-microvm-image \
  --code-artifact uri=s3://YOUR-BUCKET-NAME/app.zip \
  --base-image-arn YOUR_REGIONAL_BASE_IMAGE_ARN \
  --build-role-arn YOUR_BUILD_ROLE_ARN
```

The two `YOUR_...` values are placeholders. Use the exact base-image ARN for Mumbai and your actual IAM role ARN.

Check the build status:

```
aws lambda-microvms get-microvm-image \
  --image-identifier my-first-microvm-image
```

Wait for the image to reach the `CREATED` state. AWS starts your application during image creation and captures its initialized state for future launches.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.aws.amazon.com\&sz=32)

AWS Lambda



## Step 5: Run the MicroVM

Use the image ARN returned by the previous command. The official guide provides the required network connector configuration.

```
aws lambda-microvms run-microvm \
  --image-identifier YOUR_IMAGE_ARN \
  --ingress-network-connectors \
  "arn:aws:lambda:ap-south-1:aws:network-connector:aws-network-connector:ALL_INGRESS" \
  --egress-network-connectors \
  "arn:aws:lambda:ap-south-1:aws:network-connector:aws-network-connector:INTERNET_EGRESS" \
  --idle-policy \
  '{"autoResumeEnabled":true,"maxIdleDurationSeconds":900,"suspendedDurationSeconds":300}'
```

These settings enable inbound connectivity and outbound internet access, so use them only for your test environment and restrict network access as appropriate. All incoming requests still require an authentication token.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.aws.amazon.com\&sz=32)

AWS Lambda



The response gives you a MicroVM ID and HTTPS endpoint. Wait until the MicroVM reaches `RUNNING` before testing it.

## Step 6: Test the application

Generate a short-lived authentication token, restricted to the application's port:

```
aws lambda-microvms create-microvm-auth-token \
  --microvm-identifier YOUR_MICROVM_ID \
  --expiration-in-minutes 30 \
  --allowed-ports '[{"port":8080}]'
```

Use the returned token to call the endpoint:

```
curl https://YOUR_MICROVM_ENDPOINT/ \
  -H "X-aws-proxy-auth: YOUR_AUTH_TOKEN"
```

Expected response:

```
{
  "message": "Hello from AWS Lambda MicroVM!",
  "path": "/"
}
```

Congratulations! You've run an application inside a Lambda MicroVM. The complete process, including IAM setup and cleanup, is documented in the [official AWS getting-started tutorial](https://docs.aws.amazon.com/lambda/latest/dg/microvms-getting-started.html?utm_source=chatgpt.com).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.aws.amazon.com\&sz=32)

AWS Lambda



## Step 7: Practice the actual MicroVM lifecycle

After getting the application working, experiment with these tasks.

Practice checklist

0 of 5 completed

Launch two MicroVMs

Run two isolated instances from the same image and compare their endpoints.

Suspend and resume

Suspend an instance, resume it, and examine how its state is preserved.

Test automatic suspension

Configure an idle policy and observe the lifecycle state transitions.

Automate using Python

Use boto3 to launch an instance, retrieve its endpoint and call your application.

Add an AI agent

Build an agent that sends a simple, controlled code-execution task to the MicroVM.

Very important: When you're finished, terminate your MicroVM and clean up unused test resources. Suspended MicroVMs still incur snapshot storage charges, and MicroVM image storage has a one-week minimum retention period, so check [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/?utm_source=chatgpt.com) before creating resources.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.aws.amazon.com\&sz=32)

AWS Lambda

+1



My recommendation: complete Steps 1–6 first, without an AI model. Once you can launch a MicroVM and access its endpoint, you'll have the foundation to build an AI coding agent that executes code in an isolated environment.