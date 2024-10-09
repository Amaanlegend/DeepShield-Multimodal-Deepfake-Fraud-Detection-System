# main.tf

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "deepshield_bucket" {
  bucket = "deepshield-bucket"
  acl    = "private"
  
  versioning {
    enabled = true
  }
}

resource "aws_lambda_function" "deepshield_lambda" {
  filename         = "lambda_function.zip"
  function_name    = "DeepShieldLambdaFunction"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "lambda_function.lambda_handler"
  source_code_hash = filebase64sha256("lambda_function.zip")
  runtime          = "python3.8"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action    = "sts:AssumeRole",
      Effect    = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "lambda_policy" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/AWSLambdaExecute"
}

output "s3_bucket_name" {
  value = aws_s3_bucket.deepshield_bucket.bucket
}

output "lambda_function_name" {
  value = aws_lambda_function.deepshield_lambda.function_name
}
