# Verbstorm

Verbstorm is an automated Python tool designed to test URLs for HTTP Verb Tampering. It sends requests using standard and tampered HTTP methods, analyzes the server's response, and logs the results. This tool is highly customizable with features like rate limiting, parallel requests, and verbose output for detailed analysis.

## Features

- **HTTP Verb Tampering Tests**: Tests standard HTTP methods (`GET`, `POST`, `PUT`, etc.) and tampered variants (`gEt`, `pOsT`, etc.).
- **Response Analysis**: Logs status codes, headers, content type, and a snippet of the response body.
- **Rate Limiting**: Adds a customizable delay between requests to avoid overwhelming the server.
- **Parallel Requests**: Option to run requests concurrently to speed up testing.
- **Verbose/Silent Modes**: Toggle between detailed output and minimal output.
- **Tampered Verbs**: Checks non-standard HTTP methods like `TRACK`, `CONNECT`, and unusual verb casings.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/verbstorm.git
```
```bash
 cd verbstorm
```
```bash
pip install -r requirements.txt
```
```bash
pip install requests
```

## Usage

1.Run the script:
```bash
python3 verbstorm.py
```
2.Input the URL to test when prompted:
```bash
Enter the URL: http://example.com
```
3.Choose your preferred mode:

- **Verbose** : Display detailed output.
- **parallel** : Run requests in parallel.
- **delay** : Set a delay between requests (in seconds).

4.After the test completes, check the verb_tampering_results.log file for a detailed log of all requests and responses:
```bash
cat verb_tampering_results.log
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
