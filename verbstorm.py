import requests
import time
import logging
import threading

# Define standard and tampered HTTP methods
http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
tampered_methods = ['gEt', 'pOsT', 'TrAcK', 'CoNnEcT']

# Initialize logging
logging.basicConfig(filename='verb_tampering_results.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_http_verb_tampering(url, method, verbose=True):
    try:
        # Send request with a specific HTTP method
        response = requests.request(method, url)
        
        # Analyze and log the result
        result = f"\nMethod: {method}\nStatus Code: {response.status_code}\n"
        result += f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}\n"
        result += f"Response Headers: {response.headers}\n"
        result += f"Response Body: {response.text[:200]}..."  # Limiting body output for readability
        logging.info(result)
        
        if verbose:
            print(result)
        
    except Exception as e:
        logging.error(f"Method: {method} failed. Error: {e}")
        if verbose:
            print(f"Method: {method} failed. Error: {e}")

def run_tests(url, delay=1, verbose=True, parallel=False):
    print(f"\nTesting URL: {url} for HTTP Verb Tampering...\n")
    
    methods_to_test = http_methods + tampered_methods
    threads = []
    
    for method in methods_to_test:
        if parallel:
            t = threading.Thread(target=check_http_verb_tampering, args=(url, method, verbose))
            threads.append(t)
            t.start()
        else:
            check_http_verb_tampering(url, method, verbose)
            time.sleep(delay)  # Rate limiting between requests
            
    if parallel:
        for t in threads:
            t.join()

# Main code to get user input and run the test
if __name__ == '__main__':
    url = input("Enter the URL: ")
    mode = input("Verbose mode? (yes/no): ").strip().lower() == 'yes'
    parallel_mode = input("Run in parallel? (yes/no): ").strip().lower() == 'yes'
    delay_time = float(input("Enter delay time between requests (in seconds): "))
    
    run_tests(url, delay=delay_time, verbose=mode, parallel=parallel_mode)
    print("\nTesting complete! Results are logged in 'verb_tampering_results.log'")
