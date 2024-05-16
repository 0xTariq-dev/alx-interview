# Log Parsing Interview Preparation

## Description
This project involves reading from standard input (stdin), handling data in
a specific format, and performing calculations based on the input data.
This aim of this is to mimic a real-world scenario where you would be required
to parse log data and extract useful information from it.

## Example
The input data will be a stream of web server like logs in the following format:
>  Note: Any line that does not match the format below should be ignored.
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
i.e.
130.228.219.7 - [2024-05-17 01:46:25.454277] "GET /projects/260 HTTP/1.1" 405 357
```

The output should be the accumulated file size and the number of occurance for
each status code returned, in the following format:
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
```
The Script will update and print the output every 10 lines of input data.
and Keep track of the total file size and the number of occurrences of each status code.
until the end of the input data.

## Requirements
- Python 3.6 or higher
- re (Regular Expression) module: For parsing the input data and matching the required fields.



