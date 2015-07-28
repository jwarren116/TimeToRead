# TimeToRead

**Deliverable:** A single Python file which requests http://www.expertise.com/api/v1.0/jobs/text, pulls the text from the "text" key and prints out an estimated number of minutes it a person takes read.

**Input:** http://www.expertise.com/api/v1.0/jobs/text (your code should request this via HTTP)

**Example output:** "about 6 minutes" *(this example is not accurate for the given input text)*

## Details

The API responds to a standard HTTP GET request and returns standard JSON, with four keys: source, author, text, title. The "text" key is the only one that matters in this case.

Assuming that the average person reads 200 words per minute, it should be possible to count the number of words returned (the value of the 'text' entry) and then calculate an estimated time to read the text.

Give the answer in minutes, rounding up ("5.2 minutes" would be "about 6 minutes").

Use Python for your code. Feel free to use the [*Requests* library](http://docs.python-requests.org/en/latest/) to make the HTTP request (it will handle the JSON for you).
