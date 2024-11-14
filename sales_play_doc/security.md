RBAC
Role-based access control (RBAC) provides an extension to Redpanda’s existing access control lists (ACLs). Using rpk or Redpanda Console, you can create roles and assign those roles as the authorized or denied party for an ACL. Every user you assign to that role inherits those privileges. RBAC provides a more flexible and efficient way to manage user privileges, especially with complex organizational hierarchies or large numbers of users.

Overview
Redpanda Data maintains a set of internal information security policies and processes based on controls and best practices from AICPA SOC 2 Trust Services Criteria. The purpose of this document is to highlight processes and controls that Redpanda Data has put in place to safeguard data and ensure the security, availability, and privacy of information systems. Policies that are related to Redpanda Cloud are specifically called out when relevant.

Redpanda Data has two cloud offerings:

Dedicated, where Redpanda Cloud clusters are running in Redpanda Data’s own cloud account;
Bring Your Own Cloud (BYOC), where Redpanda Cloud _clusters are running in the customer’s own cloud account.
For the purposes of this document, any reference to Redpanda Cloud is applicable to both offerings.

Customer Data Access & Management
Redpanda Cloud is available on Amazon Web Services (AWS) and Google Cloud Platform (GCP) as either Dedicated or BYOC (Bring your own Cloud) as defined above.

Customers receive a single-tenant Redpanda Cloud cluster isolated with a separate virtual private cloud (VPC) network inside a Redpanda managed cloud account for Dedicated, or within the customer’s own VPC and cloud account for BYOC. Dedicated customers can choose between a publicly or privately accessible network, with the private network only being accessible within the same VPC or using VPC peering. BYOC customers are able to use the public or private network.

Identity & Access Management
Redpanda Cloud supports federated authentication, more commonly known as Single Sign On (SSO), using OAuth2 or OpenIDConnect (OIDC) compatible identity providers. For OIDC and OAuth2 token exchanges, we use OAuth2’s authorization code flow and Proof Key for Code Exchange (PKCE). Additionally, access tokens never leave the customer network or user’s browser, and are always encrypted at rest using AES-256 GCM.

When not using federated authentication, Redpanda Cloud authenticates users directly using their email and password. Passwords are hashed, salted, and encrypted at rest using bcrypt.

Secure Remote Access
Redpanda Cloud implements rigorous access control measures to ensure the privacy and security of customer data. A limited number of Redpanda Data employees are granted access to Redpanda Cloud production environments. Authentication is required to access Redpanda resources, with engineers being authenticated through SSO and subjected to a 2-factor authentication challenge.

Redpanda Cloud clusters are bootstrapped with an agent which receives instructions to provision and configure infrastructure and run maintenance and support activities. Zero Trust access tooling is utilized when manual access to Redpanda Cloud clusters is required. All interactive sessions are recorded and stored for auditing purposes to track and record who has done what on which environments, and when.

Security Education
All Redpanda staff complete required security training annually and at onboarding. Internal documentation provides staff with guidance in the application of security policies.

Data Protection
Data at Rest
Redpanda Cloud relies on the cloud provider’s default volume encryption. Please see the vendor documentation for AWS, GCP, and Azure for details.

Data in Transit
All customer data and cluster operations network traffic is TLS 1.2 encrypted.

TLS certificates are generated and signed by Let’s Encrypt. Redpanda Cloud implements mitigations to prevent ill-intentioned actors from enumerating the clusters’ endpoints through the public certificate transparency log.

Secret Management
Redpanda Cloud generally favors using dynamic credentials when possible, through IAM roles with policies constrained to actions and resources the principal strictly needs, following the principle of least privilege.

Static secrets are safely stored either in AWS or GCP’s Secret Manager service. Redpanda Cloud also generates dedicated secrets for every cluster and performs periodic rotation. Rotating secrets means that at a given moment in time, multiple versions for the same secrets will be active and used until the rotation process finishes.

Static secrets managed through Redpanda Console never leave their corresponding customer environment, and are securely stored in AWS and GCP Secret Manager services.

Product Security
Redpanda Cloud follows a comprehensive vulnerability management policy to ensure the prevention and mitigation of technical vulnerabilities in a timely manner. The company uses various methods to obtain information regarding potential vulnerabilities, including vulnerability scanning, penetration tests, and the bug bounty program.

Penetration testing
Penetration tests of the applications and production network are conducted at least once a year, with additional testing following significant changes to production systems.

Vulnerability Scanning
Vulnerability scans are conducted internally on a regular basis. Redpanda determines the severity of each vulnerability, creating service tickets for critical or high-risk findings that are then assessed by the IT and Engineering departments. The company assesses the severity level based on internal knowledge and understanding of technical architecture and the real-world impact/exposure. Redpanda Data commits to remedying vulnerabilities within specific timeframes, including 30 days for critical and high-risk findings.

Data Privacy
We publish our full privacy policy here: https://redpanda.com/privacy-policy

Business Continuity & Disaster Recovery
Redpanda Data has a business continuity plan to ensure the continuation of critical services in the event of extended service outages caused by factors beyond our control (e.g. natural disasters, man-made events), and to restore services to the widest extent possible in a minimum time frame.

The policy also stipulates a disaster recovery test, including a test of backup restoration processes, to be performed on an annual basis.

Responsible Disclosure
Redpanda appreciates the efforts of those who report security vulnerabilities to us. If you would like to get in touch please directly contact our information security team at security@redpanda.com.

