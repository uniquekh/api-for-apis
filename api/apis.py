from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        apis = {
            "pw-extractor-api": "https://pw-api-scammer-ext-4c2ed44fc094.herokuapp.com",
                # Proxy & ScraperAPI
                "PROXY_API": "https://proxis-api.vercel.app/api/proxies",
                
                # YouTube
                "YOUTUBE_DOWNLOAD": "https://scammer-yt-api.vercel.app/api/download",
                
                # DRM Keys APIs
                "DASH_MPD_KEYS": "https://dash-mpd-keys.vercel.app/getmpdkeys",
                "CW_KEYS_MPD": "https://cw-keys-mpd.vercel.app/getmpdkeys_n",
                "ABHINAY_KEYS": "https://abhinay-keys-mpd.vercel.app/getmpdkeys",
                "CP_KEYS": "https://scammer-keys-cp.vercel.app/api",
                "VDO_CIPHER_KEYS": "https://vdo-cipher-drm-keys-scammer.vercel.app/",
                "PW_DRM_KEYS": "https://scammer-pw-drm-keys.vercel.app/api/get-keys",
                
                # PW Batch API
                "PW_BATCH_API": "https://pw-api-scammer-batches-14b67eddd153.herokuapp.com/api/batch",
                
                # ClassWill API
                "CW_UTK_API": "https://cw-ut-api-0d37b991d272.herokuapp.com/api/vid-details",
                
                # URL Processing
                "SIGN_URL": "https://sign-url.vercel.app/get_signed_url",
                "URL_CHANGE": "https://url-change.vercel.app/process",
                "ZOOM_API": "https://scammer-zoom-api.vercel.app/api/get-mp4",

        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(apis).encode())
        return


