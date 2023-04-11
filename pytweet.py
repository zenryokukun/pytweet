"""
Twitterに投稿するスクリプト。tweet(msg:str,*img_paths)。
"""

from requests_oauthlib import OAuth1Session as session
import json
from pprint import pprint

# ツイート用URL v2対応
URL_TWEET = "https://api.twitter.com/2/tweets"

# 画像アップロードURL まだv2がリリースされていないので、v1.1のまま使えとのこと。　
URL_IMAGE = "https://upload.twitter.com/1.1/media/upload.json"


class Pytweet:

    def __init__(self, conf_path):
        """constructor

        Args:
            conf_path (string): path to your twitter confidential file.
        """
        with open(conf_path, "r", encoding="utf-8") as f:
            cf = json.load(f)

        self.req = session(cf["API_KEY"], cf["API_SECRET"],
                           cf["ACCESS_TOKEN"], cf["ACCESS_SECRET"])

    def tweet(self, msg, *img_paths):
        """tweetする

        Args:
            msg (str): ツイートするテキスト
            img_paths(list[string]): アップロードする画像のパス。optional.
        """
        tweet(self.req, msg, *img_paths)


def tweet_image(req, *img_paths):
    """画像をアップロードし、media_idを返す。アップロードのみでツイートはされないので注意。
    ツイートに添付するには、media_idを付けてURLのエンドポイントにPOSTする必要がある。

    Args:
        img_paths (List(str|pathlib.Path)) : 画像のパス（文字列かpathlib.Pathオブジェクト）

    Returns:
        str: media_ids。複数ある場合はカンマで区切られた文字列
    """
    media_ids = []
    for img in img_paths:
        params = {"media": open(img, "rb")}
        data = {"media_category": "tweet_image"}
        res = req.post(URL_IMAGE, files=params, data=data)

        if res.status_code != 200:
            print(f"error at {img}:{res.json()}")
            continue

        res_data = res.json()
        media_ids.append(res_data["media_id"])

    # media_ids_str = ",".join([str(m) for m in media_ids])
    media_ids_str_list = [str(m) for m in media_ids]
    return media_ids_str_list


def tweet(req, msg: str, *img_paths):

    media_ids = tweet_image(req, *img_paths)

    body = {}

    if len(media_ids) > 0:
        body = {"text": msg, "media": {"media_ids": media_ids}}
    else:
        body = {"text": msg}

    res = req.post(URL_TWEET, json=body)

    if not (res.status_code >= 200 and res.status_code <= 299):
        print(f"something went wrong...status:{res.status_code}")

    pprint(res.json())


# tweet("Twitter API v2テスト🚀", "view.JPG")
