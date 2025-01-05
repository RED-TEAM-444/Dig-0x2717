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


# Explanation of the Code (adv2_dig.sh)
This script is an advanced automation tool for executing exhaustive DNS queries using the dig command. Developed by SID | RED TEAM, it combines user-friendly customization, comprehensive DNS testing, parallel query execution, security testing, and automated reporting in HTML format.

### Features
1. Dynamic Input Handling:

  * Supports both default configurations and custom user inputs for domains, servers, query types, and options.
  * Custom mode is activated with the --custom argument.

2. Exhaustive DNS Query Execution:

  * Executes dig commands for all combinations of:
     * Domains
     * DNS servers
     * Query types (e.g., A, MX, TXT, etc.)
     * Options (e.g., +trace, +dnssec, etc.)

3. Parallel Execution:

  * Leverages xargs for parallel query execution, improving efficiency and reducing runtime.

4. Security Testing:

  * Includes DNS zone transfer checks to identify potential misconfigurations or vulnerabilities in DNS servers.

5. Reverse DNS Lookups:

  * Performs reverse lookups for specified IP addresses with various dig options.

6. Interactive HTML Reporting:

  * Generates an HTML report containing all DNS query results for easy review and sharing.

7. Error Handling:

  * Logs errors encountered during queries into a separate errors.log file.

8. Logging:

  * Saves the script output to a timestamped log file.

***
# Comprehensive Usage
## Prerequisites

1. Install DIG:
  * For Debian/Ubuntu:

    ```
    sudo apt install dnsutils
    ```
  * For RHEL/CentOS:

     ```
    sudo yum install bind-utils
    ```
2. Clone the Repository:

    ```
    git clone https://github.com/YourUsername/advanced-dig-tool.git
    cd advanced-dig-tool
    ```
4. Make the Script Executable:

   ```
   chmod +x dig_tool_advanced.sh
   ```
### Running the Script
1. **Default Mode:** Run the script without arguments to use default domains, servers, query types, and options:

    ```
   ./dig_tool_advanced.sh
   ```
2. **Custom Mode:** Use the --custom flag to input custom domains, servers, query types, and options:

   ```
   ./dig_tool_advanced.sh --custom
   ```
### Customization
1. **Add Domains:** Modify the domains array to include more domains:

   ```
   domains=("example.com" "test.com" "mydomain.org")
   ```
2. **Add DNS Servers:** Update the servers array with additional servers:

   ```
   servers=("8.8.8.8" "1.1.1.1" "9.9.9.9" "208.67.222.222")
   ```
3. **Add Query Types:** Extend the query_types array with additional DNS record types:

   ```
   query_types=("A" "AAAA" "MX" "TXT" "PTR" "NAPTR" "URI")
   ```
4. **Modify Options:** Add or remove dig options in the options array:

   ```
   options=("+trace" "+dnssec" "+tcp" "+short" "+norecurse")
   ```
5. **Adjust Parallel Execution:** Customize the degree of parallelism in xargs by modifying -P (number of concurrent processes):

   ```
   parallel_dig() {
    echo "${domains[@]}" | xargs -n 1 -P 8 -I {} dig @${servers[0]} {} ${query_types[0]} ${options[0]}
   }
   ```
### Sample Output
 * Log File: dig_results_20250105_123456.log
 * Error Log: errors.log
 * HTML Report: dig_report_20250105_123456.html
