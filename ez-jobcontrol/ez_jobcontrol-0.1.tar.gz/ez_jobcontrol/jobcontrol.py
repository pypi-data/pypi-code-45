import os,sys,boto3,logging
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class jobcontrol:    
    def __init__(self,job_control_table='ez_job_control',job_status_table='ez_job_status',job_dependency_table='ez_job_dependency',aws_region,profile_name=''):
        self.aws_region=aws_region
        self.job_control_table=job_control_table
        self.job_status_table=job_status_table
        self.job_dependency_table=job_dependency_table
        self.profile_name=profile_name
        self.logger=logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        
    def getsession(self):
        if self.profile_name == '':
            session = boto3.Session()
        else:
            session = boto3.Session(profile_name=self.profile_name)
        return session

    def getclient(self):
        dynamo=self.getsession().client('dynamodb',aws_region)
        return dynamo
    
    def gettable(self,table):
        table = self.getsession().resource('dynamodb',aws_region).Table(table)
        return table
    
    def checkifjobisrunning(self,job_id):
        dynamo=self.getclient()
        response_job_status=dynamo.query(TableName=self.job_status_table,
                KeyConditions=
                {
                    "job_id":{
                        "AttributeValueList":[{"S":job_id}],
                        'ComparisonOperator': 'EQ'
                        }
                },
                QueryFilter=
                {
                    "status":{
                        "AttributeValueList":[{"S":"Running"}],
                        'ComparisonOperator': 'EQ'
                        }                
                })
        if response_job_status['Count'] != 0:
            self.logger.error("There is an instance of the job already running, please cleanup and rerun")
            raise RuntimeError("There is an instance of the job already running, please cleanup and rerun")

    def getdatadate(self,job_id):
        dynamo=self.getclient()
        response_job_status=dynamo.query(TableName=self.job_status_table,
                KeyConditions=
                {
                    "job_id":{
                        "AttributeValueList":[{"S":job_id}],
                        'ComparisonOperator': 'EQ'
                        }
                },
                QueryFilter=
                {
                    "status":{
                        "AttributeValueList":[{"S":"Running"}],
                        'ComparisonOperator': 'EQ'
                        }                
                })
        data_date=response_job_status['Items'][0]['data_date']['S']
        self.logger.error("Data date for current run is : {}".format(data_date))
        return data_date

    def validatejobid(self,job_id):
        dynamo=self.getclient()
        self.logger.info("Checking if dynamoDB entry exists for the given job id:{0}".format(job_id))
        response_job_control=dynamo.query(TableName=self.job_control_table,KeyConditions=
                {
                "job_id":{
                        "AttributeValueList":[{"S":job_id}],
                        'ComparisonOperator': 'EQ'
                        }
                })
        if len(response_job_control["Items"]) != 1:
            self.logger.error("Please check dynamoDB for job_id {0}, only 1 row should exist".format(job_id))
            raise RuntimeError("Please check dynamoDB for job_id {0}, only 1 row should exist".format(job_id))
        if response_job_control["Items"][0]["enabled"]["S"] != "True":
            self.logger.error("Job ID : {0} is not enabled in dynamodb, please check".format(job_id))
            raise RuntimeError("Job ID : {0} is not enabled in dynamodb, please check".format(job_id))
        else:
            self.logger.info("All good")
        return response_job_control

    def sendalerts(self,job_id,emails,slack):
        self.logger.info("Sending alerts(not yet implemented) for job_id {0} to emails: {1} and slack:{2}".format(job_id,emails,slack))
    
    def jc_start(self,job_id):
        self.logger.info("Validating job_id : {0}".format(job_id))
        response=self.validatejobid(job_id)
        if response["Items"][0]["alert_enabled"]["S"] == "True":
            self.logger.info("Alerts are enabled for this job, will send alerts")
            emails=response["Items"][0]["email"]["S"]+','+response["Items"][0]["group_email"]["S"]
            slack=response["Items"][0]["slack_channel"]["S"]
            self.sendalerts(job_id,emails,slack)
        frequeny=response["Items"][0]["frequency"]["S"]
        self.logger.info("Checking if job_id : {0} is already running".format(job_id))
        self.checkifjobisrunning(job_id)
        dynamo=self.getclient()
        response_job_status=dynamo.query(TableName=self.job_status_table,
                KeyConditions=
                {
                    "job_id":{
                        "AttributeValueList":[{"S":job_id}],
                        'ComparisonOperator': 'EQ'
                        }
                },
                QueryFilter=
                {
                    "status":{
                        "AttributeValueList":[{"S":"Completed"}],
                        'ComparisonOperator': 'EQ'
                        }                
                }
                )
        job_run_list=response_job_status['Items']
        new_job_run_id=None
        new_data_date=None
        if len(job_run_list) == 0:
            self.logger.info("This is the first run of the job, setting job_run_id=1")
            new_job_run_id=1
            new_data_date=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
        else:
            seq = [int(item['job_run_id']["N"]) for item in job_run_list]
            max_job_run_id=max(seq)
            new_job_run_id=max_job_run_id+1
            seq2 = [item['data_date']["S"] for item in job_run_list]
            max_data_date=max(seq2)
            if frequeny == 'Monthly':
                new_data_date=str(datetime.strptime(max_data_date,'%Y-%m-%d').date() + relativedelta(months=1))
            elif frequeny == 'Daily':
                new_data_date=str(datetime.strptime(max_data_date,'%Y-%m-%d').date() + relativedelta(days=1))
        
        start_ts=str(datetime.now()).split(".")[0]
        item={
            "job_id":{"S":job_id}
            ,"job_run_id":{"N":str(new_job_run_id)}
            ,"data_date":{"S":new_data_date}
            ,"status":{"S":"Running"}
            ,"start_ts":{"S":start_ts}
            }
        try:
            dynamo.put_item(TableName=self.job_status_table, Item=item)
        except Exception as e:
            self.logger.info("Unable to put item into dynamodb table {0},pleae check".format(self.job_control_table))
            self.logger.info(e)
            raise RuntimeError("Unable to put item into dynamodb table {0},pleae check, error {1}".format(self.job_control_table,e))
        
    def jc_end(self,job_id):
        dynamo=self.getclient()
        self.logger.info("Retrieving status of job with job_id : {0}".format(job_id))
        response_job_status=dynamo.query(TableName=self.job_status_table,
            KeyConditions=
            {
                "job_id":{
                    "AttributeValueList":[{"S":job_id}],
                    'ComparisonOperator': 'EQ'
                    }
            },
            QueryFilter=
            {
                "status":{
                    "AttributeValueList":[{"S":"Running"}],
                    'ComparisonOperator': 'EQ'
                    }                
            }
            )
        job_run_list=response_job_status['Items']
        if len(job_run_list) == 0:
            self.logger.info("There is no entry in {0} with job_id : {1} in Running status, pleae check".format(self.job_status_table,job_id))
            raise RuntimeError("There is no entry in {0} with job_id : {1} in Running status, pleae check".format(self.job_status_table,job_id))
        seq = [item['job_run_id']["N"] for item in job_run_list]
        max_job_run_id=max(seq)
        end_ts=str(datetime.now()).split(".")[0]
        table=self.gettable(self.job_status_table)
        self.logger.info("Updating {0} with status as completed for job_run_id {1} for job_id : {2}".format(self.job_status_table,max_job_run_id,job_id))
        try:
            table.update_item(
                Key={
                    'job_id': job_id,
                    'job_run_id' : int(max_job_run_id)
                },
                ExpressionAttributeNames={"#status":"status","#comment":"comment"},
                UpdateExpression='SET #status=:val1,end_ts=:val2,#comment=:val3',
                ExpressionAttributeValues={
                    ':val1': 'Completed',
                    ':val2': end_ts,
                    ':val3': 'Success'
                }
            )
        except Exception as e:
            self.logger.info("Unable to update, pleaes check")
            self.logger.info(e)
            raise RuntimeError("Unable to update job_status table, pleaes check, error {}".format(e))
        self.logger.info("Updated Successfully")

    def validatedependency(self,job_id):
        dependency_flag=True
        dynamo=self.getclient()
        print("Fetching data date of curretn run")
        response=dynamo.query(TableName=self.job_status_table,
                KeyConditions=
                {
                    "job_id":{
                        "AttributeValueList":[{"S":job_id}],
                        'ComparisonOperator': 'EQ'
                        }
                },
                QueryFilter=
                {
                    "status":{
                        "AttributeValueList":[{"S":"Running"}],
                        'ComparisonOperator': 'EQ'
                        }
                })
        if len(response['Items']) == 0:
            print("    Not able to fetch data date of current run for job_id {0}".format(job_id))
            print("    Please check if it is in Running status")
            raise RuntimeError("Not able to fetch data date of current run for job_id {0}".format(job_id))
        else:
            data_date=response['Items'][0]['data_date']["S"]
        print("Data date of current run: {0}".format(data_date))
        print("Now fetching parent_job_ids which current job is dependent upon")
        response=dynamo.query(TableName=self.job_dependency_table,KeyConditions=
                {
                "job_id":{
                        "AttributeValueList":[{"S":job_id}],
                        'ComparisonOperator': 'EQ'
                        }
                })
        for item in response['Items']:
            parent_job_id=item['depending_on_parent_job_ids']['S']
            latency_in_days=int(item['latency_in_days']['N'])
            dependent_data_date=str(datetime.strptime(data_date,'%Y-%m-%d').date() + relativedelta(days=-latency_in_days))
            print("    Checking dependency for parent_job {0}, latency is set to {1}".format(parent_job_id,latency_in_days))
            print("    Now fetching all children job_ids for parent_job {0}".format(parent_job_id))
            response=dynamo.query(TableName=self.job_control_table,IndexName='parent_job_id-index',KeyConditions=
                    {
                    "parent_job_id":{
                            "AttributeValueList":[{"S":parent_job_id}],
                            'ComparisonOperator': 'EQ'
                            }
                    })
            if len(response['Items']) == 0:
                print("        No child job found for parent job {0}".format(parent_job_id))
            for item in response['Items']:
                child_job_id=item['job_id']['S']
                print("        Checking completion of job_id {0} for data date {1}".format(child_job_id,dependent_data_date))
                response=dynamo.query(TableName=self.job_status_table,
                    KeyConditions=
                    {
                        "job_id":{
                            "AttributeValueList":[{"S":child_job_id}],
                            'ComparisonOperator': 'EQ'
                            }
                    },
                    QueryFilter=
                    {
                        "status":{
                            "AttributeValueList":[{"S":"Completed"}],
                            'ComparisonOperator': 'EQ'
                            }
                    })
                seq = [item['data_date']["S"] for item in response['Items']]
                if len(seq) == 0:
                    print("            No run stats entry present for Job_ID {0}".format(child_job_id))
                    dependency_flag=False
                    continue
                max_completed_date=max(seq)
                if max_completed_date == dependent_data_date:
                    print("            Job_ID {0} is complete for data date {1}".format(child_job_id,dependent_data_date))
                else:
                    print("            Job_ID {0} is not complete for data date  {1}, max complete date for the dependency job is {2}".format(child_job_id,dependent_data_date,max_completed_date))
                    dependency_flag=False
        if dependency_flag:
            print("Dependency check passed")
            return True
        else:
            print("Dependency check failed")
            return False
