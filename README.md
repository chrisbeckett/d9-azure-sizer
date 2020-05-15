# Dome9 Azure Sizing Tool

What does this tool do?
=======================
Sizer connects to Azure subscriptions on a single Azure AD tenant to estimate Dome9 licensing costs. We collect statistics for Virtual Machine instances and SQL Servers. 

Pre-requisites
--------------
To run this script, you will need the following:-

1) **Python 3.6** (or newer)

2) An Azure AD **Application Registration** (see *https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal*)

3) Azure environment information
    - Azure AD **tenant ID**
    - Azure **Application (Client) ID**
    - Azure **Application (Client) Secret Key**
    
4) You will need the **Azure Management Group** construct configured against your Azure AD (see *https://docs.microsoft.com/en-us/azure/governance/management-groups/overview* for further information). This is so that any new subscriptions added against the Azure AD tenant are visible to the onboarding tool. **Adding the Application ID as a Contributor in the IAM Access Control blade in the Tenant Root Group will provide this capability.**

5) Run **git clone https://github.com/chrisbeckett/d9-azure-sizer.git**

6) Run **python -m venv d9-azure-sizer**

7) Run **scripts\activate.bat** to enable the Python virtual environment

8) Run **pip install -r requirements.txt** to install required Python modules
    
Setup
-----
To run the script locally, you need to set several environment variables which are then read in by the script. This prevents any secret keys being hard coded into the script. Set the following:-

- SET AZURE_TENANT_ID=xxxxxxxxxx
- SET AZURE_CLIENT_ID=xxxxxxxxxxx
- SET AZURE_CLIENT_SECRET=xxxxxxxxxxxxxxx

Running the script
------------------
Simply run the script **d9-sizer.py** from the command line 

Disclaimer
==========
This tool is intended for use in Azure environments where Dome9 is to be licensed. It **should not** be used for any definitive license numbers, but to help assist POCs and initial deployments. There is no warranty implied on the report output.
