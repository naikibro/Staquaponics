# This script shall prompt the user to choose default settings of the project
clear

function setup_project {
    echo ""
    echo "----- S E T U P - P R O J E C T -----"
    echo ""
}

function next_step {
        echo ""
        read -p "Press Enter to continue generation..."
        clear
}

function install_dependencies {
    sudo apt install -y net-tools 
}

function status_check {
    clear
    echo "project has been initialized"

    echo ""
    echo "----- E N V -----"
    echo ""

    cat .env.example

    echo ""
    echo "----- C R O N J O B S -----"
    echo ""

    echo "All background tasks are now running"
    echo ""
    echo "to see the list of running tasks, run : crontab -l "
}

# Setup
    setup_project
    echo "    --- L I B R A R I E S ---"
    install_dependencies
    next_step

# Devices
    setup_project
    echo "    --- D E V I C E S ---"
    
    # choose CAMERA_ADRESS from `lsusb -v`: default to None
        #.then(in .env CAMERA_ADRESS = device_usb_id )
        #.None(.env CAMERA_ADRESS = None )

    # choose CAMERA_TYPE ( defaults to USB ) from:
        # [ USB, PCIE, IP, None ] 
        # prompt the user to choose
    
    # set NUMBER_OF_CAMERAS ( defaults to 0 ): 
        # if CAMERA_ADRESS != None, set to 1
    
    # set NUMBER_OF_DEVICES ( devices on the same network ) based on the arp table

    next_step

# Files and folders structure

    setup_project
    echo "    --- B A C K U P - F O L D E R ---"

    # choose BACKUP_FOLDER from:
        # choose the disk where to store the BACKUP_FOLDER
            # prompt the user to choose from all available disks ( USB and SATA )
        # choose the path on the chosen disk where to store the BACKUP
            #.then( BACKUP_FOLDER = the result of my choice)
    next_step

# Servers and connections
    setup_project
    echo "    --- N E T W O R K - S E T U P ---"
    # choose local SSID for LOCAL_NETWORK
        #.then(ping)
        #.catch()

    # prompt VIDEO_SERVER_URL
        #.then(ping)
        #.catch()
    next_step

# Automate the jobs
    setup_project
    echo "    --- C R O N - J O B S ---"
    next_step

status_check
echo ""