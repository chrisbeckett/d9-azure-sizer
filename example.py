import os
from haikunator import Haikunator
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.subscription.operations import SubscriptionsOperations
from msrestazure.azure_exceptions import CloudError
from azure.mgmt.compute import ComputeManagementClient
from colorama import Fore
from colorama import init
init()

def verify_env_variables():
    try:
        if 'AZURE_TENANT_ID' in os.environ:
            pass
        else:
            print("ERROR : The Azure AD tenant ID has not been defined in environment variables")
            sys.exit(0)
        if 'AZURE_CLIENT_ID' in os.environ:
            pass
        else:
            print("ERROR : The Azure AD application ID has not been defined in environment variables")
            sys.exit(0)
        if 'AZURE_CLIENT_SECRET' in os.environ:
            pass
        else:
            print("ERROR : The Azure AD application secret key has not been defined in environment variables")
            sys.exit(0)
    except:
        sys.exit(0)

verify_env_variables()

# SET AZURE AD CREDENTIALS
#subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
credentials = ServicePrincipalCredentials(
    client_id=os.environ['AZURE_CLIENT_ID'],
    secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant=os.environ['AZURE_TENANT_ID']
 )

# Read in required environment variables
az_tenant=os.environ['AZURE_TENANT_ID']
az_appid=os.environ['AZURE_CLIENT_ID']
az_appkey=os.environ['AZURE_CLIENT_SECRET']

# INSTANTIATE SDK CLIENT INSTANCES
sub_client = SubscriptionClient(credentials)

def run_example():
    total_number_sql_servers = 0
    try:
        for sub in sub_client.subscriptions.list():
            print("\n"),
            print(Fore.CYAN + "================================================================================================")
            print(Fore.WHITE + 'Subscription found:', sub.subscription_id, sub.display_name)
            print(Fore.CYAN + "================================================================================================")
            resource_client = ResourceManagementClient(credentials, sub.subscription_id)
            resource_client.providers.register('Microsoft.Sql')
            sql_client = SqlManagementClient(credentials, sub.subscription_id)
            compute_client = ComputeManagementClient(credentials, sub.subscription_id) 
            sub_total_number_sql_servers = 0
            for item in sql_client.servers.list():
                print(Fore.WHITE + "================================================================================================")
                print(Fore.YELLOW + "{:30} {:30} {:30}".format("SQL Server Name", "||","Azure Region"))
                print(Fore.WHITE + "================================================================================================")
                print("{:30} {:30} {:30}".format(item.name,"||",item.location))
                sub_total_number_sql_servers = sub_total_number_sql_servers + 1
            print("\n")
            print("Total number of SQL Servers in subscription", sub.display_name,":",sub_total_number_sql_servers)
            for vm in compute_client.virtual_machines.list_all():
                print("VM found: ",vm)
            #total_number_sql_servers = total_number_sql_servers + sub_total_number_sql_servers
    except CloudError as e:
        print(e)
    print("\n")
    print(Fore.GREEN + "REPORT SUMMARY")
    print("==============")
    print("Total number of SQL Servers in Azure AD tenant", az_tenant,":",total_number_sql_servers)
    print("\n")
    print("Total number of Dome9 billable assets is", total_number_sql_servers)
if __name__ == "__main__":
    run_example()
