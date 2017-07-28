import subprocess
from subprocess import Popen, PIPE
from twilio.rest import Client
import time
import threading
from threading import Thread


MAX_GPU_TEMP = 60
MAX_GPU_CRITICAL_LEVEL=10
MIN_GPU_TEMP = 0

MAX_CPU_TEMP = 60
MAX_CPU_CRITICAL_LEVEL=10
MIN_CPU_TEMP = 0


global SYSTEM_STATUS
SYSTEM_STATUS = True

global GPU_CRITICAL_LEVEL
GPU_CRITICAL_LEVEL = 0

global CPU_CRITICAL_LEVEL
CPU_CRITICAL_LEVEL = 0

#Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = Client(account_sid, auth_token)

def currentGPUTemp():
    while(SYSTEM_STATUS):
        currMachineGPUTemp = subprocess.Popen(['/opt/vc/bin/vcgencmd','measure_temp'],
                                              stdout=PIPE,
                                              stderr=PIPE)
        try:
            currentMachineGPUTemparature, err = currMachineGPUTemp.communicate()
            rc = currMachineGPUTemp.returncode
            time.sleep(10)
            validatecurrentGPUTemp(currentMachineGPUTemparature[5:9])
        except OSError:
            print "Exception occured in subprocess.Popen"

def validatecurrentGPUTemp(GPUTemp):
    if((float(GPUTemp) < float(MIN_GPU_TEMP) or
                float(GPUTemp) >float( MAX_GPU_TEMP))):
        global GPU_CRITICAL_LEVEL
        GPU_CRITICAL_LEVEL=GPU_CRITICAL_LEVEL+1
        if(float(GPU_CRITICAL_LEVEL) < float(MAX_GPU_CRITICAL_LEVEL)):
            createSMSAlert("GPU",GPUTemp)
        else:
            initiateSystemShutdownSequence("GPU")

def currentCPUTemp():
    while (SYSTEM_STATUS):
        currMachineCPUTemp = subprocess.Popen(['cat','/sys/class/thermal/thermal_zone0/temp'],
                                              stdout=PIPE,
                                              stderr=PIPE)
        try:
            currentMachineCPUTemparature, err = currMachineCPUTemp.communicate()
            rc = currMachineCPUTemp.returncode
            time.sleep(10)
            validatecurrentCPUTemp(float(currentMachineCPUTemparature)/1000)
        except OSError:
            print "Exception occured in subprocess.Popen"


def validatecurrentCPUTemp(CPUTemp):
    if ((float(CPUTemp) < float(MIN_CPU_TEMP) or
                 float(CPUTemp) > float(MAX_CPU_TEMP))):
        global CPU_CRITICAL_LEVEL
        CPU_CRITICAL_LEVEL = CPU_CRITICAL_LEVEL + 1
        if (float(CPU_CRITICAL_LEVEL) < float(MAX_CPU_CRITICAL_LEVEL)):
            createSMSAlert("CPU", CPUTemp)
        else:
            initiateSystemShutdownSequence("CPU")

def createSMSAlert(alertParam,alertParamValue):
    tempAlertString = "Alert Machine "+str(alertParam)+" Temparature is " + str(alertParamValue)
    sendSMSAlert(tempAlertString)

def createCriticalSMSAlert(alertParam):
    tempAlertString = str(alertParam)+" OVERHEATED.INITIATING SHUTDOWN SEQUENCE !"
    sendSMSAlert(tempAlertString)

def sendSMSAlert(alertString):
    message = client.messages.create(
        #Contact Number from twilio.com/console
        to="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        from_="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        body=alertString)

def initiateSystemShutdownSequence(alertParam):
    print "initiateSystemShutdownSequence"+str(alertParam)
    createCriticalSMSAlert(alertParam)


def startMonitoring():
    monitoringApplicationThreadspool = []
    GPUTempCheckThread=(Thread(target=currentGPUTemp))
    CPUTempCheckThread = (Thread(target=currentCPUTemp))

    monitoringApplicationThreadspool.append(CPUTempCheckThread)
    monitoringApplicationThreadspool.append(GPUTempCheckThread)


    for eachApplicationThread in monitoringApplicationThreadspool:
        eachApplicationThread.start()
        time.sleep(5)

    for eachApplicationThread in monitoringApplicationThreadspool:
        eachApplicationThread.join()

if __name__ == "__main__":
    startMonitoring()