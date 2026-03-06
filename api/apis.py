from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        apis = {
                # Proxy & ScraperAPI
                "PROXY_API": "https://new-proxis-api.vercel.app",
                
                # YouTube
                "YOUTUBE_DOWNLOAD": "https://scammer-yt-api.vercel.app/api/download",
                "YOUTUBE_COOKIES_API": "https://saasfetcher-019640c70a50.herokuapp.com/api/cookies/youtube",
                
                # DRM Keys APIs
                "DASH_MPD_KEYS": "https://dash-mpd-keys-steel.vercel.app/getmpdkeys",
                "CW_KEYS_MPD": "https://cw1-keys-mpd.vercel.app/getmpdkeys_n",
                "ABHINAY_KEYS": "https://scammer-abhinay-keys-mpd.vercel.app/getmpdkeys",
                "CP_KEYS": "https://new1-scammer-keys-cp.vercel.app/api",
                "VDO_CIPHER_KEYS": "https://the-new-1vdo-cipher-drm-keys-scammer.vercel.app/",
                "PW_DRM_KEYS": "https://pw-drm-mpd-keys-40136ae2ba5f.herokuapp.com/api/get-keys",
                
                # PW Batch API
                "PW_BATCH_API": "https://pw-batches-scammer-47d558a1f504.herokuapp.com/api/batch",
                
                # ClassWill API
                "CW_UTK_API": "https://cw-ut-api.vercel.app/api/vid-details",
                
                # URL Processing
                "SIGN_URL": "https://scammer1-sign-url.vercel.app/get_signed_url",
                "URL_CHANGE": "https://scammer-url-change.vercel.app/process",
                "ZOOM_API": "https://new1-scammer-zoom-api.vercel.app/api/get-mp4",

        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(apis).encode())
        return









