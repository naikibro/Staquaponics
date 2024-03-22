# Staquaponics - a simple Raspberry pi based timelapse monitoring solution for Aquaponics

This project bundles a bunch of programs and scripts that form a simple and open-source solution to monitor any Aquaponic facility with USB based cameras and Raspberry pi

---

## Requirements

**Hardware:**

- Raspberry pi 4b 8go
- SD card for the raspbian operating system
- any USB camera that is supported by raspbian

**Languages, tools and frameworks:**

- **Ansible :** to automatize the deployment of the environement
- **Docker compose :** to containerize the deployments of the
- Python
- OpenCV
- Cron jobs

**Operating system:**

- Raspbian headless OS image **LTS**

---

## Run this project

Copy the project in your **Raspberry pi**

```sh
git clone git@github.com:naikibro/staquaponics.git
```

Complete the environment variables with your own data

```sh
cp .env.example .env
```

/!\ see [here]() to find how to fill the .env file /!\

---

## Configure your environement

### Paste your ssh public key in the video server

This ensures that your system will have authorization to send files to the server via scp

first create your ssh key if you dont have one

```sh
ssh-keygen -t rsa -b 4096
```

Then copy your public key into your video server

```sh
ssh-copy-id username@your_vps_ip
```

### Build or fetch the armv7 docker cloudflare image ( optionnal )
```sh
git clone -b feature/support-armhf git@github.com:jeankhawand/cloudflared.git 
```
and then cd into project dir and run the following command:


```sh
docker build . -t junni/cloudflared:arm
```

## 3 - Configure your Cloudflare tunnel
Find how to setup your cloudflare tunnel [here](https://www.youtube.com/watch?v=ey4u7OUAF3c)

```sh
docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token your-cloudfare-tunnel-token
```
if your raspberry pi is on armv7 architecture
```sh
docker run -d junni/cloudflared:arm tunnel --no-autoupdate run --token your-cloudfare-tunnel-token
```


