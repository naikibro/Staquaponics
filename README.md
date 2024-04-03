# Staquaponics - a simple Raspberry pi based timelapse monitoring solution for Aquaponics

This project bundles a bunch of programs and scripts that form a simple and open-source solution to monitor any Aquaponic facility with USB based cameras and Raspberry pi

---

## Requirements

**Hardware:**

- Raspberry pi 4b 8go
- SD card for the raspbian operating system
- any USB camera that is supported by raspbian

**Languages, tools and frameworks:**


- **Docker compose :** to containerize the deployments of the services
- **Python :** for scripts and openCV
- **OpenCV :** for imaging purposes
- **Cron jobs :** automating our jobs

**Operating system:**

- Raspbian headless OS image **LTS**
- or any flavour of Ubuntu above **18.04**

---
# Architecture
This project is a monorepo

It contains a subrepo for the [webserver](staquaponics)  
And all the scripts necessary in the [scripts](scripts) folder

## Run this project

Copy the project in your **Raspberry pi**

```sh
cd ~/Desktop
git clone git@github.com:naikibro/staquaponics.git
```

Complete the environment variables with your own data

```sh
cp .env.example .env
```

/!\ see [here]() to find how to fill the .env file /!\

---
# Configure your raspberry pi
Find out how to setup your raspberry pi [here](RASPBERRY.md)