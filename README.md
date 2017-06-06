# PSD controller

Design of the **PSD controller** as a **PID** controller for discrete digital systems.

Compared to the **integration** and **derivation** of continuous regulators, these operations in **PSD** are replaced by the **summation** and **difference** of the error value of the individual states.



---

## Usage

### Import
```
from psd.py import PSD
```
### Initialization
```
mypsd = PSD(P=30, S=600, D=40, sumMAX = 200)
```
### Set time sample
```
mypsd.setTimeSample(mytimesample)
```
### Setpoint update
```
mypsd.setPoint(newSetpoint)
```
### Update Output
```
output = mypsd.update(process_variable)
```
### Reset full PSD
```
mypsd.reset()
```

---