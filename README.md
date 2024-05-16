# Constituition Chat

> Commandline chatbot to learn about the constituition of ghana!

This chatbot helps you learn about the constituion of ghana, it can answer any questions that relates to the 1996 constituition.

![](header.png)

## Requirements

1. Python3 (<https://www.python.org/>)
2. pipenv (<https://pipenv.pypa.io/en/latest/>)

## Running Locally

1. clone the repo
2. run `sh pipenv pipenv install`
3. run `sh pipenv pipenv shell`
4. run `sh pipenv run python3 app.py`

## Usage example

How can I become a citizen of Ghana?

## How it works

1. PyPdfLoaderReads reads the document from the path provided into array of documents, where each document contains the page content and metadata with page number,and splits them into chunks.
2. The pdf chunks are then passed into chromadb which creats embeddings for them using the AzureOpenAIEmbeddings.
3. When a prompt is received, the prompt is passed to chromadb which them creates embeddings and does a similarity check to retrieve results that correspond to the prompt
4. The results together with the prompt is then passed to the llm using "rlm/rag-prompt" to make sense out of it and the response is printed to the screen.

# Note

This project can be adapted for any use case, just change the pdf file to any pdf of your choice and you will have the same functionality. enjoy!

If you have any feature reaquest, feel free to reach out to me or contribute!

## Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
