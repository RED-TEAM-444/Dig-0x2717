#!/bin/bash
#Author : SID || RED TEAM 
# dig Command Combination Automation Script
# This script generates multiple dig command combinations for exhaustive testing.

# Define domains and servers for testing
domains=("example.com" "google.com" "cloudflare.com")
servers=("8.8.8.8" "1.1.1.1")

# Define query types and options
query_types=("A" "AAAA" "MX" "NS" "TXT" "SOA" "CNAME")
options=("+short" "+noall +answer" "+dnssec" "+trace" "+multiline" "+edns" "+tcp" "-4" "-6")

# Loop through all combinations
for domain in "${domains[@]}"; do
    for server in "${servers[@]}"; do
        for qtype in "${query_types[@]}"; do
            for option in "${options[@]}"; do
                echo "Running: dig @${server} ${domain} ${qtype} ${option}"
                dig @${server} ${domain} ${qtype} ${option}
                echo "------------------------------------------------------"
            done
        done
    done
done

# Reverse DNS Lookup
echo "Running Reverse DNS Lookup Examples"
dig -x 8.8.8.8 +short
dig -x 1.1.1.1 +trace

echo "Completed all dig command tests!"

# End of Script
