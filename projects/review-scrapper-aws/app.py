from flask import Flask, render_template, request, jsonify
from os import environ
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
import certifi
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
# import logging
# logging.basicConfig(filename="scrapper.log", level=logging.INFO)

app = Flask(__name__)

load_dotenv()


@app.route("/", methods=['GET'])
def homepage():
    return render_template("index.html")


@app.route("/review", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url)
            flipkartPage = uClient.read()
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser")
            bigboxes = flipkart_html.findAll(
                "div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + \
                box.div.div.div.a['href']
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8'
            prod_html = bs(prodRes.text, "html.parser")
            # print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            reviews = []
            name = ""
            custComment = ""
            for commentbox in commentboxes:
                try:
                    # name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all(
                        'p', {'class': '_2sc7ZR _2V5EHH'})[0].text
                except:
                    # logging.info("name")
                    pass
                try:
                    # rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'
                    # logging.info("rating")
                    pass
                try:
                    # commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'
                    # logging.info(commentHead)
                    pass
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    # custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    # logging.info(e)
                    pass

                mydict = {
                    "Product": searchString,
                    "Name": name,
                    "Rating": rating,
                    "CommentHead": commentHead,
                    "Comment": custComment
                }

                reviews.append(mydict)
            # logging.info(f"log my final result {reviews}")

            client = MongoClient(
                environ["MONGO_URI"], tlsCAFile=certifi.where())

            db = client["scrapper-db"]
            scoll = db["scrapper_collection"]
            scoll.insert_many(reviews)

            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            # logging.info(e)
            return 'something is wrong'
    # return render_template('results.html')

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
