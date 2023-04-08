# Pytweet

Tweet用モジュール。Twitter API V2対応。

## これは何ですか？

PythonでTweetするモジュールです。

対応しているエンドポイントは、2023.04.05時点で以下の通りです。

- ```https://api.twitter.com/2/tweets```

メディアアップロードも出来ますが、V2版はまだリリースされていません。公式案内のとおり、旧API(V1.1)を利用しています。 リリースされ次第対応します。

## いつ使いますか？

テキストのみのTweetしたいとき、画像付きでツイートしたいとき。

## どう使いますか？

### Twitterの認情報をjson形式でファイルに保存します。

```json
{
  "API_KEY": "MY-API-KEY",
  "API_SECRET": "MY-API-SECRET",
  "BEARER": "MY-BEARER",
  "ACCESS_TOKEN": "MY-ACCESS-TOKEN",
  "ACCESS_SECRET": "MY-ACCESS-SECRET"
}
```

### ツイートしたいプロジェクトの直下にgit cloneします。

プロジェクトのほうでは`pytweet/`を.gitignoreしておくと良いです。

```git
git clone ~~~~
```

### importして使います。

```python
from pytweet import Pytweet

twitter = Pytweet("path-to-your-twitter-credential-file")

# tweet with text only
twitter.tweet("hello,world!")

# tweet with images
twitter.tweet("hello,world","path-to-img1",...,"path-to-img4")
```