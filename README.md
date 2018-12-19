Used this [guide](https://docs.google.com/document/d/e/2PACX-1vT7XPf0O3oLCACjKEaRVc_Z-nNoG6_ssRoo_Mai5Ce6qFK_v7PpR1lxmudIOqzKo2asKOc89WC-qpfG/pub?embedded=true) from Udacity to complete this project with a Windows 10 o.s.:

Step 1:

Download & install [Git](https://git-scm.com/downloads). You need this to install Vagrant and VirtualBox

Step 2: in the Git Bash terminal do the following: 

(a) Download & install [Vagrant](https://www.vagrantup.com/downloads.html)
(b) Download & install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

These enable you to create a linux virtual machine. 

Step 3: Clone fullstack-udacity-vm by running the following command in your Git bash terminal:

    git clone https://github.com/udacity/fullstack-nanodegree-vm.git

Step 4: Cd into 'fullstack', then cd into 'vagrant'

Step 5: Ensure Hyper-V is disabled so VirtualBox can do its job with Vagrant: 
    
    (a) Type 'powershell' in Windows Search --> right click powershell ---> run as administrator --> copy and paste 'Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All' (without the quotes) --> Press Enter --> Restart computer

Step 6: In the 'fullstack-nanodegree-vm/vagrant' folder run the following:

    vagrant up

Step 7: After every loads successfully (may take a hot minute), run:

    vagrant ssh

Step 8: After this operation completes, cd into '/vagrant'

Step 9: Install pip

Step 10: Install flask

Step 11: Install sqlalchemy

Step 12: Run 'ls' to see the folders. You should see 'catalog' as one. Cd into 'catalog'

Step 13: Clone my repo inside 'catalog':

    git clone https://github.com/wolfman30/FSWD-Catalog-Project2.git

Step 14: Run:

    python app.py

Step 15:

Open a web browser. Type in 'http://localhost8000/'. If you use Chrome you can omit 'http://'
