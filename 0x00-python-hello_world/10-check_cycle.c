#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function that cheks if a linked list
 * has cycles
 * @list: pointer to the head of the list
 * Return: 1 if cycle or 0  in no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if( slow == fast)
			return (1);
	}
	return (0);
}
