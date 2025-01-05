#!/bin/bash
# Author : SID || RED TEAM
# dig Command Combination Automation Script (Advanced Version)
# This script generates multiple dig command combinations for exhaustive testing with advanced features.

# Logging setup
log_file="dig_results_$(date +'%Y%m%d_%H%M%S').log"
exec > >(tee -a "$log_file") 2>&1

# Customizable input handling
if [ "$1" == "--custom" ]; then
    read -p "Enter domains (space-separated): " -a domains
    read -p "Enter servers (space-separated): " -a servers
    read -p "Enter query types (space-separated): " -a query_types
    read -p "Enter options (space-separated): " -a options
else
    # Default values
    domains=("example.com")
    servers=("8.8.8.8" "1.1.1.1" "9.9.9.9" "208.67.222.222" "4.2.2.2" "8.8.4.4")
    query_types=("A" "AAAA" "MX" "NS" "TXT" "SOA" "CNAME" "PTR" "SRV" "CAA" "NAPTR" "DS" "TLSA" "CERT"
                 "HINFO" "DNAME" "APL" "SPF" "NSEC" "NSEC3" "NSEC3PARAM" "RRSIG" "SSHFP" "URI" "IPSECKEY")
    options=("+short" "+noall +answer" "+dnssec" "+trace" "+multiline" "+edns"
             "+tcp" "-4" "-6" "+norecurse" "+besteffort" "+showsearch"
             "+ignore" "+fail" "+nssearch" "+stats" "+identify" "+qr"
             "+comments" "+split=0" "+bufsize=512" "+dnssec-check-names"
             "+edns=0" "+sigchase" "+recurse" "+cmd" "+additional" "+answer"
             "+authority" "+badcookie" "+cookie" "+retry=3" "+time=5")
fi

# Parallel Execution using xargs
parallel_dig() {
    echo "Running parallel dig queries..."
    echo "${domains[@]}" | xargs -n 1 -P 4 -I {} dig @${servers[0]} {} ${query_types[0]} ${options[0]}
}

# Interactive HTML Report Generation
html_report="dig_report_$(date +'%Y%m%d_%H%M%S').html"
echo "<html><head><title>DIG Results</title></head><body><h1>DNS Query Results</h1>" > "$html_report"

# Loop through all combinations
for domain in "${domains[@]}"; do
    for server in "${servers[@]}"; do
        for qtype in "${query_types[@]}"; do
            for option in "${options[@]}"; do
                echo "Running: dig @${server} ${domain} ${qtype} ${option}"
                result=$(dig @${server} ${domain} ${qtype} ${option})
                if [ $? -ne 0 ]; then
                    echo "ERROR: Failed to query ${domain} with ${qtype} on ${server}" >> errors.log
                fi
                echo "<h2>Domain: $domain, Server: $server, Query Type: $qtype</h2><pre>$result</pre>" >> "$html_report"
                echo "------------------------------------------------------"
            done
        done
    done
done

# DNS Security Testing (Zone Transfer Check)
for domain in "${domains[@]}"; do
    for server in "${servers[@]}"; do
        echo "Testing Zone Transfer for $domain on $server"
        dig @$server $domain AXFR | grep -i "Transfer failed" || echo "Possible Zone Transfer Vulnerability on $domain with $server" >> errors.log
    done
done

echo "</body></html>" >> "$html_report"

# Reverse DNS Lookup Examples
echo "Running Reverse DNS Lookup Examples"
dig -x 8.8.8.8 +short
dig -x 1.1.1.1 +trace
dig -x 9.9.9.9 +multiline
dig -x 208.67.222.222 +dnssec
dig -x 4.2.2.2 +comments
dig -x 8.8.4.4 +identify

# Parallel execution example call
parallel_dig

echo "Completed all dig command tests! Check $html_report for a detailed report."

# End of Script
