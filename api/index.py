
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
@app.route("/apis")
@app.route("/api/apis")
def handler():
    return jsonify({

        # ───────────────────────── VERCEL ─────────────────────────

        "PROXY_API": "https://new-proxis-api.vercel.app",

        "YOUTUBE_DOWNLOAD": "https://scammer-yt-api.vercel.app/api/download",

        "DASH_MPD_KEYS": "https://dash-mpd-keys-steel.vercel.app/getmpdkeys",

        "CW_KEYS_MPD": "https://cw1-keys-mpd.vercel.app/getmpdkeys_n",

        "ABHINAY_KEYS": "https://scammer-abhinay-keys-mpd.vercel.app/getmpdkeys",

        "CP_KEYS": "https://new1-scammer-keys-cp.vercel.app/api",

        "VDO_CIPHER_KEYS": "https://the-new-1vdo-cipher-drm-keys-scammer.vercel.app/",

        "SIGN_URL": "https://scammer1-sign-url.vercel.app/get_signed_url",

        "URL_CHANGE": "https://scammer-url-change.vercel.app/process",

        "ZOOM_API": "https://new1-scammer-zoom-api.vercel.app/api/get-mp4",


        # ───────────────────────── HEROKU ─────────────────────────

        "YOUTUBE_COOKIES_API": "https://saasfetcher-019640c70a50.herokuapp.com/api/cookies/youtube",

        "PW_DRM_KEYS": "https://pw-drm-keys-2026-8b1e66d19e8e.herokuapp.com/api/get-keys",

        "PW_BATCH_API": "https://dams-wo2435-ad5c42cb984d.herokuapp.com/",

        "CW_UTK_API": "https://cw-ut-api-new12-d02715c196d3.herokuapp.com/api/vid-details",

        "APPX_ZIP_DL": "https://zip-keys-final-b590a908debc.herokuapp.com/api/keys",

        "VID_CRYPT_KEYS": "https://vid-crypt-keys1423-dfd8a00fa048.herokuapp.com",

        "ZIP_CK_API": "https://appx-zip-keys-from-url-74ecc79db841.herokuapp.com",

        "PW_EXTRACTOR_API": "https://pw-extractorpoa-102-826cb392ce3c.herokuapp.com",

        "CW_MERGED_API": "https://cw-merged-api1231-5d0ec8742491.herokuapp.com",

        "DAMS_EXTRACTOR_API": "https://dams-wo2435-ad5c42cb984d.herokuapp.com",

        "APPX_EXTRACTOR_API": "https://appx-sign-urls-tess-3ff967eda6fc.herokuapp.com",

        "VID_CRYPT_API" : "https://vid-crypt-ext-api41-37df80a4bb82.herokuapp.com",


        # ───────────────────────── EXTRACTOR APIS ─────────────────────────

        "ADDA247_API":              "https://adda247api.vercel.app",
        "APPX_VIDS_API":            "https://api-for-appx-vids.vercel.app",
        "CW_VID_API":               "https://cw-vid.vercel.app",
        "CW_KOYEB_MAIN":            "https://troubled-ranee-scambot8-4f45ea5a12345.koyeb.app/api",
        "CW_KOYEB_NOTES":           "https://silly-lorrayne-scammerbots3-a6bebe0e.koyeb.app",
        "CW_KOYEB_PDF":             "https://yeasty-mufi-scammerbotscw1-ba766b94.koyeb.app",
        "KHAN_EX_API":              "https://scammer-khan-ex-api.vercel.app",
        "RWA_WITHOUT_API":          "https://rwa-without-api.vercel.app",
        "SELECTION_WAY_API":        "https://selection-way.vercel.app",
        "STUDY_IQ_API":             "https://study-iq-wo.vercel.app",
        "APNA_COLLEGE_API":         "https://apna-collage-data-api.vercel.app",
        "FUTURE_KUL_API":           "https://db-txts.vercel.app",


        # ───────────────────────── OTHER ─────────────────────────

        "VPS_PROXY_URL": "http://myuser:utkarsh1234@217.216.78.69:3128"
    })


if __name__ == "__main__":
    app.run()



# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")
# @app.route("/apis")
# @app.route("/api/apis")
# def handler():
#     return jsonify({
#             "PROXY_API": "https://new-proxis-api.vercel.app",
#             "YOUTUBE_DOWNLOAD": "https://scammer-yt-api.vercel.app/api/download",
#             "YOUTUBE_COOKIES_API": "https://saasfetcher-019640c70a50.herokuapp.com/api/cookies/youtube",
#             "DASH_MPD_KEYS": "https://dash-mpd-keys-steel.vercel.app/getmpdkeys",
#             "CW_KEYS_MPD": "https://cw1-keys-mpd.vercel.app/getmpdkeys_n",
#             "ABHINAY_KEYS": "https://scammer-abhinay-keys-mpd.vercel.app/getmpdkeys",
#             "CP_KEYS": "https://new1-scammer-keys-cp.vercel.app/api",
#             "VDO_CIPHER_KEYS": "https://the-new-1vdo-cipher-drm-keys-scammer.vercel.app/",
#             "PW_DRM_KEYS": "https://pw-drm-keys1-9aaec2321ffe.herokuapp.com/api/get-keys",
#             "PW_BATCH_API": "https://dams-delhi-wo-api-c27c3bd71235.herokuapp.com/",
#             "CW_UTK_API": "https://cw-ut-test-new-a38f2e64c415.herokuapp.com/api/vid-details",
#             "SIGN_URL": "https://scammer1-sign-url.vercel.app/get_signed_url",
#             "URL_CHANGE": "https://scammer-url-change.vercel.app/process",
#             "ZOOM_API": "https://new1-scammer-zoom-api.vercel.app/api/get-mp4",
#             "APPX_ZIP_DL": "https://final-zip-keys12-0703e8085255.herokuapp.com/api/keys",
#             "VID_CRYPT_KEYS" : "https://vid-crypt-keys12-60e49b6456e3.herokuapp.com",
#             "VPS_PROXY_URL" : "http://myuser:utkarsh1234@217.216.78.69:3128",
#             "ZIP_CK_API" : "https://appx-zip-keys-frm-zip-80aa3cd2a40f.herokuapp.com",
#             "PW_EXTRACTOR_API" : "https://pw-extractor-apiq-0b02d21c398a.herokuapp.com",
#             "CW_MERGED_API" : "https://cw-merged-api123-208337e372ec.herokuapp.com",
#             "DAMS_EXTRACTOR_API" : "https://dams-delhi-wo-api-c27c3bd71235.herokuapp.com",
#             "APPX_EXTRACTOR_API" : "https://appx-sign-urls-h-11cdc3889ea1.herokuapp.com"
#         })


