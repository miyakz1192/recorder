set -x

ADVSVCHOME=~/recorder

cd /etc/systemd/system 
sudo rm httpd_server.service
sudo rm recorder.service
sudo ln -s ${ADVSVCHOME}/etc/httpd_server.service httpd_server.service
sudo ln -s ${ADVSVCHOME}/etc/recorder.service recorder.service

sudo systemctl enable httpd_server.service
sudo systemctl enable recorder.service

