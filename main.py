import boto3
import os
from os import getenv
from dotenv import load_dotenv
import logging
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
import argparse
from pprint import pprint
import time
import urllib

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument('-npu', type=int, help='number of public subnet')
parser.add_argument('-npr', type=int, help='number of private subnet')
parser.add_argument('--create_vpc_with_subnets', "-cvws", nargs='?', const='true', help='create vpc with subnets' )
parser.add_argument('--create_vpc', "-cv", nargs='?', const='true', help='create vpc' )
parser.add_argument('--tag_vpc', "-tv", type=str, help='Name of vpc')
parser.add_argument('--vpc_id', "-vi", type=str, help='vpc ID')
parser.add_argument('--subnet_id', "-si", type=str, help='subnet ID')
parser.add_argument('--key_pair_name', "-kpn", type=str, help='key pair name')
parser.add_argument('--create_IGW', "-cIGW", nargs='?', const='true', help='create IGW' )
parser.add_argument('--attach_IGW', "-aIGW", nargs='?', const='true', help='attach IGW to vpc' )

args = parser.parse_args()

ec2_client = boto3.client(
    "ec2",
    aws_access_key_id=getenv("aws_access_key_id"),
    aws_secret_access_key=getenv("aws_secret_access_key"),
    aws_session_token=getenv("aws_session_token"),
    region_name=getenv("aws_region_name")
)

def create_vpc():
    result = ec2_client.create_vpc(CidrBlock="10.22.0.0/16")
    vpc = result.get("Vpc")
    vpc_id = vpc.get("VpcId")
    print(vpc)
    return vpc_id

def add_name_tag(vpc_id):
    ec2_client.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": args.tag_vpc}])
    print(f'{args.tag_vpc} tag created')

def create_igw():
    result = ec2_client.create_internet_gateway()
    igw_id = result.get("InternetGateway").get("InternetGatewayId")
    print("InternetGateway created")
    return igw_id

def create_or_get_igw(vpc_id):
    igw_id = None
    igw_response = ec2_client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}])

    if 'InternetGateways' in igw_response and igw_response['InternetGateways']:
        igw = igw_response['InternetGateways'][0]
        igw_id = igw['InternetGatewayId']
    else:
        response = ec2_client.create_internet_gateway()
        pprint(response)
        igw = response.get("InternetGateway")
        igw_id = igw.get("InternetGatewayId")
        response = ec2_client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        print("attached")
        pprint(response)
    return igw_id

def create_route_table_with_route(vpc_id, route_table_name, igw_id):
    response = ec2_client.create_route_table(VpcId=vpc_id)
    route_table = response.get("RouteTable")
    route_table_id = route_table.get
    
def create_vpc():
    result = ec2_client.create_vpc(CidrBlock="10.22.0.0/16")
    vpc = result.get("Vpc")
    vpc_id = vpc.get("VpcId")
    print(vpc)
    return vpc_id

def add_name_tag(vpc_id):
    ec2_client.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": args.tag_vpc}])
    print(f'{args.tag_vpc} tag created')

def create_igw():
    result = ec2_client.create_internet_gateway()
    igw_id = result.get("InternetGateway").get("InternetGatewayId")
    print("InternetGateway created")
    return igw_id

def create_or_get_igw(vpc_id):
    igw_id = None
    igw_response = ec2_client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}])

    if 'InternetGateways' in igw_response and igw_response['InternetGateways']:
        igw = igw_response['InternetGateways'][0]
        igw_id = igw['InternetGatewayId']
    else:
        response = ec2_client.create_internet_gateway()
        pprint(response)
        igw = response.get("InternetGateway")
        igw_id = igw.get("InternetGatewayId")
        response = ec2_client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        print("attached")
        pprint(response)
    return igw_id

def create_route_table_with_route(vpc_id, route_table_name, igw_id):
    response = ec2_client.create_route_table(VpcId=vpc_id)
    route_table = response.get("RouteTable")
    route_table_id = route_table.get("RouteTableId")
    pprint(route_table)
    print("Route table id", route_table_id)
  
def create_vpc():
    result = ec2_client.create_vpc(CidrBlock="10.22.0.0/16")
    vpc = result.get("Vpc")
    vpc_id = vpc.get("VpcId")
    print(vpc)
    return vpc_id

def add_name_tag(vpc_id):
    ec2_client.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": args.tag_vpc}])
    print(f'{args.tag_vpc} tag created')

def create_igw():
    result = ec2_client.create_internet_gateway()
    igw_id = result.get("InternetGateway").get("InternetGatewayId")
    print("InternetGateway created")
    return igw_id

def create_or_get_igw(vpc_id):
    igw_id = None
    igw_response = ec2_client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}])

    if 'InternetGateways' in igw_response and igw_response['InternetGateways']:
        igw = igw_response['InternetGateways'][0]
        igw_id = igw['InternetGatewayId']
    else:
        response = ec2_client.create_internet_gateway()
        pprint(response)
        igw = response.get("InternetGateway")
        igw_id = igw.get("InternetGatewayId")
        response = ec2_client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        print("Attached")
        pprint(response)
    return igw_id

def create_route_table_with_route(vpc_id, route_table_name, igw_id):
    response = ec2_client.create_route_table(VpcId=vpc_id)
    route_table = response.get("RouteTable")
    route_table_id = route_table.get("RouteTableId")
    pprint(route_table)
    print("Route table id", route_table_id)
