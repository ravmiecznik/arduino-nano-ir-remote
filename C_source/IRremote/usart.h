/*
 * usart.h
 *
 * Created: 2013-01-17 21:37:01
 *  Author: tmf
 */ 


#ifndef USART_H_
#define USART_H_

#include <avr/io.h>
#include <stdint.h>
#include <stdbool.h>

void USART_init();                                                     //Inicjalizacja USART
void USART_putchar(char ch);                                           //Wy�lij znak
void USART_send(const char __memx *txt);                               //Wy�lij �a�cuch w formacie NULLZ
void USART_send_block(const uint8_t __memx *block, uint8_t size);      //Wy�lij blok o d�ugo�ci size z pami�ci SRAM

static inline void waitforTx()            //Zaczekaj na koniec nadawania znaku
{
	while(!(UCSR0A & _BV(UDRE0)));
}

#endif /* USART_H_ */