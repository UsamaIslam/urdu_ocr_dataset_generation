# urdu_ocr_dataset_generation
Dataset generation for Urdu OCR. 
## Requirenments:
1) Jupyter Notebook
2) Scrapy
3) Pandas
4) Sellenium
## How to Use:
<ul>
  <li> Download Repository </li>
  <li> Go into the folder named 'bbcurdu' </li>
  <li> open command prompt and enter command `scrapy crawl bbc -o filename.csv`. It will scrape bbcurdu news titles for current page and save it in filename.csv </li>
  <li> Copy this filename.csv in main directory </li>
  <li> Open jupyter Notebook in main directory, in ln[28] you can change the column names to either "content_news" or "title_headlines". </li>
  <li> run all cells </li>
  <li> once done with running all cells open "data_set.py" file and copy paste your jupyter notebook token URL in "data_set.py". You will need drivers for the purticular browser you are using sellenium. Drivers For [Firefox](https://github.com/mozilla/geckodriver/releases) For [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) others can be found [here](https://www.seleniumhq.org/download/). Download driver and place it in main directory.</li>
  <li> Then run "python data_set.py" </li>
  <li> It will create two directories "images" and "texts" with dataset. </li>
</ul>
