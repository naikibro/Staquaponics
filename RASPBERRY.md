<<<<<<< HEAD
# Staquaponics - Setup your Raspberry pi
![staquaponics](assets/Staquaponics.png)

## Requirements

**Hardware:**

- Raspberry 3b+ 8go
- 32go Micro SD

**Languages, tools and frameworks:**

- npm : 10.5.0
- nvm : 0.39.7
- node : 20.12.0
- vite : latest

**Operating system:**

- Raspbian headless LTS latest image
    - or any flavour of UNIX supporting **apt** toolset

**Networks**  
- **Required**
    - internet connection
    - local ssh
- **Optionnal**
    - ssh tunnel
    - https tunnel

---
# Run this project

Copy the project in your **Raspberry pi**

```sh
#mkdir ~/Desktop
cd ~/Desktop
git clone git@github.com:naikibro/staquaponics.git
```

Complete the environment variables with your own data

```sh
cp .env.example .env
```

/!\ see [here](#0---complete-the-env-configuration) to find how to fill the .env file /!\

## 0 - Complete the .env configuration
```sh
# Servers and connections
LOCAL_NETWORK="192.168.1.1"
VIDEO_SERVER_URL="" #Paste your video server IP adress or public URL
CLOUDFLARE_TUNNEL_TOKEN=""
```
=======

# Configure your Raspberry pi environement

>>>>>>> f7c726226b7f9c0a92977c79c4d0e510be8cd0e9
## 1 - Install all dependencies

just run the magic script
```sh
./scripts/setup.sh
```

This script should install:
- docker
- node
- npm
- nvm
- scp
- apt get
- ffmpeg
- python
- opencv

***
## 2 - Paste your ssh public key in the video server

This ensures that your system will have authorization to send files to the server via scp

first create your ssh key if you dont have one

```sh
ssh-keygen -t rsa -b 4096
```

Then copy your public key into your video server

```sh
ssh-copy-id username@your_video_server_url_or_ip
```

## 3 - Configure your Cloudflare tunnel
Find how to setup your cloudflare tunnel [here](https://www.youtube.com/watch?v=ey4u7OUAF3c)

```sh
docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token your-cloudfare-tunnel-token
```

### if your raspberry pi is on armv7 architecture

```sh
git clone -b feature/support-armhf git@github.com:jeankhawand/cloudflared.git 
```

```sh
docker build . -t junni/cloudflared:arm
```

```sh
docker run -d junni/cloudflared:arm tunnel --no-autoupdate run --token your-cloudfare-tunnel-token
```

### Simplified docker compose images
Once you have fetched and built the cloudflare image that corresponds to your architecture, you can run the [docker-compose.yml](docker-compose.yml) file 

/!\ Dont forget to specify the image you want to use /!\
```sh
docker compose up -d
```
## 4 - Configure the cron jobs
Launch this script to launch the Staquaponics application globally

```sh
./scripts/setup_cron.sh
```
This script should create the required jobs to: 
- every 15 minutes from 6am to 6pm : take a photo
- at the end of the day : compile the video
- then : send the video to server
- then : flush the data produced on this day
