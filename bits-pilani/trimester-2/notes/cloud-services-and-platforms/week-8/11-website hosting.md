# Static Website Hosting on S3

## What S3 hosting supports
- S3 can serve static HTML, CSS, JavaScript, images, and downloads.
- It cannot execute server-side code like PHP, Node, or Python.
- Website endpoint differs from REST endpoint and has website-specific behavior.

## Setup essentials
- Enable static website hosting on bucket.
- Provide index document and optional error document.
- Allow public read only when content is intentionally public, usually with Block Public Access adjusted carefully.

## Production pattern
- Use CloudFront in front of S3 for HTTPS, caching, custom domain, and better security.
- Origin Access Control can keep S3 private behind CloudFront.
- Route 53 maps friendly domain names to CloudFront distribution.
