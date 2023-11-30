import requests
import time

def check_subdomain_status(subdomain):
  try:
    response = requests.get(subdomain)
    if response.status_code == 200:
      return "Up"
    else:
      return "Down"
  except requests.exceptions.RequestException as e:
    return "Down"

def main():
  subdomains = ["https://google.com", "https://facebook.com", "https://vlearnv.herovired.com/"]
  print("Status of subdomains:")
  print("------------------------------------------")
  print("Subdomain".ljust(30), "Status".ljust(10))
  while True:
    for subdomain in subdomains:
      status = check_subdomain_status(subdomain)
      print(subdomain.ljust(30), status.ljust(10))

    time.sleep(60)

if __name__ == "__main__":
  main()