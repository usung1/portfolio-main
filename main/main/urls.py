"""
attrib +r ~/.ssh/uss-portfolio.pem
scp -i ~/.ssh/uss-portfolio.pem -r MyResume ubuntu@18.217.252.24:/home/ubuntu
ssh -i ~/.ssh/uss-portfolio.pem ec2-user@18.217.252.24
pip install 'django<5' 'pillow<10' 'django-admin-thumbnails<0.3'


ssh -i ~/django-portfolio-key.pem ubuntu@3.37.197.249 rm -r /home/ubuntu/MyResume/MyPortfolio
scp -i ~/django-portfolio-key.pem -r MyPortfolio-media ubuntu@3.37.197.249:/home/ubuntu/MyResume

/MyResume/MyPortfolio/PortfolioA/posts
scp -i ~/django-portfolio-key.pem -r MyPortfolio ubuntu@3.37.197.249:/home/ubuntu/MyResume
ssh -i ~/django-portfolio-key.pem ubuntu@3.37.197.249 rm -r /home/ubuntu/MyResume/MyPortfolio
nohup python3 manage.py runserver 0:80 &
pkill -9 python3
 ec2-18-217-252-24.us-east-2.compute.amazonaws.com

ssh -i ~/.ssh/uss-portfolio.pem ec2-user@18.217.252.24
scp -i ~/.ssh/uss-portfolio.pem -r main ec2-user@18.217.252.24:/home/ec2-user/portfolio
nohup python3 manage.py runserver 0.0.0.0:8000 &

ssh -i ~/.ssh/uss-portfolio.pem ec2-user@18.217.252.24
scp -i ~/.ssh/uss-portfolio.pem -r main/requirements.txt ec2-user@18.217.252.24:/home/ec2-user/portfolio/main
pip install --user -r requirements.txt

레드햇 설치패키지 yum
우분투 설치패키지 apm

"""