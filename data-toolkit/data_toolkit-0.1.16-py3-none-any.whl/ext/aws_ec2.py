import boto3
import pandas as pd

def get_ec2(status: str, profile: str, filter: str):
    possible_filters = dict(
        live=[{"Name":"instance-state-name", "Values":["running"] }],
        all=[]
    )

    filters = possible_filters[filter]

    ec2 = boto3.session.Session(profile_name=profile, region_name='eu-west-1').client('ec2')
    live_inst = ec2.describe_instances(Filters=filters)
    # live_inst['Reservations']
    # live_inst['Reservations'][1]['Instances'][0]['PublicIpAddress']
    df = pd.DataFrame(live_inst['Reservations'])
    df_list = [ pd.DataFrame.from_dict(x[0], orient='index') for x in df['Instances'].values ]
    full_df = pd.concat(df_list,axis=1, sort=True)
    pd.set_option('display.max_colwidth', 40)
    return full_df

def update_ec2_ssh(profile: str):
    from .sshconf import read_ssh_config
    # get ec2 and ssh config to get hosts
    running_instances = get_ec2("running", profile=profile)
    ssh_config_obj = read_ssh_config('/Users/jakub/.ssh/config')
    hosts = ssh_config_obj.hosts()
    
    for index, row in running_instances.T.iterrows():
        target_host = [ t['Value'] for t in row.Tags if t['Key']=='Name'][0]
        target_ip = row.PublicIpAddress
        # change and write 
        ssh_config_obj.set(target_host, HostName=target_ip)
        ssh_config_obj.write('/Users/jakub/.ssh/config')
        
    print(ssh_config_obj.config())
    
