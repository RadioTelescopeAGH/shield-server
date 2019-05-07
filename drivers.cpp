#include <iostream>
#include <wiringPi.h>
#include <softPwm.h>
#include <thread>
using namespace std;

// #define LED 0 matches with ASUS_GPIO 164! This can be checked with command 'sudo gpio readall'.
struct Position {
	float phi, theta;
};
class Motors {
public:
	const int MotorAPWM = 0;
	const int MotorA0 = 2;
	const int MotorA1 = 3;

	const int MotorBPWM = 12;
	const int MotorB0 = 13;
	const int MotorB1 = 14;

	std::thread execution;
	bool shutdown = false;

	Position target;
	Position current;
	bool moveA = false;
	bool moveB = false;

	const float epsilon = 1e-5;

	Motors(){
		wiringPiSetup ();
		pinMode (MotorAPWM, OUTPUT);
		softPwmCreate(MotorAPWM, 0, 100);
		pinMode (MotorA0, OUTPUT);
		pinMode (MotorA1, OUTPUT);

		pinMode (MotorBPWM, OUTPUT);
		softPwmCreate(MotorBPWM, 0, 100);
		pinMode (MotorB0, OUTPUT);
		pinMode (MotorB1, OUTPUT);
		execution = std::thread(&Motors::loop,this);
	}
	~Motors(){
		shutdown = true;
		execution.join();
	}
	void stop(){
		target = current;
		moveA = moveB = false;
		softPwmWrite(MotorAPWM, 100); 
		softPwmWrite(MotorBPWM, 100); 
		digitalWrite (MotorA0, HIGH);
		digitalWrite (MotorA1, HIGH);
		digitalWrite (MotorB0, HIGH);
		digitalWrite (MotorB1, HIGH);
	}
	void sendTarget(Position pos){
		softPwmWrite(MotorAPWM, 100); 
		softPwmWrite(MotorBPWM, 100); 
		target = pos;
		moveA = moveB = true;

	}
private:
	void loop(){
		while(!shutdown){
			if(moveA or moveB){
				float dPhi = target.phi - current.phi;
				float dTheta = target.theta - current.theta;
				if(dPhi < epsilon){
					digitalWrite (MotorA0, LOW);
					digitalWrite (MotorA1, LOW);
					moveA = false;
				}
				if(dTheta < epsilon){
					digitalWrite (MotorB0, LOW);
					digitalWrite (MotorB1, LOW);
					moveB = false;
				}
				if(moveA){
					if(dPhi > 0){
						digitalWrite (MotorA0, HIGH);
						digitalWrite (MotorA1, LOW);
					}
					else {
						digitalWrite (MotorA0, LOW);
						digitalWrite (MotorA1, HIGH);
					}
					softPwmWrite(MotorAPWM, getSpeed(dPhi)); 
				}
				if(moveB){
					if(dTheta > 0){
						digitalWrite (MotorB0, HIGH);
						digitalWrite (MotorB1, LOW);
					}
					else {
						digitalWrite (MotorB0, LOW);
						digitalWrite (MotorB1, HIGH);
					}
					softPwmWrite(MotorBPWM, getSpeed(dTheta)); 
				}
				delay(20);
			}
			else {
				delay(250);
			} 
		}
	}
	int getSpeed(float dx){
		return 75;
	}

};

int main (void)
{
	Motors motors;
	for (;;)
	{
		digitalWrite (motors.MotorA0, HIGH);
		digitalWrite (motors.MotorA1, LOW);
				digitalWrite (motors.MotorB0, LOW);
		digitalWrite (motors.MotorB1, LOW);
		cout << "tik"<< endl;

		for(int i  = 0; i <= 200; i++){
			softPwmWrite(motors.MotorAPWM, abs(100 - i)); 
			delay (1);

		}
		digitalWrite (motors.MotorA0, LOW);
		digitalWrite (motors.MotorA1, HIGH);
		digitalWrite (motors.MotorB0, LOW);
		digitalWrite (motors.MotorB1, LOW);
		cout << "tok"<< endl;
		for(int i  = 0; i <= 200; i++){
			softPwmWrite(motors.MotorAPWM, abs(100 - i)); 
			delay (1);
		}
				digitalWrite (motors.MotorA0, LOW);
		digitalWrite (motors.MotorA1, LOW);
		digitalWrite (motors.MotorB0, HIGH);
		digitalWrite (motors.MotorB1, LOW);
			for(int i  = 0; i <= 200; i++){
			softPwmWrite(motors.MotorAPWM, abs(100 - i)); 
			delay (1);
		}
				digitalWrite (motors.MotorA0, LOW);
		digitalWrite (motors.MotorA1, LOW);
		digitalWrite (motors.MotorB0, LOW);
		digitalWrite (motors.MotorB1, HIGH);
			for(int i  = 0; i <= 200; i++){
			softPwmWrite(motors.MotorAPWM, abs(100 - i)); 
			delay (1);
		}
				digitalWrite (motors.MotorA0, LOW);
		digitalWrite (motors.MotorA1, LOW);
		digitalWrite (motors.MotorB0, LOW);
		digitalWrite (motors.MotorB1, LOW);
			for(int i  = 0; i <= 400; i++){
			softPwmWrite(motors.MotorAPWM, abs(100 - i)); 
			delay (1);
		}
	}
    return 0;
}
