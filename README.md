git clone https://github.com/284267/telegram-auto-checkin.git
cd telegram-auto-checkin
pip3 install -r requirements.txt
cp config_template.py config.py
nano config.py
python3 tgqd.py
