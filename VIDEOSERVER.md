# Staquaponics - Setup your video server

![staquaponics](assets/Staquaponics.png)
## Requirements

**Hardware:**

- 2go RAM
- sufficient storage disk size

**Languages, tools and frameworks:**


- npm : 10.5.0
- nvm : 0.39.7
- node : 20.12.0
- vite : latest

**Operating system:**

- Any flavour of UNIX supporting **apt** toolset

**Networks**
- A public IP adress
    - or a tunnel to be able to expose an ssh and https service
- A way to connect via ssh

---
# Run this project

Copy the project in your **Video server**

```sh
#mkdir ~/Desktop
cd ~/Desktop
git clone git@github.com:naikibro/staquaponics.git
```

Complete the environment variables with your own data

```sh
cp .env.example .env
```

/!\ see [here]() to find how to fill the .env file /!\


## Complete the .env configuration
```sh
# Servers and connections
LOCAL_NETWORK="192.168.1.1"
VIDEO_SERVER_URL="" #Paste your video server IP adress or public URL
CLOUDFLARE_TUNNEL_TOKEN=""
```

Ensure that the **$SYSTEM_NAME** variables share the same values on the **RASPBERRY** and the **VIDEO SERVER**

## 1 - Run the web server
```sh
cd ~/Desktop/Staquaponics/staquaponics
nohup npm run dev &
```
## 2 - Run the web server on boot
This script will setup the necessary cronjobs for the video server
```sh
cd ~/Desktop/Staquaponics
./scripts/setup_cron.sh -server
```