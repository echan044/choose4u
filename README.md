# Choose4u

Prototype Caloric Count - Most backend work complete

Done with [Python] - AWS: Rekognition, Lambda, CloudFormation

#####################################################################################

Run Rekognition with command: 

```python
aws rekognition detect-labels ^
  --image "{\"S3Object\":{\"Bucket\":\"[BUCKET-NAME]\",\"Name\":\"[IMAGE-NAME]\"}}" ^
  --region [REGION-OF-BUCKET]
```
for example:

```python
aws rekognition detect-labels ^
  --image "{\"S3Object\":{\"Bucket\":\"ucrfoodbucket3\",\"Name\":\"taco.jpg\"}}" ^
  --region us-west-2
```

#####################################################################################


or for Windows/Linux command:

```python
aws rekognition detect-labels --image "S3Object={Bucket=[BUCKET-NAME],Name=[IMAGE-NAME]}" --[REGION OF BUCKET]
```

for example:

```python
aws rekognition detect-labels --image "S3Object={Bucket=ucrfoodbucket3,Name=taco.jpg}" --us-west-2
```
