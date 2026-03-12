#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
████████╗ █████╗ ██████╗ ██████╗  ██████╗     ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
   ██║   ███████║██████╔╝██████╔╝██║   ██║    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
   ██║   ██╔══██║██╔══██╗██╔══██╗██║   ██║    ██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗   ██║   
   ██║   ██║  ██║██████╔╝██║  ██║╚██████╔╝    ██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
"""

import requests
import threading
import random
import string
import time
import os
import sys
from datetime import datetime

# Colors - Professional Hacker Style
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    DARK = '\033[90m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

C = Color()

# Clear screen
os.system('clear' if os.name == 'posix' else 'cls')

# Banner
print(f"""{C.RED}{C.BOLD}
╔══════════════════════════════════════════════════════════════════╗
║  ████████╗ █████╗ ██████╗ ██████╗  ██████╗     ██████╗ ███████╗  ║
║  ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝  ║
║     ██║   ███████║██████╔╝██████╔╝██║   ██║    ██████╔╝█████╗    ║
║     ██║   ██╔══██║██╔══██╗██╔══██╗██║   ██║    ██╔══██╗██╔══╝    ║
║     ██║   ██║  ██║██████╔╝██║  ██║╚██████╔╝    ██║  ██║███████╗  ║
║     ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝  ║
╠══════════════════════════════════════════════════════════════════╣
║{C.CYAN}                    🔥 NUCLEAR REPORT ENGINE v6.0 🔥              {C.RED}║
║{C.GREEN}                    ⚡ DEVELOPER: @tabbo73 ⚡                    {C.RED}║
║{C.PURPLE}                    💀 POWER: 10,000 THREADS 💀                  {C.RED}║
╚══════════════════════════════════════════════════════════════════╝{C.RESET}
""")

# Configuration
class Config:
    MAX_THREADS = 10000  # Nuclear power
    REPORT_DELAY = 0.0001  # Speed of light
    BATCH_SIZE = 1000  # Reports per batch
    USE_PROXY = False
    SHOW_LIVE_STATS = True

# Stats tracking
stats = {
    'sent': 0,
    'failed': 0,
    'total': 0,
    'start_time': time.time()
}
stats_lock = threading.Lock()

# User Agents (Real ones)
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
]

# LSD Tokens
LSD_TOKENS = [
    'AVq5uabXj48', 'AVp2kLmN56', 'AVr7xYz78', 'AVw9qRsT12', 
    'AVm3nPqR34', 'AVk4lHtW89', 'AVb2nMpX23', 'AVc5vYzR67',
    'AVd8wQsT90', 'AVf1jKlP45', 'AVg6hYtU78', 'AVj9kLpO12',
    'AVz5xQwE34', 'AVn8bVcR67', 'AVt2yXzU89', 'AVp4lMkN12'
]

# Email domains
EMAIL_DOMAINS = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com', 'protonmail.com', 'aol.com', 'mail.com']

def generate_email():
    """Generate random email"""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits + '._', k=random.randint(8, 15)))
    domain = random.choice(EMAIL_DOMAINS)
    return f"{username}@{domain}"

def generate_headers():
    """Generate random headers"""
    return {
        "Host": "help.instagram.com",
        "x-fb-lsd": random.choice(LSD_TOKENS),
        "x-asbd-id": str(random.randint(129477, 129999)),
        "sec-ch-ua-mobile": random.choice(["?0", "?1"]),
        "user-agent": random.choice(USER_AGENTS),
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://help.instagram.com",
        "referer": "https://help.instagram.com/contact/723586364339719",
        "accept-language": random.choice(["en-US,en;q=0.9", "hi-IN,hi;q=0.9,en;q=0.8", "ar-SA,ar;q=0.9,en;q=0.8"]),
        "cookie": f"ig_nrcb=1; sessionid={random.randint(100000, 999999)}"
    }

def generate_data(username, fullname, email):
    """Generate form data"""
    timestamp = str(int(time.time()))
    
    data = {
        'jazoest': str(random.randint(2000, 9999)),
        'lsd': random.choice(LSD_TOKENS),
        'Field258021274378282': username,
        'Field735407019826414': fullname,
        'Field506888789421014[year]': str(random.randint(2000, 2012)),
        'Field506888789421014[month]': str(random.randint(1, 12)),
        'Field506888789421014[day]': str(random.randint(1, 28)),
        'Field294540267362199': random.choice(['Parent', 'Friend', 'Self', 'Other']),
        'inputEmail': email,
        'support_form_id': '723586364339719',
        'support_form_locale_id': 'en_US',
        'support_form_hidden_fields': '{}',
        'support_form_fact_false_fields': '[]',
        '__user': '0',
        '__a': '1',
        '__req': str(random.randint(1, 50)),
        '__hs': f"19552.BP:DEFAULT.{random.randint(1,5)}.0..0.0",
        'dpr': str(random.choice([1,2,3])),
        '__ccg': random.choice(['GOOD', 'FAIR']),
        '__rev': str(random.randint(1007841948, 1007941948)),
        '__spin_t': timestamp
    }
    
    return '&'.join([f"{k}={v}" for k, v in data.items()])

def send_report(username, fullname, report_id):
    """Send single report"""
    email = generate_email()
    headers = generate_headers()
    data = generate_data(username, fullname, email)
    
    try:
        response = requests.post(
            'https://help.instagram.com/ajax/help/contact/submit/page',
            data=data,
            headers=headers,
            timeout=2
        )
        
        with stats_lock:
            if response.status_code == 200:
                stats['sent'] += 1
                status = f"{C.GREEN}✓{C.RESET}"
            else:
                stats['failed'] += 1
                status = f"{C.YELLOW}⚠{C.RESET}"
            
            stats['total'] += 1
            
        return response.status_code == 200
        
    except Exception as e:
        with stats_lock:
            stats['failed'] += 1
            stats['total'] += 1
        return False

def worker(username, fullname, report_id):
    """Worker thread function"""
    send_report(username, fullname, report_id)

def show_stats():
    """Display live statistics"""
    while True:
        time.sleep(1)
        elapsed = time.time() - stats['start_time']
        rate = stats['total'] / elapsed if elapsed > 0 else 0
        success_rate = (stats['sent'] / max(stats['total'], 1)) * 100
        
        os.system('clear')
        print(f"""{C.RED}{C.BOLD}
╔══════════════════════════════════════════════════════════════╗
║              🔥 TABBO REPORT - LIVE STATS 🔥                 ║
╠══════════════════════════════════════════════════════════════╣
║{C.GREEN}  ✓ Sent: {stats['sent']:<10}{C.RED}                                        ║
║{C.YELLOW}  ⚠ Failed: {stats['failed']:<8}{C.RED}                                        ║
║{C.CYAN}  📊 Total: {stats['total']:<9}{C.RED}                                        ║
║{C.PURPLE}  ⚡ Rate: {rate:.1f}/sec{C.RED}                                            ║
║{C.BLUE}  📈 Success: {success_rate:.1f}%{C.RED}                                         ║
║{C.WHITE}  ⏱️  Time: {elapsed:.1f}s{C.RED}                                             ║
╠══════════════════════════════════════════════════════════════╣
║{C.GREEN}              🎯 Target: @{username}{C.RED}                                      ║
╚══════════════════════════════════════════════════════════════╝{C.RESET}
        """)

def main():
    # Get target info
    print(f"\n{C.YELLOW}[+] Enter Target Information{C.RESET}\n")
    
    username = input(f"{C.CYAN}Username (without @): {C.WHITE}").strip()
    fullname = input(f"{C.CYAN}Full Name: {C.WHITE}").strip()
    
    try:
        threads = int(input(f"{C.CYAN}Threads (1000-10000): {C.WHITE}").strip() or "5000")
        threads = max(1000, min(10000, threads))
    except:
        threads = 5000
    
    print(f"\n{C.RED}[!] NUCLEAR ATTACK INITIATED ON @{username}{C.RESET}")
    print(f"{C.YELLOW}[!] Threads: {threads}{C.RESET}")
    print(f"{C.GREEN}[!] Press Ctrl+C to stop{C.RESET}\n")
    
    time.sleep(2)
    
    # Start stats thread
    if Config.SHOW_LIVE_STATS:
        stats_thread = threading.Thread(target=show_stats, daemon=True)
        stats_thread.start()
    
    # Attack loop
    report_id = 0
    try:
        while True:
            # Create thread batch
            thread_batch = []
            for i in range(min(threads, 1000)):  # Batch size 1000
                report_id += 1
                t = threading.Thread(target=worker, args=(username, fullname, report_id))
                t.start()
                thread_batch.append(t)
                time.sleep(Config.REPORT_DELAY)
            
            # Wait for batch to complete
            for t in thread_batch:
                t.join()
            
    except KeyboardInterrupt:
        print(f"\n{C.RED}[!] Attack stopped by user{C.RESET}")
    
    # Final stats
    elapsed = time.time() - stats['start_time']
    print(f"\n{C.GREEN}════════════════════════════════════════════")
    print(f"        FINAL STATISTICS")
    print(f"════════════════════════════════════════════")
    print(f"Total Reports: {stats['total']}")
    print(f"Successful: {stats['sent']}")
    print(f"Failed: {stats['failed']}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Rate: {stats['total']/elapsed:.1f}/sec")
    print(f"════════════════════════════════════════════{C.RESET}")
    
    print(f"\n{C.CYAN}💀 Developed by @tabbo73 💀{C.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}[!] Exiting...{C.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{C.RED}[!] Error: {e}{C.RESET}")
        sys.exit(1)
