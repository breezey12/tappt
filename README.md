## Tappt

### Current

The current functionality of Tappt is that it allows a user to enter a YouTube URL and a keyword, then displays the embedded YouTube, which begins playing one second before the keyword is spoken.

### Future

In the future, Tappt will monitor live video/audio streams for a keyword/set of keywords, and notify the user when one of their words is spoken, providing a direct link to the video feed.

We also plan to do something with the library of transcripts that will be built up every time someone does a search: Interactive transcripts, integration with hyperaud.io -- the list is kind of endless.

### Dependencies

* pip
* everything in requirements.txt
* Python (2.7.9)
* an account + API key from [Speechmatics](https://speechmatics.com/register).

### Installation

1. clone this repo, `cd` into it.
1. `pip install -r requirements.txt`.
1. `cd app`.
1. create a file named `_local_config.py` and add a single line: `SPEECHMATICS_API_KEY =`, then your API key surrounded by quotes.
1. `python run.py`.
1. open `http://127.0.0.1:5000/` in your browser.

### Instant Gratification

Since there's already a .json transcript provided, you can check out Tappt's functionality without a Speechmatics API key or waiting for an API call to that service, by using `https://www.youtube.com/watch?v=8MNCQTgB7o0` as your URL.  Some keywords that show up that video are "writing", "writers", "usually", and "talking".

### Usage

When you search for a URL that hasn't already been transcribed, it will take about 7x the running length (as of 5/4/2015) to transcribe/index it, then search it.  This means that if the YouTube is one minute long, it will take seven minutes before you get a result.

### Feedback and Contributions

Please create Github issues if you have any feedback or feature requests!  Also, this is a hyper-maintained project, so please fork and pull request at will; we will respond.  Lotsa issues over there →→→ :-)
