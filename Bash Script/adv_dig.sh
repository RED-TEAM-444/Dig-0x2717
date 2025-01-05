#!/bin/bash
# Comprehensive DIG Command Executor with Logging and Error Handling
# Author: SID || RED TEAM
# Description: This script automates extensive DNS testing using DIG with all available options.

# Amazing Banner
clear
echo "######################################"
echo "#          DIG COMMAND TOOL          #"
echo "#          by SID | RED TEAM         #"
echo "######################################"

# Define domains and DNS servers
domains=("example.com")
servers=("8.8.8.8" "1.1.1.1")

# Define all possible query types and exhaustive dig options
query_types=("A" "AAAA" "MX" "NS" "SOA" "CNAME" "TXT" "PTR" "SRV" "CAA" "ANY")
options=(
    "+short" "+noall +answer" "+dnssec" "+trace" "+multiline"
    "+edns" "+tcp" "-4" "-6" "+bufsize=4096" "+norecurse"
    "+nsid" "+expire" "+dns64prefix" "+cdflag" "+additional"
    "+adflag" "+besteffort" "+defname" "+ednsflags=0x8000"
    "+ednsopt=15:01ff" "+expandaaaa" "+header-only"
    "+https" "+https-get" "+http-plain" "+http-plain-get"
    "+keepalive" "+keepopen" "+multiline" "+ndots=2"
    "+nssearch" "+onesoa" "+opcode=QUERY" "+padding=512"
    "+qr" "+raflag" "+rdflag" "+recurse" "+retry=3"
    "+search" "+short" "+split=256" "+stats"
    "+subnet=0.0.0.0/0" "+tcp" "+timeout=5" "+tls"
    "+tls-ca" "+tls-hostname=example.com" "+trace"
    "+tries=3" "+ttlid" "+ttlunits" "+unknownformat"
    "+vc" "+yaml" "+zflag"
)

# Log files
log_file="dig_results_$(date +%Y%m%d_%H%M%S).log"
error_log_file="dig_errors_$(date +%Y%m%d_%H%M%S).log"

# Function to run dig commands with enhanced error handling
run_dig_command() {
    local server="$1"
    local domain="$2"
    local qtype="$3"
    local option="$4"

    echo "Running: dig @$server $domain $qtype $option" | tee -a "$log_file"
    output=$(dig @$server $domain $qtype $option 2>&1)
    exit_code=$?

    if [ $exit_code -eq 0 ]; then
        echo "$output" | tee -a "$log_file"
        echo "Success: Command executed successfully!" | tee -a "$log_file"
    else
        echo "Error: dig @$server $domain $qtype $option failed!" | tee -a "$error_log_file"
        echo "$output" | tee -a "$error_log_file"
    fi
    echo "------------------------------------------------------" | tee -a "$log_file"
}

# Execute all dig commands for every combination
echo "Starting DIG Testing on $(date)" | tee -a "$log_file"
for domain in "${domains[@]}"; do
    for server in "${servers[@]}"; do
        for qtype in "${query_types[@]}"; do
            for option in "${options[@]}"; do
                run_dig_command "$server" "$domain" "$qtype" "$option"
            done
        done
    done
done

# Reverse DNS Lookup Section
echo "Running Reverse DNS Lookups..." | tee -a "$log_file"
run_dig_command "8.8.8.8" "8.8.8.8" "PTR" "+short"
run_dig_command "1.1.1.1" "1.1.1.1" "PTR" "+trace"

# Final Message
echo "Completed all dig command tests! Results saved in $log_file and errors in $error_log_file." | tee -a "$log_file"
