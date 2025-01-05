# DIG Command Executor ( adv_dig.sh )
A **comprehensive DNS testing tool** built with **Bash** that automates DNS queries using the `dig` command. It supports all available query types and options, logs results, handles errors gracefully, and provides detailed output for analysis.
***
## Features

* **Automated DNS Queries:** Iterates through all combinations of:
 
  * Domains
  * DNS Servers
  * Query Types (e.g., A, AAAA, MX, NS, etc.)
  * DIG Options (e.g., +short, +trace, +dnssec, etc.)

* **Logging:**:

  * Saves results in a log file with a timestamp.
  * Separates error logs for troubleshooting.

* Error Handling: Captures errors during execution for debugging.
* Reverse DNS Lookup: Includes a dedicated section for reverse DNS queries.
* Customizable: Easily modify domains, servers, and options.
***
# How to Use
## Prerequisites
 1. #### Install DIG:
    * For Debian/Ubuntu:

       ```
       sudo apt install dnsutils
       ```
    * For RHEL/CentOS:

      ```
      sudo yum install bind-utils
      ```
 2. #### Clone the Repository:

     ```
     git clone https://github.com/YourUsername/dig-command-tool.git
     cd dig-command-tool
     ```
 3. #### Make the Script Executable:

    ```
    chmod +x dig_tool.sh
    ```
***

## Running the Tool

1. Execute the script:

   ```
   ./dig_tool.sh
   ```
2. Logs are saved in the current directory
   * Results: `dig_results_<timestamp>.log`
   * Errors: `dig_errors_<timestamp>.log`
***
## Customizations
You can modify the script to suit your needs:

### 1. Add Domains
Update the `domains` array to include the domains you want to test:

```
domains=("example.com" "test.com" "mydomain.org")
```
### 2.Add DNS Servers
Modify the `servers` array to include additional DNS servers:  

```
servers=("8.8.8.8" "1.1.1.1" "9.9.9.9")
```
### 3. Add or Remove DIG Options
Edit the `options` array to customize the `dig` commands:

```
options=(
    "+short" "+trace" "+dnssec" "+tcp" "+timeout=5"
)
```
***
### Use Cases
* DNS Enumeration: Essential for penetration testing and red teaming.
* Performance Testing: Assess DNS server response times and configurations.
* Error Debugging: Identify DNS misconfigurations or issues.
* Reverse DNS Lookups: Map IP addresses to hostnames for forensics.
