# motor-simulator

This repository includes source code for a simulator of the temperature measurement of a motor, coupled with a human machine interface (HMI) which animates the motor circuit, allowing its operation by using push buttons, and has the possibility to simulate fault conditions.

It is possible to choose the threshold and hysteresis of the temperature alarm. The temperature measurement is simulated by discrete values which are plotted in the HMI. 

There is a push button to start the motor in forward direction, a push button for reverse direction, and a push button to stop the motor. Tere are indicators for the forward and reverse movement of the motor. The motor circuit also has a circuit  breaker that must be closed in order to energize the motor.

A fan is switched on automatically to cool the motor if the temperature exceeds a user-defined threshold. The fan is switched  off automatically if the temperature falls below a second level of temperature defined by a hysteresis value.

A small demonstration of the GUI can be seen at http://louro.xyz/video_operation.mp4.
