/*
 * usart.c
 *
 * Created: 2013-01-17 21:39:25
 *  Author: tmf
 */ 

#include "usart.h"
#include <avr/pgmspace.h>


void USART_putchar(char ch)
{
	while(!(UCSR0A & _BV(UDRE0)));  //Zaczekaj na miejsce w buforze nadawczym
	UDR0=ch;
}

void USART_send(const char __memx *txt)
{
	while(*txt)
	{
		USART_putchar(*txt);
		++txt;
	}
}

void USART_send_block(const uint8_t __memx *block, uint8_t size)
{
	while(size--)
	{
		USART_putchar(*block);
		++block;
	}
}

static void uart_9600()
{
	#define BAUD 9600
	#include <util/setbaud.h>
	UBRR0H = UBRRH_VALUE;
	UBRR0L = UBRRL_VALUE;
	#if USE_2X
	UCSR0A |= (1 << U2X0);
	#else
	UCSR0A &= ~(1 << U2X0);
	#endif
}

void USART_init()
{
	uart_9600();  //Ustal szybkoœæ transferu na 9600 bps
	UCSR0B=_BV(RXEN0) | _BV(TXEN0);  //Odblokuj nadajnik i odbiornik
	UCSR0C=_BV(UCSZ00) | _BV(UCSZ01); //8 bitów danych + 1 bit stopu
}
