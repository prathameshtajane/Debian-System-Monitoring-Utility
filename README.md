# Debian-System-Monitoring-Utility

Debian System monitoring utility makes it easy to monitor different system parameters of any Debian based operating system like Raspbian with absolute minimum fuss.This fully customized monitoring utility allows users to decide the threshold value for different system parameters and sends text alerts to the admin user if the system parameter crosses the threshold value decided by the user.If the admin user fails to bring it below the threshold value within stipulated time(which is customized too),this utility initiates predefined commands stream in order to avoid the system being crashed.This fully optimized utility is developed in Python 2.7.10 to keep the resource requirement for the utility to the minimum.

##Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

####Signing Up for a Twilio Account 
To enable text alerts admin user have to sign up for the free Twilio service.Twilio is an SMS gateway service,  it’s a service that allows this utility to send text   alerts.The free trial is indefinite; you won’t have to upgrade to a paid plan later.
#####Steps to create free Twilio Account :
1. Go to http://twilio.com/ and fill out the sign-up form.
2.  Once you’ve signed up for a new account, you’ll need to verify a mobile phone number that you want to send texts to.
3. After receiving the text with the verification number, enter it into the Twilio website to prove that you own the mobile phone you are verifying. 
4. You will now be able to send texts to this phone number using the twilio module. 
5. Twilio provides your trial account with a phone number to use as the sender of text messages. 
6. You will need two more pieces of information: your account SID and the auth (authentication) token. 
7. You can find this information on the Dashboard page when you are logged in to your Twilio account.

####Python Modules 
1. <a href=“https://docs.python.org/2/library/subprocess.html”>Subprocess Package</a>
2. <a href=“https://docs.python.org/2/library/time.html”>Time Package</a>
3. <a href=“https://docs.python.org/2/library/threading.html”>threading package</a>
4. <a href=“https://www.twilio.com/docs/quickstart/python/devenvironment#installing-virtualenv-with-python-24”>twilio.rest </a>

##Text Alert Snapshots
![picture alt](https://drive.google.com/file/d/0BzeLZmI8HMAwSU5PSkJYYmJhQ3c/view?usp=sharing “Snapshot 1”)
![picture alt](https://drive.google.com/file/d/0BzeLZmI8HMAwOE1VdVlvczNGXzQ/view?usp=sharing “Snapshot 2”)

##Launching the Utility
```
python systemMonitoringUtility.py
```

##Versioning
We use <a href=“http://semver.org/”>SemVer</a> for versioning. For the versions available, see the <a href=“https://github.com/prathameshtajane/Debian-System-Monitoring-Utility/releases”>tags on this repository.</a>

##Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

##Reference
1. <a href=“https://www.twilio.com/docs/”>Twilio api reference document.</a>

##Contributors
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

##Authors
<a href=“linkedin.com/in/prathamesh-tajane”>Prathamesh Tajane </a>
See also the list of <a href=“https://github.com/prathameshtajane/Debian-System-Monitoring-Utility/graphs/contributors”>contributors</a> who participated in this project.

##License
This project is licensed under the MIT License - see the LICENSE.md file for details
