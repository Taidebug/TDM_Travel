import requests

def authenticate(api_key, email, password, sign_up=False):
    action = "signUp" if sign_up else "signInWithPassword"

    url = (
        "https://identitytoolkit.googleapis.com/v1/"
        f"accounts:{action}"
    )

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    try:
        response = requests.post(
            url,
            params={"key": api_key},
            json=payload,
            timeout=20
        )
    except requests.RequestException:
        raise ValueError("Cannot connect with Firebase.") from None

    if response.status_code != 200:
        error_message = response.json().get("error", {}).get(
            "message", "UNKNOWN_ERROR"
        )
        raise ValueError(f"Firebase: {error_message}")

    data = response.json()

    if not data.get("email") or not data.get("idToken"):
        raise ValueError("Firebase returned invalid account data.")

    return data