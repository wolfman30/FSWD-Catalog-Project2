Used this [guide](https://docs.google.com/document/d/e/2PACX-1vT7XPf0O3oLCACjKEaRVc_Z-nNoG6_ssRoo_Mai5Ce6qFK_v7PpR1lxmudIOqzKo2asKOc89WC-qpfG/pub?embedded=true) from Udacity to complete this with a Windows 10 o.s.:

Step 1:

Download & install [Git](https://git-scm.com/downloads). You need this to install Vagrant and VirtualBox

Step 2:

(a) Download & install [Vagrant](https://www.vagrantup.com/downloads.html)
(b) Download & install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

These enable you to create a linux virtual machine. 

Step 3: Clone fullstack-udacity-vm by running the following command in your Git bash terminal:

    git clone https://github.com/udacity/fullstack-nanodegree-vm.git

Step 4: Cd into 'fullstack', then cd into 'vagrant'

Step 5: Run:

    vagrant up

Step 6: After every loads successfully (may take a hot minute), run:

    vagrant ssh

Step 7: After this operation completes, cd into '/vagrant'

Step 8: Run 'ls' to see the folders. You should see 'catalog' as one. Cd into 'catalog'

Step 9: Clone my repo inside 'catalog':

    git clone https://github.com/wolfman30/FSWD-Catalog-Project2.git

Step 10: Run:

    python app.py

Step 11:

Open a web browser. Type in 'http://localhost8000/'. If you use Chrome you can omit 'http://'
