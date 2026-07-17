from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/apis")
@app.route("/api/apis")
def handler():
    return jsonify({
            "PROXY_API": "https://new-proxis-api.vercel.app",
            "YOUTUBE_DOWNLOAD": "https://scammer-yt-api.vercel.app/api/download",
            "YOUTUBE_COOKIES_API": "https://saasfetcher-019640c70a50.herokuapp.com/api/cookies/youtube",
            "DASH_MPD_KEYS": "https://dash-mpd-keys-steel.vercel.app/getmpdkeys",
            "CW_KEYS_MPD": "https://cw1-keys-mpd.vercel.app/getmpdkeys_n",
            "ABHINAY_KEYS": "https://scammer-abhinay-keys-mpd.vercel.app/getmpdkeys",
            "CP_KEYS": "https://new1-scammer-keys-cp.vercel.app/api",
            "VDO_CIPHER_KEYS": "https://the-new-1vdo-cipher-drm-keys-scammer.vercel.app/",
            "PW_DRM_KEYS": "https://pw-drm-keys1-9aaec2321ffe.herokuapp.com/api/get-keys",
            "PW_BATCH_API": "https://dams-wo-api-a83b422e50e7.herokuapp.com/",
            "CW_UTK_API": "https://cw-vid-data-58b3e39c266f.herokuapp.com/api/vid-details",
            "SIGN_URL": "https://scammer1-sign-url.vercel.app/get_signed_url",
            "URL_CHANGE": "https://scammer-url-change.vercel.app/process",
            "ZOOM_API": "https://new1-scammer-zoom-api.vercel.app/api/get-mp4",
            "APPX_ZIP_DL": "https://scammer-final-zip-keys-4b04092f3917.herokuapp.com/api/keys",
            "VID_CRYPT_KEYS" : "https://vid-crypt-keys1-ac44f9462407.herokuapp.com"
        })


