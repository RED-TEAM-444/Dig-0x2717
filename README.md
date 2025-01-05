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

# Explanation of the Code (tester_dig.sh)
This script automates DNS testing and enumeration using the `dig` command. It systematically runs through combinations of domains, DNS servers, query types, and options to test DNS functionality and behavior comprehensively.

## Comprehensive Usage in Linux
### Prerequisites

1. **Install DIG:**

 * On Debian/Ubuntu

   ```
   sudo apt update && sudo apt install dnsutils
   ```
 * On RHEL/CentOS:

   ```
   sudo yum install bind-utils
   ```
2. **Clone the Repository:**
   * Clone the repository to your system:

     ```
     git clone https://github.com/YourUsername/dig-automation-tool.git
     cd dig-automation-tool
     ```
3. **Make the Script Executable:**

     ```
     chmod +x dig_tool.sh
     ```
### Running the Script
1. **Execute the Script:**

 * Run the script directly:

   ```
   ./dig_tool.sh
   ```
2. **Customizing Inputs:**

 * Edit the arrays in the script to include specific domains, servers, query types, or options:

   ```
   domains=("yourdomain.com" "anotherdomain.org")
   servers=("8.8.8.8" "1.1.1.1")
   query_types=("A" "NS")
   options=("+trace" "+dnssec")
   ```

# DIG Tool GUI Documentation (gui_testing-version.py)

## Overview
This application is a professional graphical user interface (GUI) for the DIG (Domain Information Groper) DNS lookup utility, built using PyQt5. It provides a user-friendly interface to execute DNS queries with various options and parameters, making it easier to perform DNS lookups without memorizing command-line arguments.

## Technical Architecture

### Core Components

1. **CommandRunner (QThread)**
   - Handles asynchronous execution of DIG commands
   - Emits signals for successful output and errors
   - Prevents GUI freezing during command execution

2. **DIGToolGUI (QMainWindow)**
   - Main application window implementing the GUI
   - Organized into five main tabs:
     - Basic Settings
     - Query Options
     - Display Options
     - Advanced Options
     - Logs

### Key Features

#### 1. Basic Settings Tab
- Domain input field
- Query type selection (A, AAAA, MX, NS, etc.)
- Query class selection (IN, CH, HS)

#### 2. Query Options Tab
- Transport Options:
  - TCP usage toggle
  - IPv4/IPv6 protocol selection
- Query Flags:
  - DNSSEC records request
  - CD, RA, and AA flags

#### 3. Display Options Tab
- Output format controls:
  - Short output mode
  - Multiline output
  - Statistics display
  - Comments visibility
  - TTL units formatting

#### 4. Advanced Options Tab
- Timing controls:
  - Query timeout settings
  - Retry attempts configuration
- Custom options input

#### 5. Logs Tab
- Operation logging
- Log saving functionality
- Log clearing option

## Command Construction Logic

The application builds DIG commands using the following structure:
```
dig [domain] -t [query-type] -c [query-class] [transport-options] [query-flags] [display-options] [timing-options] [additional-options]
```

## Installation Requirements

1. Python 3.x
2. PyQt5
3. DIG utility (typically included in Linux distributions)

```bash
# Install required Python packages
pip install PyQt5
```

## Usage Guide

### Basic Query Execution

1. **Launch the Application**
   ```bash
   python3 dig_tool_gui.py
   ```

2. **Basic DNS Query**
   - Enter domain name (e.g., google.com)
   - Select query type (e.g., A for IPv4 address)
   - Click "Execute Query"

### Advanced Features

1. **Transport Configuration**
   - Enable TCP for larger queries
   - Force IPv4/IPv6 protocol when needed

2. **DNSSEC Verification**
   - Enable DNSSEC checkbox for security verification
   - Use CD flag to disable DNSSEC validation

3. **Output Customization**
   - Enable multiline for readable output
   - Use short mode for compact results
   - Enable statistics for query performance data

4. **Timing Controls**
   - Set custom timeout values
   - Configure retry attempts for unreliable connections

### Log Management

1. **Viewing Logs**
   - Switch to Logs tab
   - Review command history and results

2. **Saving Logs**
   - Click "Save Logs"
   - Choose destination file
   - Logs saved in text format

## Common Use Cases

1. **Standard DNS Lookup**
   ```
   Domain: example.com
   Query Type: A
   Query Class: IN
   ```

2. **Mail Server Verification**
   ```
   Domain: example.com
   Query Type: MX
   Display Options: +short
   ```

3. **DNSSEC Validation**
   ```
   Domain: example.com
   Query Type: DNSKEY
   Query Options: +dnssec +cdflag
   ```

## Troubleshooting

1. **Common Issues**
   - Command execution failures
   - Network connectivity problems
   - Invalid domain format

2. **Resolution Steps**
   - Check domain name format
   - Verify network connection
   - Review error messages in logs
   - Ensure DIG utility is installed

## Best Practices

1. **Query Optimization**
   - Use appropriate query types
   - Enable TCP for large responses
   - Set reasonable timeout values

2. **Security Considerations**
   - Use DNSSEC when security is critical
   - Review query responses carefully
   - Monitor operation logs

## Additional Notes

- The application requires proper DNS resolution configuration on the host system
- Some features may require root privileges depending on system configuration
- Regular log maintenance is recommended for optimal performance
