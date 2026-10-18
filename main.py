import json
import urllib.request
import urllib.error
import time

TOKEN = "توکن_جدید_ربات_را_اینجا_بگذار"
API = f"https://botapi.rubika.ir/v3/{TOKEN}/"

def call_api(method, data=None):
    body = json.dumps(data or {}).encode("utf-8")
    req = urllib.request.Request(
        API + method,
        data=body,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def main():
    offset = None
    print("Takpar Guard started")

    while True:
        try:
            data = {"limit": 20}
            if offset is not None:
                data["offset_id"] = offset

            result = call_api("getUpdates", data)

            for update in result.get("data", {}).get("updates", []):
                offset = update.get("update_id", offset)
                print(update)

            time.sleep(1)

        except Exception as e:
            print("Error:", e)
            time.sleep(5)

if __name__ == "__main__":
    main()
