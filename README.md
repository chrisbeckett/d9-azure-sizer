What does this script do?
-------------------------

Sizer logs into an Azure AD tenant, obtains a list of all subscriptions attached to it and then collects statistics on **Virtual Machines**, **Azure Functions** and **SQL Servers** for *indicative* Dome9 licensing purposes. As **D0** and **A0** instance types are not billable assets, these are exempted from the final figures. Function licenses are a total of all function webapps divided by 6 (the current license model).

![alt text](https://github.com/chrisbeckett/d9-azure-sizer/blob/master/sizer.png "Sizer screenshot")

What's New? (8th January 2021)
------------------------------

- Updated core libraries to latest version, resolving security issue in cryptography library
- Changed references from Dome9 to CloudGuard
- Updated standalone Windows executable
- New MacOS standalone executable
- Updated to reflect the changes in licensing for serverless functions (6:1 ratio of functions to single asset license)

Standalone executable
-----------------------------

If you need to run the tool as a one off and don't want the faff of all the steps below, you can download the ZIP archive. This is a portable version of the tool for Windows or Mac, all batteries included. Download and extract the appropriate platform ZIP and run the executable.

Pre-requisites
--------------
To run this script, you will need the following:-

1) **Python 3.6** (or newer)

2) An Azure AD **Application Registration** (see *https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal*)

3) Azure environment information
    - Azure AD **tenant ID**
    - Azure **Application (Client) ID**
    - Azure **Application (Client) Secret Key**
    
4) You will need the **Azure Management Group** construct configured against your Azure AD (see *https://docs.microsoft.com/en-us/azure/governance/management-groups/overview* for further information). **Adding the Application ID as a Contributor in the IAM Access Control blade in the Tenant Root Group will provide discovery capability.**

5) Run **git clone https://github.com/chrisbeckett/d9-azure-sizer.git**

6) Run **python -m venv d9-azure-sizer**

7) Run **scripts\activate.bat** to enable the Python virtual environment on Windows, **source bin\activate** on Mac/Linux

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
This tool is to be used to provide indicative numbers of billable assets in an Azure environment for cost analysis purposes. No warranty implied.
