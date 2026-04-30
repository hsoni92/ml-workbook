# VPC Basics

## What a VPC gives you
- A Virtual Private Cloud is an isolated logical network where AWS resources receive private IP addresses.
- It belongs to one Region and spans multiple Availability Zones through subnets.
- Default VPC is convenient for labs; custom VPC is preferred for real designs because CIDR, subnetting, and routing are deliberate.

## Core building blocks
- CIDR block: private address range, commonly from RFC1918 ranges such as 10.0.0.0/16.
- Subnet: AZ-scoped slice of the VPC CIDR.
- Route table: maps destination ranges to targets such as local, IGW, NAT, peering, or VPN.
- Internet Gateway: horizontally scaled AWS-managed gateway for internet-routable traffic.

## Answering exam questions
- If instances in same VPC cannot talk, check security groups and NACLs before assuming routing; local route exists by default.
- If internet access fails, verify route table target, public IP/NAT path, and firewall rules.
- If connecting two networks, CIDR overlap is usually the hard blocker.
