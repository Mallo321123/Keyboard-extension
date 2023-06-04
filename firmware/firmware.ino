int swich1 = 10;
int swich2 = 9;
int swich3 = 8;

int swich1_state;
int swich2_state;
int swich3_state;

int sw_r_state;
int sw_l_state;

int sw_r = 5;
int dt_r = 7;
int clk_r = 6;

int sw_l = 2;
int dt_l = 3;
int clk_l = 4;

int r;
int l;

int Pin_clk_Letzter_r;  
int Pin_clk_Aktuell_r;

int Pin_clk_Letzter_l;  
int Pin_clk_Aktuell_l;

void setup() {
  Serial.begin(9600);
  
  pinMode(swich1, INPUT_PULLUP);
  pinMode(swich2, INPUT_PULLUP);
  pinMode(swich3, INPUT_PULLUP);

  pinMode(sw_r, INPUT_PULLUP);
  pinMode(dt_r, INPUT_PULLUP);
  pinMode(clk_r, INPUT_PULLUP);

  pinMode(sw_l, INPUT_PULLUP);
  pinMode(dt_l, INPUT_PULLUP);
  pinMode(clk_l, INPUT_PULLUP);
  
  Pin_clk_Letzter_r = digitalRead(clk_r);
}

void loop() {
  if ((digitalRead(swich1) == LOW) && (swich1_state == 0)) {
    Serial.println("1");
    swich1_state = 30;
  } else if ((digitalRead(swich1) == HIGH) && (swich1_state > 0)) {
    swich1_state --;
  }

  if ((digitalRead(swich2) == LOW) && (swich2_state == 0)) {
    Serial.println("2");
    swich2_state = 30;
  } else if ((digitalRead(swich2) == HIGH) && (swich2_state > 0)) {
    swich2_state --;
  }

  if ((digitalRead(swich3) == LOW) && (swich3_state == 0)) {
    Serial.println("3");
    swich3_state = 30;
  } else if ((digitalRead(swich3) == HIGH) && (swich3_state > 0)) {
    swich3_state --;
  }


  if ((digitalRead(sw_r) == LOW) && (sw_r_state == 0)) {
    Serial.println("10");
    sw_r_state = 30;
  } else if ((digitalRead(sw_r) == HIGH) && (sw_r_state > 0)) {
    sw_r_state --;
  }

  if ((digitalRead(sw_l) == LOW) && (sw_l_state == 0)) {
    Serial.println("11");
    sw_l_state = 30;
  } else if ((digitalRead(sw_l) == HIGH) && (sw_l_state > 0)) {
    sw_l_state --;
  }


  Pin_clk_Aktuell_r = digitalRead(clk_r);
  if (Pin_clk_Aktuell_r != Pin_clk_Letzter_r){      
    if (digitalRead(dt_r) != Pin_clk_Aktuell_r) {  
      if (r == 0) {
        Serial.println("12");
        r = 1;
      } else {
        r = 0;
      }
    } else {
      if (r == 0) {
       Serial.println("13");
       r = 1;
      } else {
        r = 0;
      }
    }           
   } 
   Pin_clk_Letzter_r = Pin_clk_Aktuell_r;

   Pin_clk_Aktuell_l = digitalRead(clk_l);
  if (Pin_clk_Aktuell_l != Pin_clk_Letzter_l){      
    if (digitalRead(dt_l) != Pin_clk_Aktuell_l) {  
      if (l == 0) {
        Serial.println("14");
        l = 1;
      } else {
        l = 0;
      }
    } else {
      if (l == 0) {
        Serial.println("15");
        l = 1;
      } else {
        l = 0;
      }
    }           
   } 
   Pin_clk_Letzter_l = Pin_clk_Aktuell_l;
}
