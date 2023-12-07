int led1 = 13; //first we should define all pins 
int led2 = 12;
int  led3 = 11;
int led4 = 10;
int led5 = 9;
int led6 = 8;

int speed = 200;

void  setup() {
// put your setup code here, to run once:
// secondly we should  deside if the are output or input and of course led's are output  
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);
pinMode(11,OUTPUT);
pinMode(10,OUTPUT);
pinMode(9,OUTPUT);
pinMode(8,OUTPUT);
}

void  loop() {
  // put your main code here, to run repeatedly:
  int ambientLight = analogRead(A0);
  if (ambientLight < 300 and speed < 200) {
    speed = speed + 25;
  } else if (ambientLight > 600 and speed > 50) {
    speed = speed - 50;
  }

  digitalWrite(led1,HIGH);//  here we will make the first pin high and the second pin high and so on.
  delay(speed);
  digitalWrite(led2,HIGH);
  delay(speed);
  digitalWrite(led3,HIGH);
  delay(speed);
  digitalWrite(led4,HIGH);
  delay(speed);
  digitalWrite(led5,HIGH);
  delay(speed);
  digitalWrite(led6,HIGH);
  delay(speed);

  digitalWrite(led1,LOW);
  delay(speed);
  digitalWrite(led2,LOW);
  delay(speed);
  digitalWrite(led3,LOW);
  delay(speed);
  digitalWrite(led4,LOW);
  delay(speed);
  digitalWrite(led5,LOW);
  delay(speed);
  digitalWrite(led6,LOW);
  delay(speed);
}